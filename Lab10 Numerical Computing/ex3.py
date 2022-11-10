import numpy as np

data = np.loadtxt("Lab10 Numerical Computing/grades.tsv", delimiter='\t', dtype=float) #import tsv file

numStudents = len(data) #get amount of students incase file changes
studentID = data[0:(numStudents+1),0:1] #grabs matrix of only first column (student ids)

print("Student ID\tGPA")
for i in range(numStudents):
    x = data[i,1:] #gets the student ID row excluding ID
    summ = x[0]*3 + x[1]*2 + x[2] + x[3]*3 + x[4]*3 + x[5]*3 #calculate gpa
    gpa = summ / 15
    print("%d\t%.2f"%(studentID[i],gpa))