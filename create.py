import sys
import os
from github import Github

username = sys.argv[1]
gh_key = sys.argv[2]
repo_name = sys.argv[3]

def create():
    user = Github(gh_key).get_user()
    repo = user.create_repo(repo_name)
    print(f"Succesfully created repository {repo_name}")

if __name__ == "__main__":
    create()