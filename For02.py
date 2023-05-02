def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    l='0'
    for i in range(1,n):
        l=l+','+str(i)
    return l
n=int(input())
print(main(n))