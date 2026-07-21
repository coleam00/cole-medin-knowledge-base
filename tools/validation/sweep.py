"""Supplementary sweep: agent-artifact leakage, encoding gremlins, link-graph health."""
import glob, re, os
from collections import Counter
from pathlib import Path

ROOT = Path('C:/Users/colem/OpenSource/cole-medin-knowledge-base')
md = [p for p in glob.glob(str(ROOT/'**'/'*.md'), recursive=True) if os.sep+'.git'+os.sep not in p]
authored = [p for p in md if any(('/'+d+'/') in p.replace('\\','/') for d in ('concepts','entities','sources'))]

# 1. leakage / placeholder patterns
LEAK = [r'\bas an AI\b', r'language model', r"\bI'm sorry\b", r'\bI cannot\b', r'\bTODO\b', r'\bFIXME\b',
        r'placeholder', r'\blorem ipsum\b', r'<slug>', r'<SLUG>', r'<path>', r'```json', r'ACK:', r'Here is the JSON',
        r'\bStep 1:\b', r'\bstructured output\b', r'I have written', r'I will ']
leak_hits = Counter()
leak_examples = []
for p in authored:
    t = open(p,encoding='utf-8').read()
    for pat in LEAK:
        for m in re.finditer(pat, t, re.I):
            leak_hits[pat]+=1
            if len(leak_examples)<20: leak_examples.append((os.path.basename(p), pat, t[max(0,m.start()-30):m.start()+40].replace('\n',' ')))

# 2. encoding gremlins beyond em-dash
GREMLINS = {'curly-dq':'[“”]','curly-sq':'[‘’]','mojibake-a':'Ã','mojibake-euro':'â‚¬',
            'mojibake-e2':'â€','replacement-char':'�','nbsp':' ','ellipsis-char':'…'}
grem = Counter()
for p in md:
    t = open(p,encoding='utf-8').read()
    for name,pat in GREMLINS.items():
        grem[name]+=len(re.findall(pat,t))

# 3. every ## Sources has >=1 source link
no_src_link=[]
for p in authored:
    t=open(p,encoding='utf-8').read()
    m=re.search(r'## Sources\s*(.*)$', t, re.S)
    if not m or not re.search(r'\]\((?:\.\./)+(?:sources|raw)/', m.group(1)):
        no_src_link.append(os.path.relpath(p,ROOT))

# 4. link graph: inbound counts among concepts+entities
LINK=re.compile(r'\]\(([^)]+\.md)\)')
inbound=Counter()
pages=[p for p in authored]
def resolve(src,link):
    return str((Path(src).parent/link.split('#')[0]).resolve())
allpaths={str(Path(p).resolve()):os.path.relpath(p,ROOT).replace('\\','/') for p in md}
for p in pages:
    t=open(p,encoding='utf-8').read()
    if os.path.basename(p)=='index.md': continue
    for l in LINK.findall(t):
        if l.startswith(('http','mailto:')): continue
        r=resolve(p,l)
        if r in allpaths: inbound[allpaths[r]]+=1
# concept/entity inbound distribution
ce = [allpaths[str(Path(p).resolve())] for p in glob.glob(str(ROOT/'concepts'/'*.md'))+glob.glob(str(ROOT/'entities'/'**'/'*.md'),recursive=True) if not p.endswith('index.md')]
counts=[inbound.get(x,0) for x in ce]
weak=[x for x in ce if inbound.get(x,0)<=1]
top=sorted(((inbound.get(x,0),x) for x in ce),reverse=True)[:8]

print("=== 1. AGENT-ARTIFACT / PLACEHOLDER LEAKAGE (authored pages) ===")
print("hits:", dict(leak_hits) if leak_hits else "NONE")
for e in leak_examples[:12]: print("  ", e[0],'|',e[1],'|',e[2])

print("\n=== 2. ENCODING GREMLINS (all md) ===")
print({k:v for k,v in grem.items() if v})

print("\n=== 3. authored pages whose ## Sources lacks a source/raw link ===")
print(len(no_src_link), no_src_link[:10])

print("\n=== 4. LINK GRAPH HEALTH (concept+entity inbound) ===")
print(f"pages={len(ce)} min={min(counts)} max={max(counts)} avg={sum(counts)/len(counts):.1f}")
print(f"weakly-linked (<=1 inbound): {len(weak)}")
print("  examples:", weak[:12])
print("top hubs:")
for c,x in top: print(f"  {c:>4}  {x}")
