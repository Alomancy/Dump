
import json

from lib import utils

vulns = utils.get('https://wpvulndb.com/api/v2/wordpresses/43')
json_string = vulns.content
parsed_json = json.loads(json_string)
for i in parsed_json:
    for v in parsed_json[i]['vulnerabilities']:
        print(v)
# print (parsed_json['4.3']['vulnerabilities'])