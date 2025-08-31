from rest_framework import serializers
from .models import Product, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    low_stock = serializers.SerializerMethodField()
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source="supplier",
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "price",
            "stock_quantity",
            "supplier",
            "supplier_id",
            "low_stock",
        ]

    def get_low_stock(self, obj):
        return obj.stock_quantity < 10

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value