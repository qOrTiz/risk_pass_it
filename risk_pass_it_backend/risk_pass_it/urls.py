from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers



router = routers.DefaultRouter()
#router.register(r'product', views.ProductsList)
router.register(r'risk', views.RiskList)
router.register(r'assessment', views.AssessmentList)
router.register(r'countermeasures', views.CountermeasuresList)
router.register(r'dashboard', views.DashboardList)
#router.register(r'categoriestree', views.CategoriesTreeList)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),

    #path('categorys', views.CategoriesList.as_view()),

    #path('category/<int:product_id>', views.snippet_list),

    # path('risk/', views.RiskList.as_view()),
    # path('risk/<int:pk>', views.RiskList.as_view()),



]