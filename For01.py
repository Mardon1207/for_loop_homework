import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(n):
        l.append(i)
    return l
n=int(input())
print(main(n))