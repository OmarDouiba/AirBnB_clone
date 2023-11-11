#!/usr/bin/python3
import json

file_path =  "file.json"
with open(file_path, "w") as f:
    json.dump({"hi":11}, f)
print(file_path)
print(type(file_path))