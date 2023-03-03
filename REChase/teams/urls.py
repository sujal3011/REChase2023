from django.urls import path, include
from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.home, name='home'),
    path('get_team/', views.get_team, name='get-team'),
    path('create-team/', views.createTeam, name='create-team'),
    path('join-team/', views.joinTeam, name='join-team'),
    path('accept-team-mate/', views.acceptTeamMateView, name='accept-teammate'),
    path('complete-profile/', views.profileCompleteView, name='complete-profile'),
    path('scoreboard/', views.scoreboardView, name='scoreboard'),
    path('rules/', views.rules, name='rules'),
    path('playerdetail/', views.playerdetail, name='teamdetail'),
    path('detailedscore/',views.detailedScoreboardView, name='detailedscore'),

    path('chase/', views.get_level, name='get-level'),
    path('chase/1/', include('nft1.urls', namespace='nft1')),
    path('chase/2/', include('palindrome3.urls', namespace='palindrome3')),
    path('chase/3/', include('cars2.urls', namespace='cars2')),
    path('chase/4/', include('chess4.urls', namespace='chess4')),
    path('chase/5/', include('museum5.urls', namespace='museum5')),
    path('chase/6/', include('closedsurface6.urls', namespace='closedsurface6')),
    path('chase/7/', include('spell7.urls', namespace='spell7')),
    path('chase/8/', include('morse8.urls', namespace='morse8')),
    path('chase/9/', include('pattern9.urls', namespace='pattern9')),
    path('chase/10/', include('evan10.urls', namespace='evan10')),
    path('chase/11/', include('catalan11.urls', namespace='catalan11')),
    path('chase/12/', include('xor12.urls', namespace='xor12')),

]
