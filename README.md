# GitHub-Analyser


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
        1) Organization name
        2) Number of repositories {n}
        3) Number of committees {m}
        
    * Display top {n} repositories of the given organization on GitHub (Based on number of forks)
    * For each {n} repositories display {m} top committees (Based on number of commits)
    * When {n} is less then total repositories of the organization then it will display all repositories (<n)
    * When {m} is less then total committees of the repository then it will display all committees(<m)


- What is used:

    * Python/Django framework
    * GitHub API
