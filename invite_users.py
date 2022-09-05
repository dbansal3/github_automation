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


def add_users(self):
    user_file = open("./users.txt","r")
    users = user_file.readlines()
    user_file.close()
    gh = Github(login_or_token=PAT)
    print("Login to github : {}".format(gh))
    for user in users:
        print("user : {}".format(user))
        try:
            # ghuser = gh.get_user(user.strip())
            gh.get_user(self._login).create_repo("testing_automation")
        except Exception as e:
            print("Exception is : {}".format(e))
            print("Could not detect user {}".format(user.strip()))
            continue
        '''
        except GithubException:
            print("Could not detect user {}".format(user.strip()))
            continue
        '''
        try:
            gh.get_repo(ORG_NAME+"/"+REPO_NAME).add_to_collaborators(ghuser,PERMISSION)
        except GithubException:
            print("Error in adding user {}".format(user.strip()))
            continue
        print("{} added to repo {}".format(user.strip(),REPO_NAME))
        
add_users(self)
