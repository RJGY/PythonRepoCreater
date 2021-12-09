import requests
from pprint import pprint
from decouple import config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private" "-p", dest="is_private", action="store_true")

args = parser.parse_args()

repo_name = args.name
repo_is_private = args.is_private

API_URL = "https://api.github.com"

if (repo_is_private):
    api_data = '{ "name" : ' + repo_name + ', "private" : true }'
else: 
    api_data = '{ "name" : ' + repo_name + ', "private" : false }'

headerdata = {
    "Authorization" : "token " + config('TOKEN'),
    "Accept" : "applictation/vnd.github.v3+json"
}
try:
    req = requests.post(API_URL + "/user/repos", data=apidata, headers=headerdata)
    req.raise_for_status()

except requests.exceptions.RequestException as err:
    raise SystemExit(err)
