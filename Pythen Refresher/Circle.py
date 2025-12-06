class circle():
    def __init__(self , a , p):
        self.area = a
        self.peremiter  = p

    def circle_area(self):
        return self.area * self.peremiter

newcircle =  circle(12 ,10)
print("Area of Circle - Area : %d Peremiter : %d" % (newcircle.area, newcircle.peremiter)) 
print("Peremiter of  Circle :" , newcircle. circle_area( ))