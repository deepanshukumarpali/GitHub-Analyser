# GitHub-Analyser

#### Link: https://github-repo-analyser.herokuapp.com



- How to Use Locally:

    * Download this repository.
    * Open terminal
    * Run the following command
    ```bash
        $ cd [project_directory]
        $ python manage.py runserver
    ```

- What it does:

    * Takes 3 input values
        1) Organisation name
        2) Number of repositories (n)
        3) Number of contributors (m)
        
    * Display top {n} repositories of the given organisation on GitHub (Based on number of forks)
    * For each {n} repositories display {m} top committees (Based on number of commits)

- What is used:

    * Python/Django framework
    * GitHub API
