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
sub1 = str(input("Enter your First Subject Name:"))
sub2 = str(input("Enter your Second Subject Name:"))
sub3 = str(input("Enter your Third Subject Name:"))
percent = float(input("Enter your Percentage:"))

print("-----------------------------STUDENT PORTFOLIO---------------------------")

print("StudentName is : " + studentName.capitalize())
print("Student std is : " + std.upper())
print("Student divison is : " + divison.upper())
print("Student Roll_No is : " + str(Rollno))
print("Student Frist Subject is : " + sub1.capitalize())
print("Student Second Subject is : " + sub2.capitalize())
print("Student Third Subject is : " + sub3.capitalize())
print("Student Percentage is : " + str(percent))




