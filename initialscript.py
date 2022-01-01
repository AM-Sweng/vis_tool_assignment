from os import write
from github import Github
from datetime import datetime, timedelta
import sys

gitToken = sys.argv[1]
pull_user = sys.argv[2]

gitObj = Github(gitToken)
user = gitObj.get_user(pull_user)

# Get the average number of commits per day of this user in their repos over the last 3 months, and the number of repos commited to in the last three months
repos = user.get_repos()
repo_count = repos.totalCount
avrg_commits_a_day = 0
if repo_count != 0:
    commit_count = 0
    for rp in repos:
        used_within_last_3_months = False # Assume this repo was not commited to by the user in the last 3 months
        commits = rp.get_commits()
        for cm in commits:
            if cm.author != None:
                if cm.author.login == user.login:
                    if cm.commit.author.date >= datetime.today() - timedelta(days=90): # Check that the commit was within the last 3 months (roughly 90 days)
                        commit_count = commit_count + 1
                        used_within_last_3_months = True
        if not used_within_last_3_months:
            repo_count = repo_count - 1
    avrg_commits_a_day = commit_count / 90
    

# Write the results to a csv file and find the same data on the users followers
with open("data.csv", "w") as file:
    file.write("repo_count,commits_a_day\n")
    file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")
    followers = user.get_followers()
    for fl in followers:
        repos = fl.get_repos()
        repo_count = repos.totalCount
        avrg_commits_a_day = 0
        if repo_count != 0:
            commit_count = 0
            for rp in repos:
                used_within_last_3_months = False
                commits = rp.get_commits()
                for cm in commits:
                    if cm.author != None:
                        if cm.author.login == fl.login:
                            if cm.commit.author.date >= datetime.today() - timedelta(days=90):
                                commit_count = commit_count + 1
                                used_within_last_3_months = True
                if not used_within_last_3_months:
                    repo_count = repo_count - 1
            avrg_commits_a_day = commit_count / 90
        file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")