import re
import subprocess
from itertools import groupby

output = subprocess.getoutput("helm get all -n default car")
print(type(output))
encode1 = output.partition('MANIFEST:') [-1]
print("encode1 :", encode1, type(encode1))
# encode2 = encode1.partition('\n')
# helm_cut = re.split('MANIFEST: ', output)
# print(helm_cut)
manifests = re.split('#', output)

# Name of files
# for i in manifests:
#     print(i, sep=",,,,,,,,,")
# x = re.findall


with open('data.txt', 'w') as f:
    for item in manifests:
        f.write("%s\n" % item.split(','))
    print('Done')