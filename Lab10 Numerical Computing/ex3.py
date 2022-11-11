import numpy as np

data = np.loadtxt("grades.tsv", delimiter='\t', dtype=float)


print("Student ID\tGPA")
for i in range(len(data)):
  studentGrades = data[i,:]
  GPA = (studentGrades[1]*3 +studentGrades[2]*2 +studentGrades[3]*1 +studentGrades[4]*3 +studentGrades[5]*3 +studentGrades[6]*3)/15
  print("%d\t%.2f"%(studentGrades[0],GPA))
  