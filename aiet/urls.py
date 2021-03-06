from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from paper import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aiet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^$', views.index),


    # Question Paper URLs
    url(r'^questionpapers$', views.fetch_qpapers_all),
    url(r'^questionpapers/(?P<branch>[a-zA-Z]{1,3})/$',views.fetch_qpapers_branch),
    url(r'^questionpapers/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/$',views.fetch_qpapers_branch_semester),
    url(r'^questionpapers/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/(?P<subject>.*)/$',views.fetch_qpapers_branch_semester_subject),

    # Laboratory Software URLs
    url(r'^laboratory-software$', views.fetch_lab_software_all),
    url(r'^laboratory-software/(?P<branch>[a-zA-Z]{1,3})/$',views.fetch_lab_software_branch),
    url(r'^laboratory-software/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/$',views.fetch_lab_software_branch_semester),
    url(r'^laboratory-software/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/(?P<title_slug>.*)/$',views.fetch_lab_software_branch_semester_package),


    # Course Notes URLs
    url(r'^course-notes$', views.fetch_course_notes_all),
    url(r'^course-notes/(?P<branch>[a-zA-Z]{1,3})/$',views.fetch_course_notes_branch),
    url(r'^course-notes/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/$',views.fetch_course_notes_branch_semester),
    url(r'^course-notes/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/(?P<subject>.*)/$',views.fetch_course_notes_branch_semester_subject),


    # Lab Manual URLs
    url(r'^labmanuals$', views.fetch_lab_manuals_all),
    url(r'^labmanuals/(?P<branch>[a-zA-Z]{1,3})/$',views.fetch_labmanuals_branch),
    url(r'^labmanuals/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/$',views.fetch_lab_manual_branch_semester),
    url(r'^labmanuals/(?P<branch>[a-zA-Z]{1,3})/(?P<semester>[0-9]{1})/(?P<subject>.*)/$',views.fetch_lab_manual_branch_semester_subject),


    # Blog urls
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    # Haystack URLs
    url(r'^search/',include('haystack.urls')),
    url(r'', include('django.contrib.staticfiles.urls')),


)
