import requests
from github import Github
from properties import TOKEN

try:
    gh_conn = Github(TOKEN)
    user = gh_conn.get_user()
    repo = user.get_repo("pipeline_test")
    releases = repo.get_tags()

    if not releases:
        print(f"export FIRST_RELEASE=1")
    else:
        last_tag = releases[0].get('name')
        print(f"export LAST_TAG={last_tag}")
        print(f"export FIRST_RELEASE=0")

except requests.HTTPError:
    exit(1)

