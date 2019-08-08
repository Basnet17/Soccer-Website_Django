from django.http import HttpResponse
from django.shortcuts import render
import requests
import http.client
import json

# Create your views here.
def findValues (key,d):
    '''
    Purpose:
        Recursively goes down JSON tree to see if tag inputted by user is in user dictionary
    Parameters:
        key: tag looking for in JSON tree
        dj: JSON tree as dictionary
    Return value:
        Returns path to first occurence if found in JSON tree, if not then returns empty string
    '''
    list1 = []                                     #initialising the empty list
    if key in d and isinstance(d[key],str):        #base case to check if the key is in d
        list1.append(d[key])                       #append the value of the dictionary

    else:
        for keys in d:                             #iterate through all keys in d
            val = d[keys]                          #set the values of to be val
            if isinstance(val,dict):               #just check if the val is dictionary
                if findValues(key,val):
                    list1 += findValues(key,val)       #add the old list to the new list

            elif isinstance(val,list):             #if the val is list then iterate through the list and pick items
                for item in val:
                    if isinstance(item,dict):      #if the item is dict
                        if findValues(key,item):
                            list1 += findValues(key,item)    #then again recursively call the findValues
    return list1


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html", {})

def center_view(request, *args, **kwargs):
    connection = http.client.HTTPConnection('api.football-data.org')    #connection is established using the http client using the website from the football org
    headers = { 'X-Auth-Token': '98ef9787abd74ece820c938946cbf765' }    #using the API token and using the X-Auth security
    connection.request('GET', '/v2/competitions/PD/standings?season=2018', None, headers )   #requesting the current season standings from the LA LIGA
    response = json.loads(connection.getresponse().read().decode())   #json file format is stored in response file

    list1 =[]
    list1 =findValues('name',response)
    list1.pop(0)
    list1 = list1[:20]
    return render(request, "center.html",{
        "Team": list1
    })

def about_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "about.html", {})
