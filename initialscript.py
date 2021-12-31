from os import write
from github import Github
from datetime import date
import sys

gitToken = sys.argv[1]
pull_user = sys.argv[2]

gitObj = Github(gitToken)
user = gitObj.get_user(pull_user)

# Get the average number of commits per day of this user in their repos, and the number of repos involved
repos = user.get_repos()
repo_count = repos.totalCount
if repo_count != 0:
    commit_count = 0
    commit_times = []
    for rp in repos:
        commits = rp.get_commits()
        for cm in commits:
            if cm.author != None:
                if cm.author.login == user.login:
                    commit_count = commit_count + 1
                    commit_times.append(cm.commit.author.date.date()) # only need the date since we are just counting the number of commits
    commit_times.sort()
    delta = commit_times[-1] - commit_times[0]
    avrg_commits_a_day = commit_count / delta.days
else:
    avrg_commits_a_day = 0

# Write the results to a csv file and find the same data on the users followers
with open("data.csv", "w") as file:
    file.write("repo_count,commits_a_day\n")
    file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")
    followers = user.get_followers()
    for fl in followers:
        repos = fl.get_repos()
        repo_count = repos.totalCount
        if repo_count != 0:
            commit_count = 0
            commit_times = []
            for rp in repos:
                commits = rp.get_commits()
                for cm in commits:
                    if cm.author != None:
                        if cm.author.login == fl.login:
                            commit_count = commit_count + 1
                            commit_times.append(cm.commit.author.date.date()) # only need the date since we are just counting the number of commits
            commit_times.sort()
            delta = commit_times[-1] - commit_times[0]
            avrg_commits_a_day = commit_count / delta.days
        else:
            avrg_commits_a_day = 0
        file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")