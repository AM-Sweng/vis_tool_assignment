from github import Github
import json

gitObj = Github()

user = gitObj.get_user("AM-Sweng")

usr_list = []
usr_data = {
    'public_repos': user.public_repos,
    'contribs': user.contributions
}
usr_list.append(usr_data)
followers = user.get_followers()
for fl in followers:
    usr_data = {
        'public_repos': fl.public_repos,
        'contribs': fl.contributions
    }
    usr_list.append(usr_data)

with open('data.json', 'w') as file:
    file.write(json.dumps(usr_list))