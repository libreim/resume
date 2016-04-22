# -*- coding: utf-8 -*-

import subprocess
import os
import yaml



# Splits a file in two (three):
#  1. (REMOVED) a first empty file until the first YAML delimiter
#  2. the YAML header. The 1 offset keeps the final delimiter in this block
#  3. the body of the post
# The output files are named with a prefix
file="testfile.md"
#subprocess.Popen(["csplit","--keep-files","--elide-empty-files",file,"/---/1","/---/",'--prefix="post"'])
os.system("csplit --keep-files --elide-empty-files "+file+" /---/1 /---/ --prefix=\"post\"")

## YAML Header
stream = open("post01","r")
header = yaml.load(stream)

title = header["title"].encode('utf-8')
authors = ', '.join(header["authors"]).encode('utf-8')

headeroutput = """# {0}
*Autores: {1}*
""".format(title,authors)

outfile = open("post","w")
outfile.write(headeroutput)
outfile.close()

# Joins the header with the body
os.system('cat post02 >> post')
os.system('pandoc post -o post.pdf')
