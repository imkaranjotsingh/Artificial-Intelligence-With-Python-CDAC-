class Employee:
    institute = 'C-DAC'
    def __init__(self,eid,name,age):
        self.eid = eid
        self.name = name
        self.age = age
emp = Employee(100,'Ram',15)
print(getattr(emp,'name'))# Ram
setattr(emp,"age",23)
print(hasattr(emp,'eid'))#True
print(getattr(emp,'age'))#23
