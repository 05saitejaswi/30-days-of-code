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
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores

    def calculate(self):
        a=sum(self.scores)/len(self.scores)
        if a >= 90:
            return 'O'
        elif 90>a>=80:
            return 'E'
        elif 80>a>=70:
            return 'A'
        elif 70>a>=55:
            return 'P'
        elif 55>a>=40:
            return 'D'
        else:
            return 'T'
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
