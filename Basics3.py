#print("hello world",9)

# car=['m','r']
# print(car)
# car[-1]= 'w'
# print(car)
# car.append('w')
# print(car)
# car.remove("w")
# print(car)

# name = "ashok"
# for w in name:
#     print(w,end=" ")


name1 = input("enter the name")#ashok
name2= input("enter the name 2")#aravind
count = 0
a =[]
for i in name1:
    if i not in name2:
        count+=1
        a.append(i)
for i in name2:
    if i not in name1:
        count+=1
        a.append(i)

print(count)
print(a)
res = " ".join(reversed(a))
print(res)
