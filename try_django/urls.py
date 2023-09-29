"""
URL configuration for try_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from staff_members.views import member_view
from django.contrib import admin
from django.urls import path
from articles.views import(
    article_create_view,
    article_search_view,
    home
)
from accounts.views import(
    account_login_view,
    account_logout_view,
    account_register_view

)
from staff_members.views import(
    member_view,
    member_detail_view
)

urlpatterns = [
    path('',home),
    path('articles/', article_create_view),
    path('articles/create/',article_create_view),
    path('articles/search/', article_search_view),
    path('articles/search/<int:id>/', article_search_view),
    path('admin/', admin.site.urls),
    path('login/',account_login_view),
    path('logout/',account_logout_view),
    path('register/',account_register_view),
    path('member/',member_view),
    path('member/<str:name>/',member_detail_view)

]
