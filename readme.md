## 使用方法
- 1.安装依赖库
```
pip install aliyun-python-sdk-core-v3
pip install aliyun-python-sdk-domain
pip install aliyun-python-sdk-alidns
pip install requests
```

- 2.执行certbot签发命令
```
#!/bin/bash
certbot certonly \
    -m email@126.com \
    -d *.example.com \
    -d example.com \
    --manual \
    --preferred-challenges dns \
    --config-dir /data/workspace/certbot \
    --work-dir /data/workspace/certbot \
    --cert-name github.icu \
    --non-interactive \
    --agree-tos \
    --preferred-challenges dns \
    --manual-auth-hook "/data/workspace/certbot/add.py" \
    --manual-cleanup-hook "/data/workspace/certbot/clean.py" \
    --force-renew
```

> 注意：命令中邮箱，域名和路径根据实际情况进行更改
