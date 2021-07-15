import os

from github import Github

g = Github(os.getenv('GITHUB_TOKEN'))
GITHUB_USER = 'MachineUserHallicopter/'


def push_file_to_github(filename, content, repo):
    repo = g.get_repo(GITHUB_USER + repo)
    print(repo.create_file(path=filename, content=content, message="adds: autocommit new post", branch="gh-pages"))


def update_template(repo):
    repo = g.get_repo(GITHUB_USER + repo)
    # Create and push the template
    os.system('create_repo.sh ' + repo + ' ' + os.getenv('GITHUB_TOKEN'))
