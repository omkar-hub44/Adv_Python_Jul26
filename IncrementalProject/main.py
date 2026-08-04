from models.product import Product
from registry.registry import ProductRegistry
from services.pricing_service import calculate_prices

from reports.inventory import Inventory
from reports.inventory import inventory_generator
from reports.inventory import InventoryReport

from concurrency.order_processor import process_orders
from concurrency.inventory_summary import generate_summary

from multiprocessing import freeze_support


def main():
    # Create products
    laptop = Product("Laptop", 55000, 10)
    mouse = Product("Wireless Mouse", 1200, 50)
    keyboard = Product("Mechanical Keyboard", 4500, 25)

    print("\nProduct Details")
    print("-" * 40)

    laptop.display_details()
    mouse.display_details()
    keyboard.display_details()

    # Display automatically registered product classes
    ProductRegistry.display_registered_products()

    products = [laptop, mouse, keyboard]
    price_details = calculate_prices(products)

    print("\nPrice Report")

    for product, details in zip(products, price_details):
        print(f"\nProduct: {product.name}")
        print(f"Original Price: {details['original']}")
        print(f"Discounted Price: {details['discounted']}")
        print(f"Tax: {details['tax']}")
        print(f"Final Price: {details['final']}")

    print("\nIterator Output")

    inventory = Inventory(products)

    for product in inventory:
        print(product.name)

    print("\nGenerator Output")

    for product in inventory_generator(products):
        print(product.name)

    with InventoryReport("reports/inventory_report.txt") as report:
        report.write("Inventory Report\n")
        for product in inventory_generator(products):
            report.write(
                f"{product.name} | Rs.{product.price} | Qty: {product.quantity}\n"
            )

    print("\nInventory report generated successfully.")

    print("\nProcessing Orders")

    order_quantities = [2, 5, 3]
    process_orders(products, order_quantities)

    print("\nInventory Summary")
    generate_summary(products)


if __name__ == "__main__":
    freeze_support()
    main()