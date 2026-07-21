import sys, glob, re, os, numpy as np
sys.path.insert(0, 'C:/Users/colem/dynamous-engine/.claude/scripts')
from embeddings import embed_batch

root = 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'

def load(group):
    items = []
    for p in glob.glob(root + '/' + group + '/**/*.md', recursive=True):
        if p.endswith('index.md'):
            continue
        t = open(p, encoding='utf-8').read()
        fe = t.find('\n---', 3)
        ti = re.search(r'^title:\s*(.+)$', t[:fe], re.M)
        de = re.search(r'^description:\s*(.+)$', t[:fe], re.M)
        slug = os.path.basename(p)[:-3]
        label = group.split('/')[0] + '/' + slug
        text = (ti.group(1).strip('"\'') if ti else slug) + '. ' + (de.group(1).strip('"\'') if de else '')
        items.append((label, text))
    return items

for name, group in [('CONCEPTS', 'concepts'), ('TOOLS', 'entities/tools')]:
    items = load(group)
    embs = np.array(embed_batch([x[1] for x in items]))
    embs = embs / np.linalg.norm(embs, axis=1, keepdims=True)
    sim = embs @ embs.T
    n = len(items)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if sim[i, j] >= 0.86:
                pairs.append((float(sim[i, j]), items[i][0], items[j][0]))
    pairs.sort(reverse=True)
    print(f"\n=== {name}: {n} pages, near-duplicate pairs (cosine>=0.86): {len(pairs)} ===")
    for s, a, b in pairs[:20]:
        print(f"  {s:.3f}  {a}   <->   {b}")
