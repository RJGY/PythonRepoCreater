#!/usr/bin/env python3

# TODO: make this work with bash
import requests
from decouple import config
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private" "-p", dest="is_private", action="store_true")

args = parser.parse_args()

repo_name = args.name
repo_is_private = args.is_private

API_URL = "https://api.github.com"

if (repo_is_private):
    api_data = '{ "name" : "' + repo_name + '", "private" : true }'
else: 
    api_data = '{ "name" : "' + repo_name + '", "private" : false }'

header_data = {
    "Authorization" : "token " + config('TOKEN'),
    "Accept" : "applictation/vnd.github.v3+json"
}
try:
    req = requests.post(API_URL + "/user/repos", data=api_data, headers=header_data)
    req.raise_for_status()

except requests.exceptions.RequestException as err:
    raise SystemExit(err)

try: 
    os.system("mkdir " + repo_name)
    os.chdir(repo_name)
    os.system("git init")
    os.system("git remote add origin " + config('GITHUB') + repo_name + ".git")
    os.system("echo # " + repo_name + " >> README.md")
    os.system('git add . && git commit -m "Initial commit" && git push --set-upstream origin main')

except FileExistsError as err:
    raise SystemExit(err)
