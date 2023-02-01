import os 
HOMEDIR = 'c:\\git\\proj11'
html = ''
for fname in os.listdir (os.path.join(HOMEDIR,'data')):
    print(fname)
    html +=f'<p><a href="data/{fname}">{fname.replace(".html","")}</a></p>\n'
print(html)
    # with open 