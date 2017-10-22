class Point(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
    def __add__(self, novo):
        p1 = self.x + novo.x
        p2 = self.y + novo.y
        
        return self.__str__(p1, p2)
        
    def __str__(self,p1,p2):
        return "Pn("+str(p1)+","+str(p2)+")"