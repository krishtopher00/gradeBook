studentGrades= [[98, 95, 88, 93,  75,  96],
                [46, 70, 30, 100, 100, 85],
                [88, 76, 91, 92,  89,  83]]

classTotal = 0.0
studentAverages = []
for row in studentGrades:
    totalSoFar = 0.0
    for value in row:
        totalSoFar += value
        classTotal += value
        
    average = totalSoFar/ 6
    average = round(average, 2)
    studentAverages.append(average)

classTotal /= 18
classTotal = round(classTotal,2)
    
print("The student averages are: {}".format(studentAverages))
print("The class average is: {}".format(classTotal))    
    
