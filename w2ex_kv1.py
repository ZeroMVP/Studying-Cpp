import os
import tempfile
import json
import argparse

json_data = {}
parser = argparse.ArgumentParser()
parser.add_argument("--key", help = "find by key or create new one ")
parser.add_argument("--val", help = "value to key")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data11()')
if(os.path.exists(storage_path) == False):
    with open(storage_path, 'w') as f:
        q = json.dumps({'fucking_key_4_work':5})
        f.write(q)
#if (os.path.exists(storage_path) == None):
#    tempfile.TemporaryFile()
#with open(storage_path, 'w') as f:
#    q = json.dumps({'5': [4,7], '6' : [11], '10': [20]})
#    f.write(q)
with open(storage_path, 'r') as f:
    json_data = json.load(f)
if(args.val == None):
        print(json_data.get(args.key, None))
else:
    with open(storage_path, 'w') as f:
        listed = []
        if(json_data.get(args.key,None) == None):
            listed = []
        else:
            listed = json_data[args.key]
        listed.append(args.val)
        json_data[args.key] = listed
        json.dump(json_data,f)
        #json_data[args.key] = args.val
        #q = json.dump(json_data,f)


