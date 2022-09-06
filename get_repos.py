from github import Github

# using an access token
g = Github('dbansal3', 'Deepanshu@2022')
print ("res : ".format(g))

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

