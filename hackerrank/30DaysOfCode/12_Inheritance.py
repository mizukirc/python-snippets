class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, a, b, c, d):
        self.firstName = a
        self.lastName = b
        self.idNumber = c
        self.scores = d
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        ave_score = sum(self.scores) / len(self.scores)
        if 90 <= ave_score <= 100:
            grade = 'O'
        elif 80 <= ave_score < 90: 
            grade = 'E'
        elif 70 <= ave_score < 80: 
            grade = 'A'
        elif 55 <= ave_score < 70: 
            grade = 'P'
        elif 40 <= ave_score < 55: 
            grade = 'D'
        else:
            grade = 'T'
        return grade
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
