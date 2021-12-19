from github import Github
import sys

gitToken = sys.argv[1]
pull_user = sys.argv[2]

gitObj = Github(gitToken)
user = gitObj.get_user(pull_user)

with open('data.csv', 'w') as file:
    file.write('public_repos,contribs\n')
    if (user.public_repos != None and user.contributions != None):
        file.write(str(user.public_repos) + ',' + str(user.contributions) + '\n')
    followers = user.get_followers()
    for fl in followers:
        if (fl.public_repos != None and fl.contributions != None):
            file.write(str(fl.public_repos) + ',' + str(fl.contributions) + '\n')