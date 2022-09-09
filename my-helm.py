from distutils.filelist import findall
import re
import subprocess
from itertools import groupby
from xml.etree.ElementTree import Comment

output = subprocess.getoutput("helm get all -n default car")
# print(type(output))
encode1 = output.partition('MANIFEST:') [-1]
# print("encode1 :", encode1, type(encode1))
# name_manifests = 
# manifests = re.split('#', output)

with open('data.txt', 'w') as f:
    for item in encode1:
        f.write(item)
        # f.write("%s\n" % item.split(','))
    print('Done')
print(encode1)
comment = re.findall(r'#.+', encode1)
print(comment) 
# print(encode1.split('#'), sep=',')
# for i in list(encode1):
#     print(i)