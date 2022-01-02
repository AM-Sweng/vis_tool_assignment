# Software Engineering Visualisation App

This app is used to visualise on a scatterplot the number of repositories a user has commited something to in the last 3 months vs the average number of commits a day they did over the last 3 months. It focuses on the user's own repositories. It works by gathering data from one specified user and then gathering data from their followers. The only data collected, processed, and saved is the number of commits and number of repositories, no name, username, or location is associated with data in the resulting csv file.

## Requirements

This project requires Python, Pip, and PyGithub. These will have to be installed manually if running the scripts locally, but not if running through docker. If run through docker, everything necessary is installed on the container automatically.

You will also need a Github Personal Access Token to be able to use this.

## How to Run Locally

1. Run the script run_gather.sh followed by two arguments: your Personal Access Token, and the username of an account to start gathering from. Once complete, a new csv file will appear in the directory called data.csv.

        $ ./run_gather.sh ACCESS_TOKEN USERNAME

2. Run the script run-serv.sh. This will display the html page from index.html on localhost, on port 8000 by default. The exact port being used will be displayed on the terminal.

        $ ./run-serv.sh

## How to Run Through Docker

1. Run the script docker-build.sh. This will create the image and download all packages to the image necessary to run the python script and host the html page.

        $ ./docker-build.sh

2. Run docker-run-gather.sh followed by two arguments: your Personal Access Token, and the username of an account to start gathering from.

        $ ./docker-run-gather.sh ACCESS_TOKEN USERNAME

3. Run docker-run-serv.sh. This will display the html page from index.html, and can be accessed through localhost using port forwarding. The docker-run-serv.sh script uses localhost:8000 by default.

        $ ./docker-run-serv.sh