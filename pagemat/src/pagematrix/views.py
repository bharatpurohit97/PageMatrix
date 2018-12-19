from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import pandas as pd
import csv

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def services(request):
	context = {}
	template = 'services.html'
	return render(request,template,context)

def learn(request):
    context = {}
    template = 'learn.html'
    return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)









 
#disabling csrf (cross site request forgery)
@login_required
@csrf_exempt
def index(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        post = Post()


        
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')

        post.save()

 
        #adding the values in a context variable 

        context = {
            'name': get_google_page_rank(name=name,email=email)
            
            
        }
        
        #getting our showdata template
        template = loader.get_template('home.html')
        
        #returing the template 
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('home.html')
        return HttpResponse(template.render())



def li_count(text):
    import re
    x =re.findall('<ul ([^ ].*?)</ul>',text)
    total = 0
    for line in x:
        finded = line.count('<li>')

        if finded != -1:
            total += finded
    return total

def usetor(name,email):
    from tbselenium.tbdriver import TorBrowserDriver
    #import selenium
    import time
    import numpy as np
    #from selenium import webdriver
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui import WebDriverWait
    #from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    #import timeit
    import re
    from time import sleep
    keywords = name.split(',')
    all_data = {}
    while keywords!=[]:
        try:
            with TorBrowserDriver("pagemat/tor-browser-linux64-7.5.6_en-US/tor-browser_en-US/") as driver:
                x = int(np.random.normal(110,10,1))
                google_search = 'https://www.google.co.in/search?num=' +str(x)
                driver.load_url(google_search, wait_for_page_body=True)
                while keywords!=[]:
                    for keyword in keywords:
                        #sleep(np.random.normal(2.00,0.500,1))
                        search = driver.find_element_by_name('q')
                        search.clear()
                        for char in keyword:
                            search.send_keys(char)
                            sleep(np.random.normal(0.7,0.05,1))
                        sleep(np.random.normal(0.6,0.02,1))
                        #search.send_keys(Keys.ENTER)
                        search.send_keys(Keys.RETURN)
                        sleep(np.random.normal(10,0.02,1))
                        #text =driver.find_element_by_tag_name("body").get_attribute('innerHTML')
                        text= driver.page_source
                        if re.findall('<ul ([^ ].*?)</ul>',text)[0] == 'recaptcha':
                            print (text)
                            continue
                        else:
                            all_data[keyword]=text
                            keywords.remove(keyword)
                            if keywords==[]:
                                return all_data        

                        
        except:
            pass

        
def processing_dataframe(all_data,df):
    import pandas as pd
    processsed_dataframe=pd.DataFrame(columns=['keyword','Rank','Link'])
    all_keys=list(all_data.keys())
    for key in all_keys:
        new_dataframe=df[df['keyword']==key]
        if len(new_dataframe)>1:
            new_dataframe=new_dataframe[new_dataframe['Rank']!='not in 100']
            #print(new_dataframe)
            processsed_dataframe = processsed_dataframe.append(new_dataframe)
        else:
            processsed_dataframe = processsed_dataframe.append(new_dataframe)
    return processsed_dataframe
        
def get_google_page_rank(name,email):
    import re

    import time


    import timeit
    import re
    from time import sleep
    import pandas as pd
    df = pd.DataFrame(columns=['keyword','Rank','Link'])
    all_data=usetor(name=name,email=email)
    #all_data = all_data
    all_data_1 = {}
    #all_list = []
    for key in all_data:
        list1 = re.findall('"r"><a href="([^ ].*?)\"',all_data[key])
        all_data_1[key]=list1
    for key in all_data_1:
        list1=all_data_1[key]
        print(key)
        if list1==[]:
            df = df.append({'keyword':key,'Rank':'NA','Link':'NA'},ignore_index=True)
            print('na')
        else:
            k=0
            for item in list1:
                if email in item:
                    df = df.append({'keyword':key,'Rank':k+1,'Link':item},ignore_index=True)
                    print('found')
                    k=k+1
                elif k==len(list1)-1:
                    df = df.append({'keyword':key,'Rank':'not in 100','Link':'NA'},ignore_index=True)
                    print('not in 100')
                
                else:
                    k=k+1
    processed_df = processing_dataframe(all_data=all_data,df = df)
    filename = str(email)+'.xls'
    print(filename)
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    processed_df.to_excel(writer)
    writer.save()
    output = "your task is completed,  Find files in  "+ str(filename)
    return output