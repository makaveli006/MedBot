class OnlineStore:
    def __init__(self):
        self.products = []
        self.orders = []
        self.customers = []

    def add_product(self, product_id, name, price):
        self.products.append({'id': product_id, 'name': name, 'price': price})

    def place_order(self, customer_id, product_id, quantity):
        # Check if product exists
        product_exists = False
        for product in self.products:
            if product['id'] == product_id:
                product_exists = True
                break
        if not product_exists:
            print("Product not found!")
            return

        # Check if customer exists
        customer_exists = False
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer_exists = True
                break
        if not customer_exists:
            print("Customer not found!")
            return

        # Calculate total price
        total_price = 0
        for product in self.products:
            if product['id'] == product_id:
                total_price = product['price'] * quantity
                break

        # Apply discount
        if quantity > 10:
            total_price *= 0.9  # 10% discount

        # Add order
        self.orders.append({
            'customer_id': customer_id,
            'product_id': product_id,
            'quantity': quantity,
            'total_price': total_price
        })
        print("Order placed successfully!")

    def add_customer(self, customer_id, name, email):
        self.customers.append({'id': customer_id, 'name': name, 'email': email})

    def generate_report(self):
        print("Products:")
        for product in self.products:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")
        print("\nCustomers:")
        for customer in self.customers:
            print(f"ID: {customer['id']}, Name: {customer['name']}, Email: {customer['email']}")
        print("\nOrders:")
        for order in self.orders:
            print(f"Customer ID: {order['customer_id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Total Price: {order['total_price']}")
