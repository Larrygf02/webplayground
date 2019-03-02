from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView
from . import views
pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name="create")
], 'pages') 