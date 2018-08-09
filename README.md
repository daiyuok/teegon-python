ShopEx Teegon sdk (python version)
===============================================

用途
-----------------------------------------------

实现ShopEx Teegon 的Python版SDK供第三方使用


功能
-----------------------------------------------

    提供http API调用（GET/POST方式）

要求
-----------------------------------------------

python sdk 2.6或者以上更高的版本


打包、安装、日志
-----------------------------------------------


1、打包

    git clone https://github.com/daiyuok/teegon-python

    cd teegon-python/

    python setup.py sdist  #构建Teegon SDK完成，构建SDK位于.dist目录中
    
    ps:版本号只需 com.version.py 中version=XXX修改即可

2、安装

    tar -zxvf teegon-python-0.1.tar.gz

    cd teegon-python-0.1

    python setup.py install  #Teegon SDK完成
    
3、日志
   
   日志级别的修改com.shopex.config.py 讲LOG_LEVEL改成对应的ERROR、WARNING、INFO、DEBUG  

使用方法
-----------------------------------------------


###1、提供HTTP API调用(GET/POST)(参考如下TestCase代码)

ps:
```
import unittest

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

```

返回是一串json格式的response消息体






