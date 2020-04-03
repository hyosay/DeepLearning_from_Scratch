s = input("네 개 숫자를 가진 단어를 입력하여라: ")
#1

a, b, c, d = s
s_rev = d + c + b + a
print(s_rev)

#2

s_rev1 = s[3] + s[2] + s[1] + s[0]
print(s_rev1)


#3

s_rev2 = s[::-1]
print(s_rev2)

