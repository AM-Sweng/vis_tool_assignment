from os import write
from github import Github, RateLimitExceededException, GithubException
from datetime import datetime, timedelta
import sys

gitToken = sys.argv[1]
pull_user = sys.argv[2]

try:
    gitObj = Github(gitToken)
    user = gitObj.get_user(pull_user)

    # Get the average number of commits per day of this user in their repos over the last 3 months, and the number of repos commited to in the last three months
    repos = user.get_repos()
    repo_count = repos.totalCount
    avrg_commits_a_day = 0
    if repo_count > 0:
        commit_count = 0
        for rp in repos:
            try:
                commits = rp.get_commits(author = user, since = datetime.today() - timedelta(days=90)) # Get all commits within the last 3 months (roughly 90 days)
                if commits.totalCount > 0:
                    commit_count = commit_count + commits.totalCount
                else:
                    repo_count = repo_count - 1
            except GithubException: # If an exception arises from this repo, dont count it or the commits from it
                repo_count = repo_count - 1
        avrg_commits_a_day = commit_count / 90
        

    # Write the results to a csv file and find the same data on the users followers
    with open("data.csv", "w") as file:
        file.write("repo_count,commits_a_day\n")
        if repo_count > 0: # Avoid writing data on users who have not commited to their repos in the specified time (last 3 months)
            file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")
        followers = user.get_followers()
        for fl in followers:
            repos = fl.get_repos()
            repo_count = repos.totalCount
            avrg_commits_a_day = 0
            if repo_count > 0:
                commit_count = 0
                for rp in repos:
                    try:
                        commits = rp.get_commits(author = fl, since = datetime.today() - timedelta(days=90))
                        if commits.totalCount > 0:
                            commit_count = commit_count + commits.totalCount
                        else:
                            repo_count = repo_count - 1
                    except GithubException:
                        repo_count = repo_count - 1
                avrg_commits_a_day = commit_count / 90
                if repo_count > 0: # Avoid writing data on users who have not commited to their repos in the specified time (last 3 months)
                    file.write(str(repo_count) + "," + str(avrg_commits_a_day) + "\n")
    
    print("Script Completed")

except RateLimitExceededException as e:
    print(e)