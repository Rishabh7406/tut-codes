class Father:
    def skill(self):
        print("Father: Knows carpentry")

class Mother:
    def talent(self):
        print("Mother: Great singer")

class Child(Father, Mother):
      # Inheriting both classes
    def hobby(self):
        print("Child: Loves painting")

c = Child()
c.skill()   # From Father
c.talent()  # From Mother
c.hobby()   # Own method