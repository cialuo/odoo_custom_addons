import werkzeug
import json
import requests
from odoo import http, api
from odoo.modules.registry import Registry
from odoo import SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class WechatMiniProgram(http.Controller):

    @http.route('/web/transfer', type='http', auth="none", sitemap=False)
    def get_wechat_openid(self,target_url, request_paramters):
        result = {}
        result['is_success'] = True
        web_target_url = '%s%s' % ('https://wuzffalu.cn.flextronics.com/flexpsappapi/api/', target_url)
        try:
            request_paramters = json.loads(request_paramters)
            request_paramters = werkzeug.url_encode(request_paramters)
            request_result = requests.get(web_target_url, params=request_paramters).json()
            result['data'] = request_result
        except:
            result['is_success'] = False
            pass
        result = json.dumps(result)
        return result


    @http.route('/web/gettoken', type='http', auth="none", sitemap=False)
    def get_openid(self, code, db_name):
        result = {}
        result['is_success'] = True
        cr = Registry(db_name).cursor()
        env = api.Environment(cr, SUPERUSER_ID,{})
        is_success, token = env['wechat.mini.program.session'].get_token(code)
        result['token'] = token
        result['is_get_token'] = is_success
        cr.commit()
        cr.close()
        return json.dumps(result)

    @http.route('/web/create_user',type='http',auth="none", sitemap=False)
    def create_user(self, login_name, help_id, db_name):
        result = {}
        result['is_success'] = True
        registry = Registry(db_name)
        cr = registry.cursor()
        env = api.Environment(cr, SUPERUSER_ID, {})
        user_id = env['res.users'].create_wechat_mini_user(login_name, help_id)
        result['user_id'] = user_id
        cr.commit()
        cr.close()
        return json.dumps(result)

