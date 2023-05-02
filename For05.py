def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(B,A-1,-1):
        l.append(i)
    return l
A=int(input())
B=int(input())
print(main(A,B))