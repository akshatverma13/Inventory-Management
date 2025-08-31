import csv
from django.core.management.base import BaseCommand
from inventory.models import Supplier, Product


class Command(BaseCommand):
    help = "Import suppliers and products from CSV files"

    def handle(self, *args, **kwargs):
        suppliers_file = "/Users/akshatverma/Desktop/Akshat_Assignment/backend_assignment/data/suppliers.csv"
        products_file = "/Users/akshatverma/Desktop/Akshat_Assignment/backend_assignment/data/products.csv"

        self.stdout.write(self.style.WARNING("Importing suppliers..."))
        self.import_suppliers(suppliers_file)

        self.stdout.write(self.style.WARNING("Importing products..."))
        self.import_products(products_file)

        self.stdout.write(self.style.SUCCESS("Data import completed!"))

    def import_suppliers(self, filepath):
        with open(filepath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                supplier, created = Supplier.objects.get_or_create(
                    name=row["name"],
                    defaults={"contact_email": row.get("email", None)},
                )
                self.stdout.write(f"{'Created' if created else 'Exists'}: {supplier.name}")

    def import_products(self, filepath):
        default_supplier = Supplier.objects.first()
        if not default_supplier:
            self.stdout.write(self.style.ERROR("No suppliers found! Import suppliers first."))
            return

        with open(filepath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product, created = Product.objects.get_or_create(
                    name=row["name"],
                    supplier=default_supplier,
                    defaults={
                        "category": row.get("category", ""),
                        "price": float(row.get("price", 0)),
                        "stock_quantity": int(row.get("stock_quantity", 0)),
                    },
                )
                if not created:
                    product.price = float(row.get("price", 0))
                    product.stock_quantity = int(row.get("stock_quantity", 0))
                    product.save()
                self.stdout.write(f"{'Created' if created else 'Updated'}: {product.name}")
