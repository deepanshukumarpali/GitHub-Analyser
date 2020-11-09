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
    top_repo_list = organization.GetTopRepoAndContributors( n, m)

    # If given organization is inValid 

    if(len(top_repo_list)==0): 
        return error_page_view(request,"Organization Not Found")


    return render( request,'repo_page.html',
            {
                'organization_name' : organization_name,
                'repo_list' : top_repo_list,
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