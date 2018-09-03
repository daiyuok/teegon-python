# __author__ = 'daixinyu'
# coding=utf8
import unittest
import sys
import time
import simplejson

sys.path.append("../")
reload(sys)
sys.setdefaultencoding('utf-8')

from com.shopex.teegon.TeegonClient import TeegonClient


class TeegonClientTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "http://api.teegon.com/router"
        # self.url = "http://127.0.0.1:3000/hiproxy"
        self.key = "XX"
        self.secret = "XX"

        self.teegonClient = TeegonClient(self.url, self.key, self.secret)

    def testDoPost(self):
        params = sys_params()
        params['method'] = "store.apigateway.request"
        params['node_id'] = "1876146934"
        params['api_method'] = "jingdong.pop.PopCommentJsfService.getVenderCommentsForJos"
        params['params'] = '{"page": "1", "pageSize": "10"}'
        response = self.teegonClient.do_post(params)
        print response


def sys_params():
    params = {

    }
    return params


if __name__ == '__main__':
    unittest.main()
