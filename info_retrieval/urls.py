"""info_retrieval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from productReviewSearch import views
from rest_framework.routers import DefaultRouter
from productReviewSearch.views import home, search_results

router = DefaultRouter()
router.register('products', views.ProductViewSet)

# urlpatterns = [
#     #path('', include(router.urls)),
#     path('search/', SearchResultsView.as_view(), name='search_results'),
#     path('', HomePageView.as_view(), name='home'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info_retrieval/', include(router.urls)),
    path('info_retrieval/search', views.search_product),
    path('search_results', views.search_results, name='search_results'),
    path('home', views.home, name='home')
]
