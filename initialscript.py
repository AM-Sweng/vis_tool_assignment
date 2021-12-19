from github import Github

gitObj = Github()

user = gitObj.get_user("AM-Sweng")

with open('data.csv', 'w') as file:
    file.write('public_repos,contribs\n')
    file.write(user.public_repos + ',' + user.contributions + '\n')
    followers = user.get_followers()
    for fl in followers:
        file.write(fl.public_repos + ',' + fl.contributions + '\n')