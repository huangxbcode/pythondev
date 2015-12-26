from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'.*', 'todo.views.hello_world'),
)
