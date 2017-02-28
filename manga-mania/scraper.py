#!/usr/bin/python3

'''

    Manga-Mania
    ------------
    
    Author: Koushtav Chakrabarty <TheIllusionistMirage>
    Email:  koushtav at fleptic dot eu
    
    
    This code is licensed under the MIT license. Please see
    `LICENSE` file for more info.

'''

import shutil
import requests
from bs4 import BeautifulSoup

DEFAULT_TIMEOUT = 5

class Scraper:

    def __init__(self):
        
        foo = 1

        # set the default timeout to 5 seconds
        #self.DEFAULT_TIMEOUT = 5
        
        
    @staticmethod
    def search(site, url):
    
        if site == 'MangaFox':
        
            r = requests.get(url, timeout = DEFAULT_TIMEOUT)
            page = r.text
            
            bs = BeautifulSoup(page, 'lxml')
            
            results = bs.find_all('div', class_='manga_text')
            
            l = []
            for i in results:
                
                #print(i.find('a').get('href'))
                #print(i.find('a').text + '\n')
                l.append([i.find('a').get('href'), i.find('a').text])
            
            del r
            
            return l
    
    
    @staticmethod
    def fetchAllChapters(url):
    
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml')
        
        results = bs.find_all('a', class_='tips')
        
        m = [] # {}
        for i in results:
        
            #print(i.text, end=' ')
            #print(i['href'], end=' ')
            #m[i.text] = i.href
            m.insert(0, [i.text, i['href']])
            
        del r
        
        return m
        
    
    @staticmethod
    def fetchNextPageURL(url):
        # 'url' is the url of the current page
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml')
        
        results = bs.find('a', class_ = 'btn next_page')
        
        #print(results)
        
        #print('Next page URL: ' + str(results['href']))
        
        rs = url.split('/')
        rs.pop()
        
        #print(rs)
        
        suf = str(results['href'])
        
        if suf[-5:] != '.html':
        
            return ''
        
        nextURL = '/'.join(rs)
        nextURL = nextURL + '/' + str(results['href'])
        
        #print(nextURL)
        
        #return str(results['href'])
        return nextURL
            
    
    @staticmethod
    def fetchImage(url):
        
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml')
        
        results = bs.find_all('div', class_='read_img')
        
        #print(results)
        
        imageURL = results[0].find('img').get('src')
        print('Image URL: ' + imageURL)
        
        '''
        r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
        
        if r.status_code == 200:
            
            with open(path, 'wb') as f:
            
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        '''
        
        r = requests.get(imageURL, stream=True, timeout=5)
        with open('current.jpg', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        
        pg = bs.find('div', class_='r m')
        
        print(pg.text.split(' '))
        
        del r
        
        print('Saved current page image.')
        
        return True


# End of class `Scraper`
