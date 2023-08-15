#!/usr/bin/python3
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
import requests
from urllib.request import urlopen
import json
import sys
import os

accessKeyId = "accesskeyid"  # 账户的accessKeyId
accessSecret = "accesssecret"  # 账户的accessSecret
domain = os.getenv('CERTBOT_DOMAIN')  # 主域名
sub_domain = "_acme-challenge"  # 要进行解析的子域名
value = os.getenv('CERTBOT_VALIDATION') # 解析值，如ip地址，域名，与解析类型有关
type = "TXT" # 解析类型，如A，CNAME

client = AcsClient(accessKeyId, accessSecret, 'cn-shanghai')
request = DescribeSubDomainRecordsRequest()
request.set_accept_format('json')
request.set_DomainName(domain)
request.set_SubDomain(sub_domain + '.' + domain)
request.set_Type(type)
response = client.do_action_with_exception(request)  # 获取域名解析记录列表
domain_list = json.loads(response)  # 将返回的JSON数据转化为Python能识别的


def delete(RecordId):  # 删除域名解析记录
    from aliyunsdkalidns.request.v20150109.DeleteDomainRecordRequest import DeleteDomainRecordRequest
    request = DeleteDomainRecordRequest()
    request.set_accept_format('json')
    request.set_RecordId(RecordId)
    response = client.do_action_with_exception(request)


for i in range(len(domain_list['DomainRecords']['Record'])):
    delete(domain_list['DomainRecords']['Record'][i]['RecordId'])
print("删除域名解析"+sub_domain+"."+domain+"成功")
