#question 1
# rows = int(input("enter no. of rows==== "))
# for i in range (rows):
#     for z in range (rows, i, -1):
#         print(z, end="")
#     print(" ")

# question 2
# num = int(input("enter your number==== "))
# sum = 0
# while num>10:
#    sum = 0
#    while num>0:
#      sum += num % 10 
#      num//=10
#    sum = num
# print(num)

# question 3
# num = int(input("enter your number==== "))
# i = num // 10
# j = num % 10
# if (i*j) + (i+j) == num:
#     print("true")
# else:
#     print("false")

#question 4
# num = int(input("enter your num==== "))
# current = 0 
# even = 0
# odd = 0

# while num>0:
#     current = num%10
#     num//=10
#     if current%2==0:
#         even += 1
#     else:
#         odd += 1

# print(" even are", even)
# print(" odd are", odd)

# question 5
# num = int(input("enter your num==== "))
# i = num // 100
# j = num % 100 // 10
# k = num % 10
# if (i*i*i) + (j*j*j) + (k*k*k) == num:
#     print("the number is Armstrong")
# else:
#     print("the number is not Armstrong")

# question 6 
num = int(input("enter your num==== "))
current = 0
largest = 0
while num>0:
    current = num%10
    num//=10
    if current > largest:
        largest = current 
print (largest)

# question 7
# rows = int(input("enter no. of rows==== "))
# for i in range(1,rows+1):
#     for z in range (1, i+1):
#         print(z, end="")
#     print(" ")

#question 8
# num = int(input("enter your num==== "))

# while num>10 :
#     num//=10

# print(num)


#question 9
# num = int(input("enter your num==== "))
# original = num
# new_num = 0
# remainder = 0

# while num>0:
#     remainder = num % 10 
#     new_num = new_num*10 + remainder
#     num //= 10

# if new_num == original:
#     print("Palindrome")
# else:
#     print("NOT PALINDROME")

# question 10
# num = int(input("enter your num==== "))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#        count += 1
# print("number of factors ====", count)
    
#question 11
# rows = int(input("enter no. of rows==== "))
# for i in range(0, rows):
#     for z in range (0, i+1):
#          print(2**z, end=" ")
#     print(" ")

# question 12
# num = int(input("enter your last num==== "))
# for i in range(2, num+1):
#      prime = True
#      for z in range(2, int(i/2) +1 ):
#       if i % z == 0:
#         prime = False
#         break
#      if prime:
#         print(i, end = " ")

# question 13
# num = int(input("enter your num==== "))
# num1 = num
# sum = 0

# while num>0 :
#     sum += num %10
#     num //= 10

# if num1 % sum == 0:
#     print("Yes")
# else:
#     print("no")

#question 14
# num = int(input("enter your num==== "))
# current = 0
# next = 0
# while num != 0:
#     current = num %10 
#     next = (num // 10) % 10
#     if (next >= current):
#         print("no")
#         break
#     num //= 10
# if current > next:
#     print("yes")

# question 15
# num = int(input("enter your num==== "))
# n = int(input("enter n-th digit from right====="))
# original = 0
# original  =  (num // 10**(n-1)) % (10)
# print(original)
