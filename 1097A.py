s=input()
l=input().split()
m = "YES" if any(i[0] == s[0] or i[1] == s[1] for i in l) else "NO"
print(m)
# for i in l:
#     if i[0]==s[0] or i[1]==s[1]:
#         print("YES")
#         break
# else:
#     print("NO")