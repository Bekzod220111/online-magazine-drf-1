from rest_framework.generics import ListAPIView
from api.user.serializers import product_serializers
from apps.shop.models import Product

class ProductListApiView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = product_serializers.ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset