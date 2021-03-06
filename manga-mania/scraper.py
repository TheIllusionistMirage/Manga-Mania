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


# Set the default timeout to 5s
DEFAULT_TIMEOUT = 5

class Scraper:

    @staticmethod
    def search(site, url):
    
        '''        
        Method:
            
            Scraper.search
        
        Args:
        
            url - The search URL with all search parameters
        
        Description:
        
            This method performs a search on the MangaFox database
            about a manga based on the search parameters provided
            during the search.
        
        Returns:
        
            mangaList -
            
                A list of pairs of the for [result label: result URL]
        '''
    
        # Fetch the HTML code of the page containing the search results
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        
        # If GET operation fails, method returns immediately
        if r.status_code != 200:
        
            print('[ERROR] GET request failed while trying to fetch page image')
            return []
        
        page = r.text
        
        # BeautifulSoup4 object parses the HTMl code using lxml to make
        # scraping easier
        bs = BeautifulSoup(page, 'lxml')
                
        # The results in the search page are stored in `div`s which have
        # the class `manga_text`. All such ocurrences are stoed in `results`
        results = bs.find_all('div', class_='manga_text')
        
        # The final step is to create a list that maps the manga
        # name to their URLs, which is stored in `mangaList`.
        
        mangaList = []
        
        for i in results:
            
            mangaList.append([i.find('a').text, i.find('a').get('href')])
        
        del r
        del bs
        
        return mangaList
    
    
    @staticmethod
    def fetchAllChapters(url):
    
        '''        
        Method:
            
            Scraper.fetchChapters
        
        Args:
        
            url - The URL of the manga
        
        Description:
        
            This method scrapes the manga's page for all
            chapters in the manga.
        
        Returns:
        
            chapterList -
            
                A list containing the Chapter name (or
                number) and the URL
        '''
    
        # Fetch the HTML code of the page containing the chapters
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        
        # If GET operation fails, method returns immediately
        if r.status_code != 200:
        
            print('[ERROR] GET request failed while trying to fetch page image')
            return []
        
        page = r.text
        
        # BeautifulSoup4 object parses the HTMl code using lxml to make
        # scraping easier
        bs = BeautifulSoup(page, 'lxml')
        
        # The chapters in the manga are stored in `a`s which have
        # the class `tips`. All such ocurrences are stoed in `results`
        results = bs.find_all('a', class_='tips')
        
        # The final step is to create a list that maps the
        # chapters to their URLs, which is stored in `chapterList`.
               
        chapterList = []
        
        for i in results:
        
            chapterList.insert(0, [i.text, i['href']])
            
        del r
        del bs
        
        return chapterList
    
    
    @staticmethod
    def fetchChapterInfo(url):
    
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        
        if r.status_code != 200:
        
            print('[ERROR] GET request failed while trying to fetch page image')
            return 0
        
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml')
        
        result = bs.find('div', class_='l')
        
        #print(result.text.split('\t\t\t'))
        foo = result.text.split('\t\t\t')
        bar = foo[3]
        foo2 = bar.split('\tof ')
        #print(foo2[1])
        return int(foo2[1])
        #print(bar.split('\tof '))
        #print(result.text.split('\t\t\t '))
    
       
    @staticmethod
    def fetchPageImage(url):
    
        '''        
        Method:
            
            Scraper.fetchPageImage
        
        Args:
        
            url - The URL of the page being read currently
        
        Description:
        
            This method scrapes the page being read for
            the page image
        
        Returns:
        
            True  - If the page's image was successfully saved
        '''
        
        # Fetch the HTML code of the page containing the page image
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        
        # If GET operation fails, method returns immediately
        if r.status_code != 200:
        
            print('[ERROR] GET request failed while trying to fetch page image URL')
            return False
        
        page = r.text
        
        # BeautifulSoup4 object parses the HTMl code using lxml to make
        # scraping easier
        bs = BeautifulSoup(page, 'lxml')
        
        # Find the image's permalink which is present in a `div` of the
        # class `read_img`
        result = bs.find('div', class_='read_img')
        imageURL = result.find('img').get('src')
        
        print('Page image URL: ' + imageURL)
        
        # Fetch the image in blocks and save it to a file called
        # `current.jpg`
        r = requests.get(imageURL, stream=True, timeout=DEFAULT_TIMEOUT)
        
        # If GET operation fails, method returns immediately
        if r.status_code != 200:
        
            print('[ERROR] GET request failed while trying to fetch page image')
            return False
            
        # Save the image, one `chunk` at a time
        with open('current.jpg', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
                
        del r
        del bs
        
        print('Saved current page image.')
        
        return True


# End of class `Scraper`

'''
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
    def fetchPreviousPageURL(url):
        
        # 'url' is the url of the current page
        r = requests.get(url, timeout = DEFAULT_TIMEOUT)
        page = r.text
        
        bs = BeautifulSoup(page, 'lxml')
        
        results = bs.find('a', class_ = 'btn prev_page')
        
        #print(results)
        
        #print('Next page URL: ' + str(results['href']))
        
        rs = url.split('/')
        rs.pop()
        
        #print(rs)
        
        suf = str(results['href'])
        
        if suf[-5:] != '.html':
        
            return ''
        
        prevURL = '/'.join(rs)
        prevURL = prevURL + '/' + str(results['href'])
        
        #print(nextURL)
        
        #return str(results['href'])
        return prevURL
'''
