def calculate_discount(original_price,discount_percentage):

    discount=original_price*discount_percentage
    discounted_price=original_price-discount
    return f"The final price of the commodity of original price ${original_price} after a discount of ${discount} is ${discounted_price}"

price=int(input("Enter the price of your commodity\n"))
dis=int(input("Enter the discount percentage\n"))

dis=dis/100

final_price= calculate_discount(price,dis)
print(final_price)