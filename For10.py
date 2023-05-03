def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    N=len(list1)
    for i in range(N):
        list1[i]=list1[i].title()
    return list1
list1=['alisher','mardon','mahmud','diyor']
print(main(list1))