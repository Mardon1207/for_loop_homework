def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    l=[]
    m=price
    for i in range(1,11):
        l.append(m)
        m+=price
    return l
price=float(input())
print(main(price))