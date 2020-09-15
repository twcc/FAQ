import re
import os
from collections import defaultdict

bdir = "../"
not_bdir = [".", "..", ".git", "tools"]
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
                    foo, bar, cate1, cate2 = abs_md.split("/")
                    toc_buf[cate1][cate2].append(buf)

output = []
for cate1 in toc_buf:
    output.append("## [%s](%s)"%(cate1, cate1.replace(" ", "%20")))
    for cate2 in toc_buf[cate1]:
        output.append("### [%s](%s/%s)"%(cate2.replace(".md", ""), cate1.replace(" ", "%20"), cate2))
        for faq in toc_buf[cate1][cate2]:
            output.append("- %s"%faq)
            
open("../README.md", "w").write( open("README.md", "r").read().replace("{{TOC_HERE}}", "\n".join(output)))