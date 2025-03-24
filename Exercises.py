a = int(input("Enter a lower number:")) 
b = int(input("Enter a higher number:"))
def OddNumbers():
    for num in range (a,b+1):
        if num %2 != 0 :
            # 
            print(num)
            num+=2
print(f"Odd numbers between {a} and {b+1} are :" )    
OddNumbers()




