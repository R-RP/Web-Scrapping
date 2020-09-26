import requests
from bs4 import BeautifulSoup
import pprint



def hacker_news(link,subtext):
    final = []
    for i in range(len(link)):#length of the link and votes will be diff. if there is no votes in some articles. It will lead to index error 
        vote = subtext[i].select('.score')#'.select' always returns list even if there is no item so to access it always use index.  
        if len(vote): #to make sure we don't try to fetch data when there is no votes or else we will have mismatch in links and votes finally it causes index errors
            points = int(vote[0].text.split(' ')[0])
            if points > 100:
                title =  link[i].text # you can also use .getText()
                href = link[i].get('href')
                final.append({'Title':title,'Link':href,'Votes':points})
    final =  sorted(final,key= lambda i: i['Votes'],reverse=True)
    return final
while True:
    page = input('How many pages do you want to Scrap from HACKER NEWS: ')
    try:
        int(page)
        break    
    except:
        print('please enter an integer')
i = 1
final_link = []
final_subtext = []
while i<=int(page): 
    res = requests.get('https://news.ycombinator.com/news?p='+ str(i))
    soup = BeautifulSoup(res.text,'html.parser')
    link = soup.select('.storylink')
    subtext = soup.select('.subtext')
    final_link = final_link + link   
    
    final_subtext = final_subtext + subtext
    i += 1
pprint.pprint(hacker_news(final_link,final_subtext))


'''
while i<=page 
res = requests.get('https://news.ycombinator.com/news?p='+i)
soup = BeautifulSoup(res.text,'html.parser')
link = soup.select('.storylink')
subtext = soup.select('.subtext')
pprint.pprint(hacker_news(link,subtext))
'''