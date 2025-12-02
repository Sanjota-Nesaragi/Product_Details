def product_info(product_id, name, quantity, price):
    
    # This function returns product details in a formatted string.

    return f"Product ID: {product_id},\n Name: {name},\n Quantity: {quantity},\n Price: {price}\n"
    

if __name__ == "__main__":
    # Example call - you may change values
    result = product_info(101, "Keyboard", 5, 499.99)
    print(result)
