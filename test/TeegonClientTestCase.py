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
        self.key = "xx"
        self.secret = "xx"

        self.teegonClient = TeegonClient(self.url, self.key, self.secret)

    def testDoPost(self):
        params = sys_params()
        params['method'] = "shopex.queue.read"
        params['topic'] = "orders"
        params['drop'] = "false"
        params['num'] = "1"
        response = self.teegonClient.do_post(params)
        print response


def sys_params():
    params = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'format': 'json',
    }
    return params


if __name__ == '__main__':
    unittest.main()
