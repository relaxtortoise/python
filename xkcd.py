#python3
import requests,os,bs4
url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok = True)
while not url.endswith('#'):
    print("下载网页%s..."%url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("无法找到图片")
    else:
        comicUrl = comicElem[0].get('src')
        print('下载图片%s'%comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')
print('已完成。')