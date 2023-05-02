def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(n):
        l.append(k)
    return l
k=int(input())
n=int(input())
print(main(k,n))