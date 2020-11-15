"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from elevator.views import elevdata, ElevList, ElevDetail
from cross_pass.views import crossdata, CrossList, CrossDetail
from post.views import ReviewCrossList, ReviewElevList, StarElevCreate, StarCrossCreate

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('elev', elevdata),
    path('cross', crossdata),
    path('api/cross', CrossList.as_view()),
    path('api/elev', ElevList.as_view()),
    path('api/<int:pk>/cross', CrossDetail.as_view()),
    path('api/<int:pk>/elev', ElevDetail.as_view()),
    path('api/<int:pk>/cross/review', ReviewCrossList.as_view()),
    path('api/<int:pk>/elev/review', ReviewElevList.as_view()),
    path('api/<int:pk>/cross/star', StarCrossCreate.as_view()),
    path('api/<int:pk>/elev/star', StarElevCreate.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)