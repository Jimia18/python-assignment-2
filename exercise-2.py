studentNames = ['Shakira','Edith','Cathy'] #strings
studentMarks = [80,70,60] #integers
data = ['Shakira',80,'Kamokya'] #mixed types

print(studentNames,type(studentNames))

print(studentNames[0])#first item
print(studentNames[1])#second item
print(studentNames[2])#third item

print(studentNames[-3])#first item
print(studentNames[-2])#second item
print(studentNames[-1])#third item

studentNames.append('Jimia')
print(studentNames)

studentNames.insert(2,'Sherina')
print(studentNames)



# print ['Edith', 'Sherina', 'Cathy]
studentNames.pop(0)  # removes first item, 
studentNames.pop(-1)  # removes last item, 
print(studentNames)


# Add Masha at the fourth position 
studentNames.insert(3,'Masha')
print(studentNames)

#Update the name 'Shakira' to 'Hawezi Shakira'
updated_name = studentNames.replace("Shakirah","Hawezi Shakirah") 
print(updated_name)

# Display the len of the students list
studentNames=["Edith","Sherina","Cathy","Hawezi Shakirah"]
for student in studentNames:
    print(f"The length of {student} is {len(studentNames)}")


#Print all the  student names using a 'for' loop
studentNames =["Edith","Sherina","Cathy","Hawezi Shakirah"]
for student in studentNames:
    print(studentNames)

#Calculate the total marks for the student mark variable
studentMarks = [80,70,60]
totalMarks = sum(studentMarks)
print(f"The total marks for the students is:{totalMarks}",)