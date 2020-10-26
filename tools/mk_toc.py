import re
import os
from collections import defaultdict

if 'GITHUB_WORKSPACE' in os.environ:
    bdir = os.environ['GITHUB_WORKSPACE'] 
else:
    bdir = "../"
    
not_bdir = [".", "..", ".git", ".circleci", "venv", "tools", ".github"]
toc_buf = defaultdict(lambda: defaultdict(list)) # https://stackoverflow.com/a/27809959
for fn in os.listdir(bdir):
    wdir = bdir+os.path.sep+fn
    if not fn in not_bdir and os.path.isdir(wdir):
        for md in os.listdir(wdir):
            abs_md = wdir+os.path.sep+md
            cnt = open(abs_md, 'r').readlines()
            for li in cnt:
                if re.search(":::spoiler Q", li):
                    buf = li.strip().replace(":::spoiler ", "")
                    dirs =  abs_md.split("/")
                    cate1, cate2 = dirs[-2], dirs[-1]
                    toc_buf[cate1][cate2].append(buf)

output = []
for cate1 in sorted(toc_buf.keys()):
    output.append("## [%s](%s)"%(cate1, cate1.replace(" ", "%20")))
    for cate2 in sorted(toc_buf[cate1].keys()):
        output.append("### [%s](%s/%s) (%s) "%(cate2.replace(".md", ""), cate1.replace(" ", "%20"), cate2, len(toc_buf[cate1][cate2])))
        for faq in toc_buf[cate1][cate2]:
            output.append("- %s"%faq)

open("../README.md", "w").write( open("README.md", "r").read().replace("{{TOC_HERE}}", "\n".join(output)))
