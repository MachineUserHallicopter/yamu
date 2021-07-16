import os
from github import Github
import yaml

g = Github(os.getenv('GITHUB_TOKEN'))
GITHUB_USER = 'MachineUserHallicopter/'


def push_file_to_github(filename, content, repo):
    repo = g.get_repo(GITHUB_USER + repo)
    print(repo.create_file(path=filename, content=content, message="adds: autocommit new post", branch="gh-pages"))


def update_template(repo):
    file_name = 'template/_config.yml'
    print("title: "+repo+"\nbaseurl: '/"+repo+"/' # name of the repository")
    file = open(file_name, "a")  # append mode
    file.write("title: "+repo+"\nbaseurl: '/"+repo+"/' # name of the repository")
    file.close()

    # Create and push the template
    os.system('./create_repo.sh ' + repo + ' ' + os.getenv('GITHUB_TOKEN'))

update_template("yamu")