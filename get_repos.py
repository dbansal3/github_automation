from github import Github

# using an access token
g = Github('dbansal3', 'Deepanshu@2022')
print ("res : {}".format(g))

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

user = g.get_user('dbansal3').get_repos()
print(user)

for repo in g.get_user().get_repos():
    print(repo)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
