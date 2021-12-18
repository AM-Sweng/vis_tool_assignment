from github import Github
import json

gitObj = Github()

user = gitObj.get_user("AM-Sweng")

dict = {
    'user': user.login,
    'fullname': user.name,
    'location': user.location,
    'company': user.company
}

print("The dictionary is " + json.dumps(dict))
