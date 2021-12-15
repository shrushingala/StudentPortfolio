#!/usr/bin/env python
# coding: utf-8

# # #PROJECT 1.0
# 
# Name of the student ,std and divison , Roll no , Any three subject and percent 

# In[37]:


print("Student Portfolio")
studentName = str(input("Enter your name:"))
std = str(input("Enter your standard:"))
divison = str(input("Enter your divison:"))
Rollno = int(input("Enter your Roll_No:"))
sub1 = int(input("Enter your English marks:"))
sub2 = int(input("Enter your Maths marks:"))
sub3 = int(input("Enter your Science marks:"))


print("-----------------------------STUDENT PORTFOLIO---------------------------")

print("StudentName is : " + studentName.capitalize())
print("Student std is : " + std.upper())
print("Student divison is : " + divison.upper())
print("Student Roll_No is : " + str(Rollno))
print("Student English marks is : " + str(sub1))
print("Student Maths marks is : " + str(sub2))
print("Student Science marks is : " + str(sub3))
total=sub1+sub2+sub3
print("Student Average marks is :" + str(total))
percentage=total/3
print("Student Percentage is : " + str(percentage))




