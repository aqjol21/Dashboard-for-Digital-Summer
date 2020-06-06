pastCGpa = float(input("Past CGpa: "))
pastCredits = int(input("Past credits: "))
print("Let's calculate your current gpa: ")
pastScore = pastCGpa*pastCredits
letter = {'A' : 4,
          'A-': 3.67,
          'B+': 3.33,
          'B' : 3,
          'B-': 2.67,
          'C+': 2.33,
          'C' : 2,
          'C-': 1.67,
          'D+': 1.33,
          'F' : 0} 
tsCredits = 0
tsScore = 0

while(True):
    grade = input("Grade or press Q to quit ")
    if(grade=='Q' or grade=='q'):
        break
    credits = int(input("Credit "))
    tsCredits += credits
    tsScore += credits*letter[grade]
    grading = input("Press Y/y to select letter grading ")
    if(grading=="Y" or grading=='y'):
        pastCredits += credits
        pastScore += credits * letter[grade]

print("Your semester grade before SD/UD is  ")
print('%.2f' %(tsScore/tsCredits))
print("Your cgpa after SD/UD is ")
print('%.2f' %(pastScore/pastCredits))

