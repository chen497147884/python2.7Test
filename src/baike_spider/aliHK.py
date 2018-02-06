# coding: utf-8
import requests
from aliyunsdkcore import client
from aliyunsdkjaq.request.v20161123 import AfsCheckRequest
from aliyunsdkcore.profile import region_provider
from app.libs.configure import config

region_provider.modify_point('Jaq', 'cn-hangzhou', 'jaq.aliyuncs.com')

clt = client.AcsClient(config.ALIYUN_OSS_ACCESS_KEY, config.ALIYUN_OSS_ACCESS_SECRET, 'cn-hangzhou')


def check_aliyun_captcha(session, sig, token, scene):
    request = AfsCheckRequest.AfsCheckRequest()
    # 必填参数：请求来源： 1：Android端； 2：iOS端； 3：PC端及其他
    request.set_Platform(3)
    request.set_Session(session)
    request.set_Sig(sig)
    request.set_Token(token)
    request.set_Scene(scene)
    result = clt.do_action_with_exception(request)
    print result