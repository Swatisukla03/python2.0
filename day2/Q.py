# All the Basic Questions of Python
# Using a flag variable
# num=int(input("Enter the number :"))
# flag=False
# if num>1:
#     for i in range(2,num):
#        if(num%i)==0:
#            flag=True

#            break
# if flag:
#     print(num,"is not a prime number")

# else:
#     print(num,"is a prime number")

# Program to check if a number is prime or not
# num=int(input("Enter the number:"))
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num,"is not a prime number")
#             # print(i,"times",num//i,"is",num)
#             break
#         else:
#             print(num,"is a prime number")
#             break
# else:
#     print(num,"is not")

# Prime No between two interval
lower = int(input("Enter the from where to start:"))
higher = int(input("Enter the till the end :"))
print("Prime numbers between", lower, "and", higher, "are :")
for num in range(lower, higher+1):

    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
                print(num)
# https://www.programiz.com/python-programming/examples/prime-number
# Python program to display all the prime numbers within an interval

# lower = int(input("Enter the start no :"))
# upper = int(input("Enter the end no :"))

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
