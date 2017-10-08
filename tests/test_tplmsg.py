# -*- coding: utf-8 -*-

from local_wecfg_example import OPENID, TEMPLATEDATA, TEMPLATEIDSHORT, WECHAT
from pywe_template_message import (TemplateMessage, add_template, del_private_template, get_all_private_template,
                                   get_industry, send_template_message, set_industry)


class TestTplmsgCommands(object):

    def test_set_industry(self):
        """
        {u'errcode': 0, u'errmsg': u'ok'}
        {u'errcode': 43100, u'errmsg': u'change template too frequently hint: [byn8Va0476vr25]'}
        """
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        tplmsg = TemplateMessage(appid=appid, secret=appsecret)
        industry1 = tplmsg.set_industry(3, 31)
        assert isinstance(industry1, dict)
        assert industry1['errcode'] in [0, 43100]

        industry2 = set_industry(3, 31, appid=appid, secret=appsecret)
        assert isinstance(industry2, dict)
        assert industry2['errcode'] in [0, 43100]

    def test_get_industry(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        tplmsg = TemplateMessage(appid=appid, secret=appsecret)
        industry1 = tplmsg.get_industry()
        assert isinstance(industry1, dict)
        assert isinstance(industry1['primary_industry'], dict)
        assert isinstance(industry1['secondary_industry'], dict)

        industry2 = get_industry(appid=appid, secret=appsecret)
        assert isinstance(industry2, dict)
        assert isinstance(industry2['primary_industry'], dict)
        assert isinstance(industry2['secondary_industry'], dict)

        assert industry1 == industry2

    def test_add_template(self):
        """ {u'errcode': 0, u'errmsg': u'ok', u'template_id': u'JEFAYuLxonU8skfH_Uk_G7-eLrjRgCFhF3B4WxLJjIk'} """
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        tplmsg = TemplateMessage(appid=appid, secret=appsecret)
        template1 = tplmsg.add_template(template_id_short=TEMPLATEIDSHORT)
        assert isinstance(template1, dict)
        assert template1['errcode'] == 0
        assert template1['errmsg'] == 'ok'

        template2 = add_template(template_id_short=TEMPLATEIDSHORT, appid=appid, secret=appsecret)
        assert isinstance(template2, dict)
        assert template2['errcode'] == 0
        assert template2['errmsg'] == 'ok'

        # {u'errcode': 0, u'errmsg': u'ok'}
        template3 = tplmsg.del_private_template(template_id=template1['template_id'])
        assert isinstance(template3, dict)
        assert template3['errcode'] == 0
        assert template3['errmsg'] == 'ok'

        template4 = del_private_template(template_id=template2['template_id'], appid=appid, secret=appsecret)
        assert isinstance(template4, dict)
        assert template4['errcode'] == 0
        assert template4['errmsg'] == 'ok'

    def test_get_all_private_template(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        tplmsg = TemplateMessage(appid=appid, secret=appsecret)
        all_private_template1 = tplmsg.get_all_private_template()
        assert isinstance(all_private_template1, dict)
        assert isinstance(all_private_template1['template_list'], list)

        all_private_template2 = get_all_private_template(appid=appid, secret=appsecret)
        assert isinstance(all_private_template2, dict)
        assert isinstance(all_private_template2['template_list'], list)

        assert all_private_template1 == all_private_template2

    def test_send_template_message(self):
        """ {u'errcode': 0, u'errmsg': u'ok', u'msgid': 425077957} """
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        template = add_template(template_id_short=TEMPLATEIDSHORT, appid=appid, secret=appsecret)
        template_id = template['template_id']

        tplmsg = TemplateMessage(appid=appid, secret=appsecret)
        msg1 = tplmsg.send_template_message(user_id=OPENID, template_id=template_id, data=TEMPLATEDATA)
        assert isinstance(msg1, dict)
        assert msg1['errcode'] == 0
        assert msg1['errmsg'] == 'ok'

        msg2 = send_template_message(user_id=OPENID, template_id=template_id, data=TEMPLATEDATA, appid=appid, secret=appsecret)
        assert msg2['errcode'] == 0
        assert msg2['errmsg'] == 'ok'

        del_private_template(template_id=template_id, appid=appid, secret=appsecret)
