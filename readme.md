## 说明
该项目源自：[python-alidns][1]

## 使用方法
- 1.安装依赖库
```
pip install aliyun-python-sdk-core-v3
pip install aliyun-python-sdk-domain
pip install aliyun-python-sdk-alidns
pip install requests
```

- 2.变量替换
```
accesskeyid  # 阿里云账户的accessKeyId
accesssecret  # 阿里云账户的accessSecret
```

- 3.执行certbot签发命令
```
#!/bin/bash
certbot certonly \
    -m your-email@example.com \
    -d *.example.com \
    -d example.com \
    --manual \
    --preferred-challenges dns \
    --config-dir /path/to/certbot \
    --work-dir /path/to/certbot \
    --cert-name example.com \
    --non-interactive \
    --agree-tos \
    --preferred-challenges dns \
    --manual-auth-hook /path/to/add.py \
    --manual-cleanup-hook /path/to/clean.py \
    --force-renew
```

参数解释：
|名称|含义|
|-|-|
|`your-email@example.com`|自己的邮箱，可以收到Let's Encrypt的邮件|
|`example.com`|需要签发证书的二级域名，若想签发多个通配符证书，可以跟多个`-d`|
|`/path/to/certbot`|证书生成的路径|
|`/path/to/add.py`|自动添加dns解析的脚本|
|`/path/to/clean.py`|自动删除dns解析的脚本|

> 注意：命令中邮箱，域名和路径根据实际情况进行更改，详细参数解释请参看:[如何自签发免费通配符域名证书并实现自动化----Let's Encrypt][2]

## Q&A
- 1. Q：`CERTBOT_DOMAIN`和`CERTBOT_VALIDATION`这两个变量如何传入certbot
A：这两个变量是certbot在执行过程中生成的，`CERTBOT_DOMAIN`即为通配符域名，`CERTBOT_VALIDATION`即为TXT解析的记录值，是certbot随机生成的，这两个变量必须在hook脚本中获取，如果是在certbot命令外部通过传参方式传入hook脚本，是获取不到的，比如`--manual-auth-hook "/path/to/add.py ${CERTBOT_DOMAIN} ${CERTBOT_VALIDATION}"`


[1]: https://github.com/leif160519/python-alidns
[2]: https://github.icu/articles/2023/06/10/1686364528354.html#toc_h1_1
