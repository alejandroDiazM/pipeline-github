import sys
import requests

project_id = sys.argv[1]
auth_token = sys.argv[2]

header = {'Authorization': f'Bearer {auth_token}'}
try:
    r = requests.get(f'https://gitlab.com/api/v4/projects/{project_id}/releases', headers=header)
    r.raise_for_status()

    releases = r.json()
    if not releases:
        print(f"export FIRST_RELEASE=1")
    else:
        last_tag = releases[0].get('tag_name')
        print(f"export LAST_TAG={last_tag}")
        print(f"export FIRST_RELEASE=0")

except requests.HTTPError:
    exit(1)
