from distutils.filelist import findall
import os
import re
import subprocess


output = subprocess.getoutput("helm get all -n default car")
# print(output)
# print(type(output))
cut_output = output.partition('MANIFEST:') [-1]
# print("cut_output :", cut_output, type(cut_output))
# name_manifests = 
# manifests = re.split('#', output)

with open('data.txt', 'w') as f:
    for item in cut_output:
        f.write(item)
        # f.write("%s\n" % item.split(','))
    # print('Done')
# print(cut_output)
helm_comment = re.findall(r'#.+', cut_output)
# print(type(helm_comment))
# print(helm_comment)

# Namespace
namespace_name = []
# print(output)
# namespace_name.append(re.findall('NAMESPACE: (.*?)$', output).group(1))
# print(re.search('NAMESPACE: (.*?)$', output))
# print(namespace_name)

# Name
chart_name = []
for i in helm_comment:
    chart_name.append(re.search('Source: (.+?)/', i).group(1))
# print(chart_name)

# Essential
essential_name = []
for i in helm_comment:
    essential_name.append(re.search('\/(.+?)\/', i).group(1))
# print(essential_name)

# File name
file_name = []
for i in helm_comment:
    # print(i, sep='')
    file_name.append(re.search('/.*?/(.*?)$', i).group(1))
# print(file_name)

# Kind
k8s_kind = []
# for i in cut_output:
#     print(i)
#     print(re.search('kind:', i).group(1))
#     k8s_kind.append(re.search('kind: (.+?)$', i).group(1))
# print(k8s_kind)

k8s_kind.append(re.search('kind:(.+?)$', cut_output))
print(k8s_kind)

# Name of kind
# kind_name = []
# for i in cut_output:
#     kind_name.append(re.search('\n  name: (.+?)$', i).group(1))
# print(kind_name)

# Creating files
# for i in chart_name:
#     os.mkdir(i)
#     create_name = os.path.join(i, file_name)
#     with open(i, 'wt') as f:
#         f.write('example')
