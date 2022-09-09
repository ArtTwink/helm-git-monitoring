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
    # print('Done')
# print(encode1)
helm_comment = re.findall(r'#.+', encode1)
# print(type(helm_comment))

# Name
chart_name = []
for i in helm_comment:
    chart_name.append(re.search('Source: (.+?)/', i).group(1))
print(chart_name)

# Essential
essential_name = []
for i in helm_comment:
    essential_name.append(re.search('\/(.+?)\/', i).group(1))
print(essential_name)

# File name
file_name = []
for i in helm_comment:
    file_name.append(re.search('\/.*', i))
print(file_name)
