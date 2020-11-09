from django.shortcuts import render
from .GitHub import GithubOrg

# Create your views here.


# Website Entry Point

def home_page_view(request):

    return render( request, 'home_page.html')




# Listing the Repositories Fetched

def repo_page_view(request):
    
    # Input given on home_page
    organization_name = request.GET['Organization']
    m = request.GET['mValue']
    n = request.GET['nValue']
    
    # parsing m and n to integer value
    m = int(m)
    n = int(n)

    # Instance of class GithubOrg with given organisation
    organization = GithubOrg( organization_name )
    repos = organization.GetTopRepoAndContributors( n, m)

    # If given organization is inValid 

    if(repos['status'] != 'ok'): 

        return error_page_view(request,repos['status'])


    return render( request,'repo_page.html',
            {
                'organization_name' : organization_name,
                'repo_list' : repos['top_repo'],
                'total_repo' : organization.total_repo,
                'n': n,
                'm' : m,
            }
        )



# For Invalid Organisations or Request Limit Reached

def error_page_view(request,message):

    return render( request, 'error_page.html',
        {
            'message': message,
        }
    )