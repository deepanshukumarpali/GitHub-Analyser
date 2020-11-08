# GitHub-Analyser

#### Link: ---



- How to Use Locally:

    * Download this repository.
    * Open project directory.
    * Run following command
    ```bash
        $ python manage.py runserver
    ```

- What it does:

    * Takes 3 input values
        * Organisation name
        * Number of repositories (n)
        * Number of contributors (m)
    * Display top {n} repositories of the given organisation on GitHub (Based on number of forks)
    * For each {n} cepositories display {m} top contributors (Based on number of commits)

- What is used:

    * Python/Django framework
    * GitHub API
