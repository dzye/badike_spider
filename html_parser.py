
#encoding:utf-8
import re
import urlparse
import pymongo
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        # client = pymongo.MongoClient('localhost', 27017)
        # db = client.test_db
        # new_urls = db['list']
        new_urls = []
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            # new_urls.insert({'url':new_full_url})
            new_urls.append(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        summary_node = soup.find('div',class_="lemma-summary")
        if(title_node.get_text().encode('utf8').find("足球俱乐部")!=-1):
            res_data = {}
            res_data['url'] = page_url
            res_data['title'] = title_node.get_text()
            res_data['summary'] = summary_node.get_text()
        return res_data

