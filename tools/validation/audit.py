"""Comprehensive audit + citation-integrity check for the OKF bundle."""
import glob, os, re, json
from pathlib import Path

ROOT = Path('C:/Users/colem/OpenSource/cole-medin-knowledge-base')

def fm_and_body(text):
    if not text.startswith('---'):
        return {}, text
    end = text.find('\n---', 3)
    if end < 0:
        return {}, text
    raw = text[3:end]
    fm = {}
    for line in raw.splitlines():
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, text[end+4:]

def has_list(fm, key):
    return key in fm and '[' in fm.get(key, '')

problems = []
def prob(cat, msg):
    problems.append((cat, msg))

# ---- gather ----
concepts = [p for p in glob.glob(str(ROOT/'concepts'/'*.md')) if not p.endswith('index.md')]
tools = [p for p in glob.glob(str(ROOT/'entities'/'tools'/'*.md')) if not p.endswith('index.md')]
people = [p for p in glob.glob(str(ROOT/'entities'/'people'/'*.md')) if not p.endswith('index.md')]
orgs = [p for p in glob.glob(str(ROOT/'entities'/'organizations'/'*.md')) if not p.endswith('index.md')]
sources = [p for p in glob.glob(str(ROOT/'sources'/'*.md')) if not p.endswith('index.md')]
raws = [p for p in glob.glob(str(ROOT/'raw'/'*.md')) if not p.endswith('index.md')]
source_slugs = {Path(p).stem for p in sources}
raw_slugs = {Path(p).stem for p in raws}

print("=== COUNTS ===")
print(f"concepts={len(concepts)} tools={len(tools)} people={len(people)} orgs={len(orgs)} "
      f"sources={len(sources)} raw={len(raws)}")

# ---- frontmatter completeness ----
titles = {}
for p in concepts:
    fm, body = fm_and_body(open(p,encoding='utf-8').read())
    for k in ('type','title','description'):
        if not fm.get(k): prob('concept-fm', f"{Path(p).name} missing {k}")
    if fm.get('type') != 'concept': prob('concept-fm', f"{Path(p).name} type!=concept")
    if not has_list(fm,'videos'): prob('concept-fm', f"{Path(p).name} missing videos[]")
    titles.setdefault(fm.get('title','').lower(), []).append('concepts/'+Path(p).name)
    # word count
    wc = len(body.split())
    if wc < 120: prob('thin', f"concepts/{Path(p).name} only {wc} words")
    if '## Sources' not in body: prob('sources-sec', f"concepts/{Path(p).name} no ## Sources")

for group,plist,sub in (('tool',tools,'tool'),('person',people,'person'),('org',orgs,'organization')):
    for p in plist:
        fm, body = fm_and_body(open(p,encoding='utf-8').read())
        if fm.get('type')!='entity': prob('entity-fm', f"{Path(p).name} type!=entity")
        if fm.get('subtype')!=sub: prob('entity-fm', f"{Path(p).name} subtype!={sub} (got {fm.get('subtype')})")
        for k in ('title','description'):
            if not fm.get(k): prob('entity-fm', f"{Path(p).name} missing {k}")
        titles.setdefault(fm.get('title','').lower(), []).append(Path(p).parent.name+'/'+Path(p).name)
        wc=len(body.split())
        if wc<120: prob('thin', f"{Path(p).parent.name}/{Path(p).name} only {wc} words")
        if '## Sources' not in body: prob('sources-sec', f"{Path(p).parent.name}/{Path(p).name} no ## Sources")

for p in sources:
    fm, body = fm_and_body(open(p,encoding='utf-8').read())
    for k in ('type','title','youtube_id','url','slug','raw','published','duration','recency_rank'):
        if fm.get(k) in (None,''): prob('source-fm', f"{Path(p).name} missing {k}")
    if fm.get('type')!='source': prob('source-fm', f"{Path(p).name} type!=source")
    # raw link resolves
    rawlink = fm.get('raw','').strip('"')
    if rawlink:
        if not (Path(p).parent/rawlink).resolve().exists(): prob('source-raw', f"{Path(p).name} raw link broken: {rawlink}")
    if Path(p).stem not in raw_slugs: prob('parity', f"source {Path(p).stem} has no raw")

# ---- dup titles ----
for t,ps in titles.items():
    if t and len(ps)>1: prob('dup-title', f"title '{t}' on {ps}")

# ---- videos[] cross-ref ----
missing_vid = 0
for p in concepts+tools+people+orgs:
    fm,_ = fm_and_body(open(p,encoding='utf-8').read())
    v = fm.get('videos','')
    if '[' in v:
        for slug in re.findall(r'[a-z0-9][a-z0-9-]+', v):
            if slug not in source_slugs and slug not in ('videos',):
                # only flag things that look like slugs (len>4) and aren't real
                if len(slug)>6 and slug not in source_slugs:
                    missing_vid += 1
print(f"\n=== videos[] refs not matching a source slug: ~{missing_vid} (heuristic) ===")

# ---- taxonomy consistency ----
tax = json.load(open(ROOT/'scripts'/'taxonomy.json',encoding='utf-8'))
tax_c = [s for _,ss in tax['concept_themes'] for s in ss]
file_c = {Path(p).stem for p in concepts}
if set(tax_c)!=file_c:
    prob('taxonomy', f"concept mismatch: in-tax-not-file={sorted(set(tax_c)-file_c)[:5]}, in-file-not-tax={sorted(file_c-set(tax_c))[:5]}")
if len(tax_c)!=len(set(tax_c)): prob('taxonomy','concept appears in >1 theme')

print("\n=== PROBLEMS ===")
if not problems:
    print("NONE")
else:
    from collections import Counter
    c = Counter(cat for cat,_ in problems)
    for cat,n in c.most_common():
        print(f"[{cat}] {n}")
    for cat,msg in problems[:40]:
        print(f"  {cat}: {msg}")
print(f"\nTOTAL PROBLEMS: {len(problems)}")
