

class Student:
    def __init__(self, id , name):
        self.id = id
        self.name  = name

    def print(self):
        print(f"student name: {self.name}\nstudent ID: {self.id}")

class Marks(Student):
    def __init__(self, id, name, ds,algo,cal):
        super().__init__(id,name)
        self.ds = ds
        self.algo = algo
        self.cal = cal

    def print(self):
        super().print()
        print(f"DS:{self.ds}\nALGO:{self.algo}\nCAL:{self.cal}")

class Result(Marks):
    def __init__(self,id,name,ds,algo,cal):
        super().__init__(id,name,ds,algo,cal)

    def calc(self):
        print(f"Marks: {self.ds+self.algo+self.cal}\nAverage: {(self.ds+self.algo+self.cal)/3}")

final = Result(230073,"rayyyyy",98,99,100)
final.print()
final.calc()        
