import sys
import json
import requests
import configparser
import argparse


CONFIG_FILE = 'config.conf'



def init_config():
    config = {"TIMEOUT":5,
"URL_WECHAT_GET_TOKEN":'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}',
"URL_WECHAT_MESSAGE": 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}',
'WECHAT_CORPID':'',
'WECHAT_SECRET':'',
'AGENT_ID':''}
    conf = configparser.ConfigParser()
    conf['config'] = config
    with open(CONFIG_FILE,'w+') as f:
        conf.write(f)
    print('create config file,run again ')
    exit(0)

def LoadConfig():
    try:
        conf = configparser.ConfigParser()
        conf.read(CONFIG_FILE)
        config1 = conf._sections['config']
        config= {}
        for key in config1:config[key.upper()] = config1[key]
        globals().update(config)
        print('load config file')
    except Exception as e:
        # print(e)
        init_config()


# def LoadConfig(config_file = CONFIG_FILE):
#     pass

def Req(url,method='get',payload=None):
    if method == 'get':
        try:
            req = requests.get(url,timeout=int(TIMEOUT))
            return req
        except Exception as  e:
            print(e)
            return False
    else:
        try:
            print(payload)
            req = requests.post(url,payload,timeout=int(TIMEOUT))
            return req
        except Exception as e:
            print(e)
            return False


def GetWechatKey():
    url = URL_WECHAT_GET_TOKEN.format(corpid = WECHAT_CORPID,corpsecret = WECHAT_SECRET)
    print(url)
    try:
        result = Req(url).json()
        print(result)
        if result['errcode'] == 0: 
            key = result['access_token']
            return key
        else:
            print('get wechat token error')
            return False
    except Exception as e:
        print(e)
        return False


def PushWechatMessage(to_user,text_content,token):

    body = {
   "touser" : "",
   "toparty" : "",
   "totag" : "",
   "msgtype" : "text",
   "agentid" : int(AGENT_ID),
   "text" : {
       "content" : ""
   },
   "safe":0,
   "enable_id_trans": 0,
   "enable_duplicate_check": 0
}

    body['touser'] = to_user
    body['text']['content'] = text_content
    try:
        result = Req(URL_WECHAT_MESSAGE.format(token = token),'post',json.dumps(body)).json()
        # print(result)
        print('[+] message push sucessful')
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    LoadConfig()
    # print(globals())
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--user',dest='username',type=str,help='to user')
    parser.add_argument(dest='message',type=str,help='to user message')
    # parser.add_argument('-t','--token',dest='token',type=str,help='to user message')
    options = parser.parse_args()
    # token = GetWechatKey()
    PushWechatMessage(options.username,options.message,GetWechatKey())