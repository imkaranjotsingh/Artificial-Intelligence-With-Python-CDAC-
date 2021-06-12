class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self.total_marks = 0
    def getName(self):
        return str(getattr(Stu1,'name'))
    def totalScores(self):
        return sum(self.marks)
    def avgScores(self):
        return str(self.totalScores()/len(self.marks))
 
    def __str__(self):
        return "Student "+self.getName()+" has got "+self.avgScores()+" Scores."

name = input("Enter the Name:")
l = [int(input("Enter Marks of "+ str(i+1) +" Subject:")) for i in range(5)]
Stu1 = Student(name,l)
print(Stu1)
setattr(Stu1,"name","James")
print(Stu1)
        
