class mathoperation():
    a:int=10

    def getval(self):
        return self.a

m=mathoperation()
m.a=20
print(m.getval())

mathoperation.a=30
print(id(mathoperation))
print(m.getval())

m=mathoperation()
print(m.getval())


#static method

class mathoperations:
  def __init__(self):
      pass

  def add(a:int,b:int):
    print(a+b)
mathoperations.add(1,2)

