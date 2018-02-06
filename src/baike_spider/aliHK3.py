import random
from urllib import quote
from hashlib import sha1
import hmac
import requests
from base64 import b64encode
import datetime

def utcnow_isostr():
    dt = datetime.datetime.utcnow()
    return datetime.datetime.strftime(dt, '%Y-%m-%dT%H:%M:%SZ')

def quote_ali(element):
    return quote(str(element)).replace('+', '20%').replace('*', '2A%').replace('%7E', '~')

def build_afs_check_request(session, sig, token, scene):
    m = dict()
    m['Action'] = 'AfsCheck'
    m['Format'] = 'JSON'
    m['Version'] = '2016-11-23'
    m['AccessKeyId'] = config.ALIYUN_OSS_ACCESS_KEY
    m['SignatureMethod'] = 'HMAC-SHA1'
    m['Timestamp'] = utcnow_isostr()
    m['SignatureVersion'] = '1.0'
    m['SignatureNonce'] = str(int(random.random()*1000000))
    m['token'] = token
    m['sig'] = sig
    m['session'] = session
    m['scene'] = scene
    m['platform'] = 3
    ks = m.keys()
    ks.sort()
    query_list = list()
    for k in ks:
        query_list.append(k + '=' + quote_ali(m[k]))
    string_to_sign = 'GET&%2F&' + '&'.join(query_list)
    print string_to_sign
    base_query_string = '&'.join(query_list)
    hashed = hmac.new(config.ALIYUN_OSS_ACCESS_SECRET + '&', string_to_sign, sha1)
    signature = b64encode(hashed.digest())
    print signature
    url = 'http://jaq.aliyuncs.com/?{}&Signature={}'.format(base_query_string, quote_ali(signature))
    print url
    return url

def custom_check_aliyun_captcha(session, sig, token, scene):
    url = build_afs_check_request(session, sig, token, scene)
    resp = requests.get(url)
    print resp.content