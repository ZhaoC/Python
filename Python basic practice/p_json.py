# example of reading json file
import json

json_data = json.loads(open("./test_files/samplejson.json").read())
print json_data["code"][0]
print json_data["code"][1]
print json_data["code"][2]
print json_data["code"][3]
