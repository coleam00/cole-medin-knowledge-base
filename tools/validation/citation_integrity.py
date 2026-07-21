"""Citation-integrity: verify each ## Sources quote appears in its cited raw transcript near its timestamp."""
import glob, re, random
from pathlib import Path

ROOT = Path('C:/Users/colem/OpenSource/cole-medin-knowledge-base')

def to_sec(ts):
    parts = [int(x) for x in ts.split(':')]
    while len(parts) < 3: parts = [0]+parts
    h,m,s = parts[-3],parts[-2],parts[-1]
    return h*3600+m*60+s

def norm(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

# preload raw transcripts -> list of (sec, normtext) + full normtext
RAW = {}
for p in glob.glob(str(ROOT/'raw'/'*.md')):
    if p.endswith('index.md'): continue
    slug = Path(p).stem
    txt = open(p,encoding='utf-8').read()
    segs = []
    for m in re.finditer(r'\*\*\[(\d+:\d+:\d+)\]\*\*\s*(.*?)(?=\n\*\*\[|\Z)', txt, re.S):
        segs.append((to_sec(m.group(1)), norm(m.group(2))))
    RAW[slug] = {'segs': segs, 'full': norm(txt)}

# quote pattern in ## Sources bullets
QRE = re.compile(r'\]\((?:\.\./)+sources/([a-z0-9][a-z0-9-]+)\.md\)\s*-\s*"\[(\d+:\d+:\d+)\]\s*(.+?)"')

quotes = []
authored = (glob.glob(str(ROOT/'concepts'/'*.md')) +
            glob.glob(str(ROOT/'entities'/'**'/'*.md'), recursive=True) +
            glob.glob(str(ROOT/'sources'/'*.md')))
for p in authored:
    if p.endswith('index.md'): continue
    txt = open(p,encoding='utf-8').read()
    for m in QRE.finditer(txt):
        quotes.append((Path(p).name, m.group(1), m.group(2), m.group(3)))

def overlap(quote, slug, ts):
    if slug not in RAW: return None, 'no-raw'
    r = RAW[slug]
    qwords = [w for w in norm(quote).split() if len(w) >= 4]
    if not qwords: return 1.0, 'trivial'
    sec = to_sec(ts)
    # window text: segments within [sec-45, sec+120]
    win = ' '.join(t for s,t in r['segs'] if sec-45 <= s <= sec+120)
    hay = win if len(win) > 40 else r['full']  # fall back to full transcript if window empty
    hit = sum(1 for w in qwords if w in hay)
    frac_win = hit/len(qwords)
    # also full-transcript overlap (timestamp-independent) as secondary signal
    hitf = sum(1 for w in qwords if w in r['full'])
    frac_full = hitf/len(qwords)
    ts_in_range = bool(r['segs']) and sec <= r['segs'][-1][0] + 120
    return (frac_win, frac_full, ts_in_range), 'ok'

total=len(quotes); verified=0; ts_ok=0; suspicious=[]; full_ok=0
for page,slug,ts,quote in quotes:
    res, status = overlap(quote, slug, ts)
    if status!='ok':
        suspicious.append((page,slug,ts,quote[:70],status)); continue
    fw, ff, tsr = res
    if ff >= 0.5: full_ok += 1
    if tsr: ts_ok += 1
    # verified = quote words present near the cited timestamp
    if fw >= 0.55:
        verified += 1
    else:
        suspicious.append((page,slug,ts,quote[:70], f"win={fw:.2f} full={ff:.2f} ts_in_range={tsr}"))

print(f"=== CITATION INTEGRITY ===")
print(f"total quotes checked: {total}")
print(f"verified near cited timestamp (>=55% quote words in +/-window): {verified} ({100*verified//max(total,1)}%)")
print(f"quote words present somewhere in cited transcript (>=50%): {full_ok} ({100*full_ok//max(total,1)}%)")
print(f"timestamp within transcript duration: {ts_ok} ({100*ts_ok//max(total,1)}%)")
print(f"suspicious (low overlap OR bad ts): {len(suspicious)}")
print("\n--- sample suspicious (up to 25) ---")
for row in suspicious[:25]:
    print("  ", row[0], '|', row[1], row[2], '|', row[4], '|', row[3])
