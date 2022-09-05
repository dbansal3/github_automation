'''
1. Update the constants in the script.
2. PERMISSION should be given in folowing manner:
    "push" --> for Write
    "pull" --> for Read
    "triage" --> for Triage
    "maintain" --> for Maintain
    "admin" --> for Admin
3. Add the github handles to be added to users.txt
4. Place users.txt and this script in the same location
5. Install PyGithub ---> pip install PyGithub
5. Run the script with Python 3
'''   

from github import Github
from github import GithubException

'''
PAT = "PROVIDE YOUR GITHUB TOKEN HERE"
ORG_NAME = "ORGANIZATION NAME FROM URL"
REPO_NAME = "REPO NAME URL"
PERMISSION = "REFER ABOVE TO PROVIDE THE PERMISSION"
'''

PAT = "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"
ORG_NAME = "dbansal3"
REPO_NAME = "sonar-scanning-examples"
PERMISSION = "pull"


def add_users():
    user_file = open("./users.txt","r")
    users = user_file.readlines()
    user_file.close()
    gh = Github(login_or_token=PAT)
    for user in users:
        try:
            ghuser = gh.get_user(user.strip())
        except GithubException:
            print("Could not detect user {}".format(user.strip()))
            continue
        try:
            gh.get_repo(ORG_NAME+"/"+REPO_NAME).add_to_collaborators(ghuser,PERMISSION)
        except GithubException:
            print("Error in adding user {}".format(user.strip()))
            continue
        print("{} added to repo {}".format(user.strip(),REPO_NAME))
        
add_users()
