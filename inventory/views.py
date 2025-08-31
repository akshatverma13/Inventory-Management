from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product, Supplier
from .serializers import ProductSerializer, SupplierSerializer
class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("supplier")
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "category"]
    ordering_fields = ["price", "stock_quantity"]
    @action(detail=True, methods=["put"], url_path="stock")
    def update_stock(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(
            product, 
            data={"stock_quantity": request.data.get("stock_quantity")}, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
