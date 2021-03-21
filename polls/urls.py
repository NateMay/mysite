from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    # # manual
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),

    path('owner', views.owner, name='owner'),
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/

    # # generic
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # ex: /polls/5/results/


]