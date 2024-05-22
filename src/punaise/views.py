#import Python

#Django import

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

##############
#Public Views#
##############

def public_views (request):

    #Get me as the user
    me = request.user

    #Variable test

    hello = "Bienvenvue sur Elevage"

    #Context variable for the html

    context = {
        "elevage" : hello
    }

    return render (request, "index.html", context)

###############
#Gallery Views#
###############

def gallery_views (request):

    #Get me as the user
    me = request.user

    return render (request, "gallery.html")



###############
#Contact Views#
###############

def contact_views (request):

    #Get me as the user
    me = request.user

    return render (request, "contact.html")