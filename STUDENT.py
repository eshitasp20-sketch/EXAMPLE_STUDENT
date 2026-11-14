name = input("Enter student name: ")
college = input("Enter college: ")
city = input("Enter city: ")
no_of_sub = int(input("Enter number of subjects: "))
total = 0

for i in range(0, no_of_sub):
    marks = int(input("Enter marks: "))
    total = total + marks

print("Total marks: ",total)

avg = total / no_of_sub

print("Average is: ",avg)