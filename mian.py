#coding: UTF-8
import web
import os, sys

# 初始化模板系统
render = web.template.render('templates/')

'''
# 设置模板路径(部分软件会以软件安装目录为运行目录,就会导致web.py找不到指定目录)
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root, 'templates/'))
'''

'''
# 拼接路径时可用os.path.join，会根据当前系统选择合适拼接方式
# 例如os.path.join(“home”, "me", "mywork")
# Linux上返回home/me/mywork
# Windows上返回home\me\mywork
root = os.path.dirname(__file__)
static_dir = os.path.join(root, 'static','')
'''

# 设置当前工作目录
os.chdir(sys.path[0])

# urls表示可访问的链接(URL路由表)，两个元素一组分别为url和处理类
urls = (
    '/', 'index',
    '/test/(.*)', 'test',
)

# url处理类，负责处理url的访问
class index:

    # 注意url路径有多少个匹配块,处理函数就要有多少个接收参数(不包括self)
    def GET(self):
        # 调用模板系统搜索文件
        return render.index()

class test:

    def GET(self, name):
        i = web.input(name=None)['name']
        print name
        print i
        return render.test(name)

def notfound():
    return web.notfound(render.notfound())

def internalerror():
    return web.internalerror('Server GG')

if __name__ == "__main__":

    # 返回当前python脚本的执行路径
    #print os.path.abspath(__file__)

    # 显示调试信息
    #web.config.debug = False

    # 创建应用实例
    app = web.application(urls, globals())

    # 自定义NotFound信息(404)
    app.notfound = notfound

    # 自定义InternalError信息(500)
    app.internalerror = internalerror

    #exit(0)
    # 初始化WCGI接口，启动内置HTTP服务器
    app.run()