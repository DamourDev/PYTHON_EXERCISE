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

# a = int(input("Enter a first number:"))
# b = int(input("Enter a second number:"))
# def power(a,b):
#     return b**a
# print(f"{b} power {a} is {power(a,b)}")

# dictionary program to calculate average

students = {
    "John": [70, 80, 90,77,86],
    "Jane": [80, 90, 93,75,70],
    "Tom": [90,78,75,80,85],
    "Jerry": [80, 90, 93,75,70],
    "Alice": [90,78,75,80,85]
}

def average():
    averages = {}
    print("The following is average score of Jane and Tom :\n")
    for student in ["Jane", "Tom"]:
        avg = sum(students[student])/len(students[student])
        averages[student] = avg
        
        print(f"{student} : {avg}")

    for student in students:
        if student not in averages:
            avg = sum(students[student])/len(students[student])
            averages[student] = avg
    print("\nThe following is dictionary of students and their average scores\n :")    
    return averages

print(average())
