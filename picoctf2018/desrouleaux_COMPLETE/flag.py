import json

with open('incidents.json') as json_file:
    data = json.load(json_file)

t = len(data['tickets'])

src_ip = []
dst_ip = []
files = []

for i in range(t):
    src_ip.append(data['tickets'][i]['src_ip'])
    dst_ip.append(data['tickets'][i]['dst_ip'])
    files.append(data['tickets'][i]['file_hash'])

print(set(files))
print(set(dst_ip))
print(set(src_ip))