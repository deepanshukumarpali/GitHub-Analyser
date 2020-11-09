
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

        return_obj = {
            'status': 'ok',
            'top_repo': list() 
        }

        try: 
            self.total_repo = content['total_count']

        except: 

            # When organization in inValid

            return_obj['status']="Organization Not Found"
            return return_obj
        
        content = content['items']

        for repo in content:

            name=repo['full_name']
            link=repo['html_url']
            forks=repo['forks']

            try:  
                contributors=self.GetTopContributors( repo['full_name'], m)

            except:
                
                # API request Error " API Rate Limit Exceeded "
                return_obj['status']="Request Limit Exceeded"
                break

            return_obj['top_repo'].append(
                (
                    name,
                    link,
                    forks,
                    contributors,
                )
            )

        return return_obj

