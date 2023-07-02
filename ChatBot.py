from datetime import datetime as dt
import os
import glob
import random
import bs4
import urllib.request as url
import json

chat = True

greetIntent = ['hi', 'hello', 'hey', 'good morning', 'hey there']
dateIntent = ['date', 'tell me date', 'please tell me date']
timeIntent = ['time', 'tell me time', 'please tell me time']
musicIntent = ['play music', 'play song', 'music','song', 'please play a song', 'please play music']
productIntent = ['shop', 'buy']
newsIntent = ['news', 'tell me news', 'what is the news', 'news updates']

while chat:
    msg = input("Enter your message:").lower()
    
    if msg in greetIntent:
        print("Hello User")
    
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is ;", date.strftime("%d %B, %Y, %a"))
    
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is ;", time.strftime("%H:%M:%S %p"))

    elif msg in musicIntent:
        os.chdir(path=r"C:\Users\rajsh\Desktop\Python IoT Training Projects\ChatBot\Music")
        os.getcwd()
        songs=glob.glob('*mp3')
        random_song = random.choice(songs)
        os.startfile(random_song)

    elif msg in productIntent:
        product=input("Enter product name:")
        product=product.replace(" ","+").lower()
        for k in range(1,3):
            path=f"https://www.flipkart.com/search?q={product}&page={k}"
            response=url.urlopen(path)
            page=bs4.BeautifulSoup(response,"lxml")
            titleList=page.find_all('div',{'class':'_4rR01T'})
            priceList=page.find_all('div',{'class':'_30jeq3 _1_WHN1'})
            for i in range(len(titleList)):
                print(titleList[i].text)
                print(priceList[i].text)
                print("*" * 30)

    elif msg in newsIntent:
        print(f'''
        1. Politics
        2. Sports
        3. Entertainment
        4. Health''')
        category=input("Enter your category: ")
        path=f"https://newsapi.org/v2/top-headlines?country=in&category={msg}&apiKey=b44cbf630d8442e5bdfda63eae3e3e72"
        response=url.urlopen(path)
        data=json.load(response)
        articles=data['articles']
        for i in range(len(articles)):
            print(articles[i]['title'])
            print('*'*50)

    elif msg=="bye":
        print("Bye User")
        chat=False
    
    else:
        print("I didn't understand your message.")
