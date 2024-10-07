n=input()
print(max(int(n[:len(n)-1]),int(n[:len(n)-2]+n[-1]),int(n)))
