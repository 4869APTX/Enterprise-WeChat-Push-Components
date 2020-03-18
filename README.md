# Enterprise-WeChat-Push-Components
Enterprise WeChat Push Components by python

## 这是啥
小用处大轮子白给系列，初步完成企业微信应用的消息推动模块。

## how to use
```
python3 wx-push.py -u username "message" 
usage: wx-push.py [-h] [-u USERNAME] message
```
初次使用会自动生成`config.conf`文件,需要在`config.conf`中填写企业微信corpid及secret id,再次发送即可。

- `config.conf`文件格式
    ```
    [config]
    timeout = 5
    url_wechat_get_token = https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}
    url_wechat_message = https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}
    wechat_corpid = 
    wechat_secret = 
    agent_id = 
    ```


