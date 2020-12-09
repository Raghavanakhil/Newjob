'''
a = "ABCABCBB"
b = len(a)
s=''
k =[]
dic = {}
for i in range(b):
    s = a[i]
    for j in range(i+1,b):

        if(a[j] not in s):
            s+=a[j]
    k.append(s)

for i in k:
    dic[i] = len(i)

print(dic)
'''

a = 'raghavan'
print(a[::-1])

n = len(a) -1

b = reversed(a)
c  = ''.join(b)
print(c)
st=''
for i in range(n+1):
    if(i<=n):
        st+=a[n-i]
print(st)


s = "learing python is very easy"
p = s.split(' ')
print(p)
k =p[::-1]
print(' '.join(k))


input = "one two three four five six"

a = input.split(' ')
b = []
for i in range (0,len(a)):
    if(i%2==0):
        b.append(a[i])
    else:

        b.append(a[i][::-1])
print(b)



m = 'B4A1D3'
k = []
l=[]
for i in m:
    if(i.isdigit()):
        k.append(i)
    else:
        l.append(i)

n = ''.join(sorted(l)+sorted(k))
print(n)


input = 'a4z3c2'
b = len(input)
s = ''
for i in range(b):
    if(input[i].isdigit()):
        s+=input[i-1]*(int(input[i])-1)
    else:
        s+=input[i]
print(''.join(sorted(s)))


a = 'aaaabbbccz'
b = len(a)
count =1
s=''
pre =''
for i in range(b):
    pre = a[i]


    if (a[i+1] in pre):
        count+=1

    else:
        s+=(str(count) + pre)
        count = 1
        i = i+1


print(s)


print('got a new job so need to work hard double')