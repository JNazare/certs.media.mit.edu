import os
import json
import hashlib

from config import JSONS_PATH, DATA_PATH, PUBKEYMAP_PATH

pubkey_mappings = {}
for filename in os.listdir(JSONS_PATH):
	if filename.split(".")[1]=="json":
		pubkey = json.loads(open(JSONS_PATH+filename).read())["recipient"]["pubkey"]
		pubkey_mappings[pubkey]=filename.split(".")[0]

open(PUBKEYMAP_PATH, "wb").write(json.dumps(pubkey_mappings))