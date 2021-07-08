import os
import re
import random
import urllib.request
import urllib.error
import urllib.parse
from Crypto.Cipher import AES
import base64
import requests
import json
import time
from bs4 import BeautifulSoup
import traceback
import csv


agents = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {
    'Host':'music.163.com',
    'Origin':'https://music.163.com',
    'Referer':'https://music.163.com/song?id=28793052',
    'Cookie':'_ntes_nnid=fa21aa6f7fa91846484d1da0038b0136,1555152041426; _ntes_nuid=fa21aa6f7fa91846484d1da0038b0136; P_INFO=m13777828147_1@163.com|1555425055|0|mail163|00&99|zhj&1552921787&mail163#zhj&330100#10#0#0|137147&1||13777828147@163.com; nts_mail_user=13777828147@163.com:-1:1; NNSSPID=5ce8bcc65a504155a68ac478289da24a; mail_psc_fingerprint=0129f2a8a774dc4939675508ea68c9d2; usertrack=CrHucly15yJR8ps6AwlqAg==; _iuqxldmzr_=32; WM_NI=9b2qjWYZQsAexrkDZxlSoaMxvJM3fF4pF1yquvmCtfMPle4zqPUxH16BdP4H0%2Fyim25ECSa4wjqdJTpSqxPri4aqcf%2F1VziFCCwlcQYsl94ayqp44NJV3DCPGIJqE3y2UWs%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5d75293baa2b4f74faa868ea6d85e928a8baef36686b8fbd1ce39b4e99bb3fc2af0fea7c3b92afbbefe92e95d9b869f94c46fbcaea5a5d974b08da182d074b69683d4e54ef8b08ad2fc7bb7aaa3a4f76e8f90a486b772b3909b99cb3bf69eacb1b744f4f1b78af03af79b8db4e440b5b6bf85c960b48dbf99d37aabecaf92e26eedef9a9bec4e819db98de25b9bada4dab76bbbafc0d5b7468a8afda5c25c85978692c839bbee9bb8f237e2a3; WM_TID=XsyButsmj6ZERQRFVVIsyEkpge2t6VRj; __remember_me=true; JSESSIONID-WYYY=c53%2B53zBc7ouAGhtFt9qOp8ANNZne92S1d%2BrlSMdGjnpF%2B2Qn5ARymQH6reEZ3cqgVUj%2B3kBHwJ99TfRZQCx8g3UOEryg3c%2FijbG%5C%2BXa9kJ%2FigaxB0XsUDDYUS%2FA4k3bgOZmq2z7Yr1BO2T0kRHtEoQ8BiVojcbHNDzY%5Cf%5C02lpM%2FbgM%3A1555484616734; MUSIC_U=acf6800242386c13cb493646528f61bdc9d5d8560748596cea98c6875c2135cc8708d177bc2dbca6dc8f640ef351e1f131b299d667364ed3; __csrf=2be18a45ab2aaa5ad48e08c34b16ad47',
    'User-Agent':''.join(random.sample(agents, 1))
}

# 除了第一个参数，其他参数为固定参数，可以直接套用
# offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
# 第一个参数
# first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
# 第二个参数
second_param = "010001"
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# 第四个参数
forth_param = "0CoJUm6Qyw8W8jud"


# 获取参数
def get_params(page):  # page为传入页数
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    if(page == 1):  # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)
    else:
        offset = str((page-1)*20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset,'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


# 获取 encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


# 解密过程
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(encrypt_text, encoding="utf-8")  # 注意一定要加上这一句，没有这一句则出现错误
    return encrypt_text


# 获得评论json数据
def get_json(url, params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content.decode('utf-8')  # 解码




# 抓取某一首歌的前page页评论
def get_all_comments(song_id):  # hot_song_order为了给文件命名添加一个编号
    urls = 'https://music.163.com/song?id=' + song_id
    r = requests.get(urls, timeout=30, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    if title.text.split()[0] == '网易云音乐':
        return ''
    song_name = title.text.split()[0]
    song_singer = title.text.split()[2]

    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(song_id) + '?csrf_token='   # 歌评url

    params = get_params(1)
    encSecKey = get_encSecKey()
    json_text = get_json(url, params, encSecKey)
    # print(json_text)

    json_dict = json.loads(json_text)
    song_cem_num = json_dict["total"]  # 热评总数
    print("{},{},{}".format(song_name, song_singer, song_cem_num))
    try:
        writer.writerow((song_name, song_singer, song_cem_num))
    except Exception as msg:
        print(msg)

ls1 = []
#读取专辑id和名字
fo = open("/home/ymc/Documents/Python project/网易云音乐爬虫及过程文件/requests实现/music_163_songs.csv", "r", encoding='utf-8')
for line in fo:
    line = line.replace("\n", "")
    line_s = line.split(',')
    if line_s[0] != '':
        ls1.append(line_s[0]) #把专辑id存入ls1
fo.close()
lent = len(ls1)
count = 59136
ls = ls1[count:]
csvfile = open('/home/ymc/Documents/Python project/网易云音乐爬虫及过程文件/requests实现/music_163_songs_hot.csv', 'a', encoding='utf-8')    # 文件存储的位置
writer = csv.writer(csvfile)
for i in ls:
    count = count + 1
    a = count / lent *100
    print("count = {}/{}--{:.3f}%".format(count, lent, a))
    if i != "":
        song_id = str(i)
        get_all_comments(song_id)



