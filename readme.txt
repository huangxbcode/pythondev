
����python2.7.9

demo������ҳ
http://finance.yahoo.com/q?s=GOOG

Beautiful Soup
www.crummy.com/software/BeautifulSoup/
���أ�beautifulsoup4-4.4.1
��װ��ע��Ҫ��setup.py����Ŀ¼ִ�У�python setup.py install

from bs4 import BeautifulSoup
ע�⣺�����ϵ��в��

FireFox and Firebug
http://getfirefox.com/
http://getfirebug.com/

��װDjango
https://www.djangoproject.com/download/
cd /python/django-1.9/      //����Դ�ļ�Ŀ¼
python setup.py install     //��װ

��װʧ�ܡ������ǰ汾��ƥ��
Ȼ����������Django-1.6.11����װ�ɹ���

Django�İ�װ
���л�����Windows vista, python2.7

python��װ·����C:\Python27

�� https://www.djangoproject.com/ ����django��װ����

��ѹ�󣬽���djangoĿ¼������ python setup.py install��������װ��

Django����װ�� C:\Python27\Lib\site-packages

��һ�����̵Ĵ���,���ɹ��̿�ܣ�
E:\workspace\pythondev>python e:\Python27\Lib\site-packages\django\bin\django-admin.py startproject todos
ע�⣺·�����⣬�տ�ʼdjango-admin.py startproject todos·�����ԣ����³���
 

���п�����������python manage.py runserver

��������У����� http://127.0.0.1:8000/������ ��Welcome to Django�� ����ʾ��

todos(��һ��)Ŀ¼��ִ�����python manager.py runserver
������ֱ���
XXX
You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.
XXX
�����ԣ��Ѿ�����������ô���ˣ��Ǿ�ִ��һ�£�python manage.py migrate
��˵���migrate�Ǹ�ʲô���أ����������������޸�Model������ڲ�Ӱ���������ݵ�ǰ�����ؽ���ṹ��

���Կ������������
Operations to perform:
Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying sessions.0001_initial... OK
������ᷢ������һ���mysiteĿ¼�������һ���ļ�dg.sqlite3

ʹ��IDLE���о��ڱ༭�ĵ�֮����ת���鷳������һ��IDE�ɡ�
����һ�������ֿ�ζ��˵���Ķ��У���������Ϥ��eclipse�ɣ�����һ��pydev

�����ѧϰPython, ������Eclipse��ͨ�����簲װ�ķ�����װpydev���,�������ϵĲ���û�취��װpydev,��Ϊeclipse��ȡ������Ӧ����Ϣ,������������pydev�İ�װ����V2.2.4��,�ֶ���װpydev,���ڰѹ��̹���һ��.
       �����ǰ�װeclipse,���ص�ַ�ǵ��������,ѡһ�����ʵĵط���ѹ�Ϳ�������.
       �ڶ���������python,���ص�ַ�ǵ��������,��װ,�Ұ�װ��c:\python
       ��������ӻ�������,��java���
       ���Ĳ�����pydev,��ַ�ǵ��������
       ���岽,�����غ��pydevѹ�����ڵ�plugins��features�ļ����ڵ����ݸ��Ƶ�eclipse�Ľ�ѹĿ¼����Ӧ�ļ�����
       ������,��eclipse�еĲ˵�window,ѡ��reference.�ҵ���������pydev��չ�������Interpreter-Python
       ���߲�,���new,�ҵ�python��װ·��,����c:\python\python.exe,ȷ������Ϳ�����
       �����Ϳ�����eclipse���½�python������


python manage.py syncdb //Django����ָ�������ݿ⣬��ѯ�����Ƿ�Ҫ���������û���
�����ʱ��������������������������
python manage.py createsuperuser

Your url for admin should be:
url(r'^admin/', include(admin.site.urls))
not (r'^admin/(.*)', admin.site.root)----������ʾ���뱨��
- it's for Django 1.0. For Django 1.3 it wouldn't work.