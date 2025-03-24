# a = int(input("Enter a lower number:")) 
# b = int(input("Enter a higher number:"))
# def OddNumbers():
#     for num in range (a,b+1):
#         if num %2 != 0 :
#             # 
#             print(num)
#             num+=2
# print(f"Odd numbers between {a} and {b+1} are :" )    
# OddNumbers()

# program to return first number to the powe of the second number

a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
def power(a,b):
    return b**a
print(f"{b} power {a} is {power(a,b)}")