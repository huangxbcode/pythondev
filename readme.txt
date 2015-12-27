
下载python2.7.9

demo所用网页
http://finance.yahoo.com/q?s=GOOG

Beautiful Soup
www.crummy.com/software/BeautifulSoup/
下载：beautifulsoup4-4.4.1
安装，注意要到setup.py所在目录执行：python setup.py install

from bs4 import BeautifulSoup
注意：和书上的有差别！

FireFox and Firebug
http://getfirefox.com/
http://getfirebug.com/

安装Django
https://www.djangoproject.com/download/
cd /python/django-1.9/      //进入源文件目录
python setup.py install     //安装

安装失败。可能是版本不匹配
然后重新下载Django-1.6.11，后安装成功！

Django的安装
运行环境：Windows vista, python2.7

python安装路径：C:\Python27

从 https://www.djangoproject.com/ 下载django安装包。

解压后，进入django目录，运行 python setup.py install，启动安装。

Django被安装在 C:\Python27\Lib\site-packages

第一个工程的创建,生成工程框架：
E:\workspace\pythondev>python e:\Python27\Lib\site-packages\django\bin\django-admin.py startproject todos
注意：路径问题，刚开始django-admin.py startproject todos路径不对，导致出错
 

运行开发服务器：python manage.py runserver

在浏览器中，访问 http://127.0.0.1:8000/，看到 “Welcome to Django” 的提示。

todos(上一层)目录下执行命令：python manager.py runserver
如果出现报错：
XXX
You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.
XXX
很明显，已经告诉我们怎么做了，那就执行一下：python manage.py migrate
话说这个migrate是干什么的呢，它可以让我们在修改Model后可以在不影响现有数据的前提下重建表结构。

可以看到如下输出：
Operations to perform:
Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying sessions.0001_initial... OK
这是你会发现在上一层的mysite目录下面多了一个文件dg.sqlite3

使用IDLE，感觉在编辑文档之间跳转很麻烦，下载一个IDE吧。
搜了一个，各种口味、说法的都有，先用用熟悉的eclipse吧，下载一个pydev

最近在学习Python, 打算在Eclipse中通过网络安装的方法安装pydev插件,按照网上的步骤没办法安装pydev,因为eclipse获取不到相应的信息,所以我下载了pydev的安装包（V2.2.4）,手动安装pydev,现在把过程共享一下.
       首先是安装eclipse,下载地址是点击打开链接,选一个合适的地方解压就可以用了.
       第二步是下载python,下载地址是点击打开链接,安装,我安装在c:\python
       第三步添加环境变量,和java差不多
       第四步下载pydev,地址是点击打开链接
       第五步,把下载后的pydev压缩包内的plugins和features文件夹内的内容复制到eclipse的解压目录的相应文件夹中
       第六步,打开eclipse中的菜单window,选择reference.找到左侧边栏的pydev，展开，点击Interpreter-Python
       第七步,点击new,找到python安装路径,我是c:\python\python.exe,确定导入就可以了
       这样就可以在eclipse中新建python程序了


python manage.py syncdb //Django创建指定的数据库，会询问您是否要创建管理用户。
如果此时不创建，可以用下面的命令创建：
python manage.py createsuperuser

Your url for admin should be:
url(r'^admin/', include(admin.site.urls))
not (r'^admin/(.*)', admin.site.root)----书中所示代码报错
- it's for Django 1.0. For Django 1.3 it wouldn't work.