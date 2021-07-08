import requests
from bs4 import BeautifulSoup
import csv


# 构造函数获取歌手信息
def get_artists(url):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Connection': 'keep-alive',
             'Cookie':'_ntes_nnid=fa21aa6f7fa91846484d1da0038b0136,1555152041426; _ntes_nuid=fa21aa6f7fa91846484d1da0038b0136; P_INFO=m13777828147_1@163.com|1555425055|0|mail163|00&99|zhj&1552921787&mail163#zhj&330100#10#0#0|137147&1||13777828147@163.com; nts_mail_user=13777828147@163.com:-1:1; NNSSPID=5ce8bcc65a504155a68ac478289da24a; mail_psc_fingerprint=0129f2a8a774dc4939675508ea68c9d2; usertrack=CrHucly15yJR8ps6AwlqAg==; _iuqxldmzr_=32; WM_NI=9b2qjWYZQsAexrkDZxlSoaMxvJM3fF4pF1yquvmCtfMPle4zqPUxH16BdP4H0%2Fyim25ECSa4wjqdJTpSqxPri4aqcf%2F1VziFCCwlcQYsl94ayqp44NJV3DCPGIJqE3y2UWs%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5d75293baa2b4f74faa868ea6d85e928a8baef36686b8fbd1ce39b4e99bb3fc2af0fea7c3b92afbbefe92e95d9b869f94c46fbcaea5a5d974b08da182d074b69683d4e54ef8b08ad2fc7bb7aaa3a4f76e8f90a486b772b3909b99cb3bf69eacb1b744f4f1b78af03af79b8db4e440b5b6bf85c960b48dbf99d37aabecaf92e26eedef9a9bec4e819db98de25b9bada4dab76bbbafc0d5b7468a8afda5c25c85978692c839bbee9bb8f237e2a3; WM_TID=XsyButsmj6ZERQRFVVIsyEkpge2t6VRj; __remember_me=true; JSESSIONID-WYYY=c53%2B53zBc7ouAGhtFt9qOp8ANNZne92S1d%2BrlSMdGjnpF%2B2Qn5ARymQH6reEZ3cqgVUj%2B3kBHwJ99TfRZQCx8g3UOEryg3c%2FijbG%5C%2BXa9kJ%2FigaxB0XsUDDYUS%2FA4k3bgOZmq2z7Yr1BO2T0kRHtEoQ8BiVojcbHNDzY%5Cf%5C02lpM%2FbgM%3A1555484616734; MUSIC_U=acf6800242386c13cb493646528f61bdc9d5d8560748596cea98c6875c2135cc8708d177bc2dbca6dc8f640ef351e1f131b299d667364ed3; __csrf=2be18a45ab2aaa5ad48e08c34b16ad47',
             'Host': 'music.163.com',
             'Referer': 'http://music.163.com/',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    for artist in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        artist_name = artist.string
        print(artist.string)
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        try:
            writer.writerow((artist_id, artist_name))
        except Exception as msg:
            print(msg)


ls1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]    # id的值
ls2 = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]    # initial的值
csvfile = open('/home/ymc/Documents/Python project/网易云音乐爬虫及过程文件/requests实现/music_163_artists.csv', 'a', encoding='utf-8')    # 文件存储的位置
writer = csv.writer(csvfile)
for i in ls1:
    for j in ls2:
        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        get_artists(url)
