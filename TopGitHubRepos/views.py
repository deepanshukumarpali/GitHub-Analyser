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


    # try:

    #     # If given organization is Valid 
    #     top_repo_list = organization.GetTopRepoAndContributors( n, m)
    # except:

    #     # If given  organization is not Valid
    #     message = "Error! Invalid Organization or Request Limit Reached"
    #     return error_page_view(request,message)

    top_repo_list = [
        ('PBhustle','https://github.com/flenoir/purbeurre',20, [ ('sparsh','www.google.com',12),('sparsh','www.google.com',12) ] ),
        ('PBhustle','https://github.com/flenoir/purbeurre',20, [ ('sparsh','www.google.com',12),('sparsh','www.google.com',12) ] ),
        ('PBhustle','https://github.com/flenoir/purbeurre',20, [ ('sparsh','www.google.com',12),('sparsh','www.google.com',12) ] )
    ]


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