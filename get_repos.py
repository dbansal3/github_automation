from github import Github

# using an access token
g = Github('dbansal3', 'Deepanshu@2022')
print ("res : {}".format(g))

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

user = g.get_user()
print(user.name)
print(user.login)


for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
