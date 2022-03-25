from django.urls import path, include
from rest_framework.routers import DefaultRouter

import tutorial.views
from tutorial.api import SampleModelViewset

router = DefaultRouter()
router.register(r'sample', SampleModelViewset, basename='sample_api')

urlpatterns = [
    path('', tutorial.views.index, name='index'),
    path('sample/', tutorial.views.sample_page, name='sample'),
    path('sample2/', tutorial.views.sample_page2, name='sample2'),
    path('api/', include(router.urls)),
]