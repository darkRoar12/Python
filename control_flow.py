def calculate_discount(original_price,discount_percentage):

    discounted_price=original_price*discount_percentage
    return discounted_price

price=int(input("Enter the price of your commodity\n"))
dis=int(input("Enter the discount percentage\n"))

dis=dis/100

discounted_price= calculate_discount(price,dis)
print(f"The discounted priced is {discounted_price}")
if discounted_price<50:
    print("Low cost item\n")
elif discounted_price >50 and discounted_price <100:
    print("Moderate cost item\n")
else:
    print("High cost item\n")
