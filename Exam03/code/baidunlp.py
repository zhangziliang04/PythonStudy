#-*- coding:utf-8 -*-
import urllib
import urllib.parse
import urllib.request
import json
def get_access_token():
    """
    获取百度AI平台的Access Token
    """
    #Appid = 15149435
    #API Key = XI2BoOo7vWVlEVgQLvhKicPI
    #Secret Key = j74PyrpFypliNfgFaFEVAPzDmKFqABwv
    #host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[]&client_secret=[Secret Key]'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XI2BoOo7vWVlEVgQLvhKicPI&client_secret=j74PyrpFypliNfgFaFEVAPzDmKFqABwv'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    rdata = json.loads(content)
    return rdata['access_token']
# 24.ff0dd7d51549eca03c13828db73bd146.2592000.1547276608.282335-15149435
def sentiment_classify(text):
    """
    获取文本的感情偏向（消极 or 积极 or 中立）
    参数：
    text:str 本文
    """
    raw = {"text":"内容"}
    raw['text'] = text
    data = json.dumps(raw).encode('utf-8')
    #AT = "24.ff0dd7d51549eca03c13828db73bd146.2592000.1547276608.282335-15149435"
    AT = "24.f1c248c9887837ab6ffa8ebc19b197a9.2592000.1562928906.282335-15149435"
    host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token="+AT
    request = urllib.request.Request(url=host,data=data)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    rdata = json.loads(content)
    return rdata

if __name__ == "__main__":
    #print("acces-token:")
    #print(get_access_token())

    text = "Axela昂克赛拉 发动机故障灯亮，去了4S店三次仍然未解决"
    print(sentiment_classify(text)['text'])
    print(sentiment_classify(text)['items'])
    print("正向情感概率：")
    print(sentiment_classify(text)['items'][0]['positive_prob'])
    print("负向情感概率：")
    print(sentiment_classify(text)['items'][0]['negative_prob'])
    print("置信度：")
    print(sentiment_classify(text)['items'][0]['confidence'])
