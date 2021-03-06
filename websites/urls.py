from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from . import views



'''app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	path('', views.index, name='index'),
	# ex: /polls/5/
	path('<int:question_id>/', views.detail, name='detail'),
	# ex: /polls/5/results/
	path('<int:question_id>/results/', views.results, name='results'),
	# ex: /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
]'''


app_name = 'websites'
urlpatterns = [
	path('',views.Homepage, name='Homepage'),
	path('login/',views.loginattempt, name='loginattempt'),
	path('login/#',views.login, name='login'),
	path('directory/',views.directory, name='directory'),
	path('calendar/',views.events, name='events'),
	path('editpage/',views.editpage, name='editpage'),
	path('edit/',views.edit, name='edit'),
	path('schedule/',views.adddate, name='adddate'),
	path('schedule/#',views.insertdate, name='insertdate'),
	path('newmember/',views.newmember, name='newmember'),
	path('newmember/#',views.insertmember, name='insertmember'),
	path('customize/#',views.customize, name='customize'),
	path('customize/send',views.send_email, name='send_email'),
	path('register/', views.signup, name='signup'),
	path('register/#', views.register, name='register'),
	path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
	path('myPage/', views.myPage, name='myPage'),
	path('myPage/#', views.changepass, name='changepass'),
	path('varsity/<int:vnum>', views.varsitee, name='varsitee'),
	path('varsity2/<int:vnum>', views.varsitee2, name='varsitee2'),
	path('varsity3/<int:vnum>', views.varsitee3, name='varsitee3'),
	path('logout/', views.logout, name='logout'),
	path('subscribe/<int:vnum>', views.subscribe, name='subscribe'),
	path('descedit/', views.descedit, name='descedit'),
	path('customize2/', views.edit2, name='edit2'),
	path('subscriptions/',views.subscriptions,name='subscriptions'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT, }),]'''