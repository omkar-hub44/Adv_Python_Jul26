from models.product import Product
from registry.registry import ProductRegistry

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

products = [laptop,mouse,keyboard]
price_details = calculate_prices(products)

print("\n Price Report")

for product,details in zip(products,price_details):
    print(f"\n Product: {product.name}")
    print(f"Original Price: {details['original']}")
    print(f"Discounted Price: {details['discounted']}")
    print(f"Tax: {details['tax']}")
    print(f"Final Price: {details['final']}")