# # # # print("hello world",9)

# # # # car=['m','r']
# # # # print(car)
# # # # car[-1]= 'w'
# # # # print(car)
# # # # car.append('w')
# # # # print(car)
# # # # car.remove("w")
# # # # print(car)

# # # # name = "ashok"
# # # # for w in name:
# # # #     print(w,end=" ")


# # # # name1 = input("enter the name")#ashok
# # # # name2= input("enter the name 2")#aravind
# # # # count = 0
# # # # a =[]
# # # # for i in name1:
# # # #     if i not in name2:
# # # #         count+=1
# # # #         a.append(i)
# # # # for i in name2:
# # # #     if i not in name1:
# # # #         count+=1
# # # #         a.append(i)

# # # # print(count)
# # # # print(a)
# # # # res = " ".join(reversed(a))
# # # # print(res)

# # # def min_max(Array):
# # #     minimum = min(Array)
# # #     maximum = max(Array)
# # #     return minimum,maximum

# # # number = int(input("enter the length: "))
# # # Array =[]
# # # for i in range(number):                                 
# # #     value=int(input("enter the numbers: "))
# # #     Array.append(value)
# # # result = min_max(Array)
# # # print(result)
# # # print(f"minimum:{result[0]},maximum:{result[1]}")

# # def add(a,b):
# #     x = a+b
# #     return x
# # def sub(a,b):
# #     x = a-b
# #     return x
# # def mul(a,b):
# #     x = a*b
# #     return x
# # def div(a,b):
# #     x = a/b
# #     return x
# # a = int(input("enter 1st number: "))
# # b = int(input("enter 2nd number: "))
# # operation = print("add,sub,mul,div")
# # do = input("enter Arth operation")

# # if(do == "add"):
# #     print(add(a,b))
# # elif(do == "sub"):
# #     print(sub(a,b))
# # elif(do == "mul"):
# #     print(mul(a,b))
# # elif(do == "div"):
# #     print(f"division_result {int(div(a,b))}")
# # else:
# #     print("enter the correct value")


# car = {
#     "branch" : "ford",
#     "model" : "mustung",
#     "make" : 1997
# }

    
# car["make"] = 1990

# print(car["make"])



def sum(packet,length, secure_byte):
    initial = 0xFF
    value = 0x00
    result = 0x00
    for i in range(3,length):
        value = initial ^ packet[i]
        result = value ^ secure_byte

    return result


packet =[0]*64
bz_count = 0
packet[1] = bz_count
address0 = 0x14
address1 = 0x15
address2 = 0x16
data0 = [0x11]*16
data1 = [0x12]*16
data2 = [0x13]*16
length = 64
packet[2] = address0
packet[3] = length
packet[4:19]= data0 
packet[20] = address1
packet[21] = length
packet[22:37]= data1
packet[38] = address2
packet[39] = length
packet[40:55]= data2

crc = sum(packet,length, secure_byte = 0xED)
packet[0] = crc

print(packet)

