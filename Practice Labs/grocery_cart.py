#define the add_to_cart function here
def add_to_cart(cart, item, quantity=1):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    return cart


def main():
    my_cart= {}
    print("Begin: cart is empty")
    add_to_cart(my_cart, "HoneyCrisp Apples", 8)
    add_to_cart(my_cart, "2% Milk 4L")
    add_to_cart(my_cart, "Rice Crispies Cereal 1kg", 2)
    add_to_cart(my_cart, "Peaches", 6)
    add_to_cart(my_cart, "Organic carrots 1kg", 2)
    print("End:", my_cart)

if __name__ == "__main__":
    main()