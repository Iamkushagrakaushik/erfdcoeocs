t=int(input())
d={"Ico":20,"Cub":6,"Tet":4,"Dod":12,"Oct":8}
a=0
for i in range(t):
    s=input()
    a+=d[s[0:3]]
print(a)