from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views.category_views import CategoryListApiView
from api.user.views.product_views import ProductListApiView

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    path('category/', CategoryListApiView.as_view()),
    path('products/', ProductListApiView.as_view())


    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]
