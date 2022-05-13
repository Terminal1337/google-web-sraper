import pyfiglet,os
import requests,time,sys
import urllib
from colorama import Fore,init
from requests_html import HTML
from requests_html import HTMLSession
init(convert=True)



def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

print(Fore.LIGHTRED_EX+pyfiglet.figlet_format("GoogleScraper")+Fore.RESET)
os.system('title GoogleScraper [MainMenu-v1] - Support : Terminal#1337 - Discord : /cybersec')
search_term = input(Fore.LIGHTBLUE_EX+"Enter the Search Keyword [>] "+Fore.RESET)
print(Fore.GREEN+"Scraped Successfully \n"+Fore.RESET)
print(scrape_google(search_term))
save_in = input(Fore.LIGHTBLUE_EX+"Do you want to write the output to a output.txt? [Y/n] "+Fore.RESET)
if save_in == "Y":
    pass
    with open('output.txt','w') as f:
        f.write(str(scrape_google(search_term)))
        print(Fore.GREEN+"Scrapped data has been written to output.txt"+Fore.GREEN)
else:
    print(Fore.RED+"Thanks for using Consider staring the repo on github"+Fore.RESET)
    time.sleep(1)
    sys.exit()