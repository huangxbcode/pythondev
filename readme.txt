
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