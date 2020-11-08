
import requests



class GithubOrg:

    def __init__(self, organization):

        self.organization = organization
        self.total_repo = 0



    def GetTopContributors(self, repo, m):

        '''

            This method returns the list of top 'm' contributers of a given repository
            of the organisation.

            Each contributor is a tuple of - 
                1) Name
                2) GitHub Profile Link
                3) Number of Contributions given

        '''

        url = f"https://api.github.com/repos/{repo}/contributors"
        content = requests.get(url).json()

        top_contributors = list() 

        for contributor in content:

            top_contributors.append(
                (
                    contributor['login'],
                    contributor['html_url'],
                    contributor['contributions'],
                )
            )

        return top_contributors[:m]



    def GetTopRepoAndContributors(self, n, m):

        '''

            This method returns the list of top 'n' repositories of of
            the organisation.

            Each repository is a tuple of - 
                1) Repository Name
                2) GitHub Link
                3) Number of Forks
                4) Top 'm' Contributors

        '''

        url = f"https://api.github.com/search/repositories?q=user:{self.organization}+sort:forks-desc&per_page={n}"
        content=requests.get(url).json()


        self.total_repo = content['total_count']
        content = content['items']
        top_repos = list()

        for repo in content:

            top_repos.append(
                (
                    repo['full_name'],
                    repo['html_url'],
                    repo['forks'],
                    self.GetTopContributors( repo['full_name'], m),
                )
            )

        return top_repos
