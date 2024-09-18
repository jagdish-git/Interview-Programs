# Encapsulation

class Students:
    cls_var = 897

    def __init__(self, name='AK', rank=10, points=300):
        self.name = name
        self.rank = rank
        self.points = points

   # instance method
    def demofunc(self):
        print("I am "+self.name)
        print("I got Rank ",+self.rank, " and points of ", self.points)
    
    @classmethod
    def clsmethod(cls):
        print(cls.cls_var)

    @staticmethod
    def static_method():
        print('hii there !')




if __name__ == "__main__":
    # create 4 objects
    st1 = Students("Steve", 1, 100)
    st2 = Students("Chris", 2, 90)
    st3 = Students("Mark", 3, 76)
    st4 = Students("Kate", 4, 60)
    st5 = Students()

    # st1.demofunc()
    # st2.demofunc()
    # st3.demofunc()
    # st4.demofunc()
    st5.demofunc()

    st1.clsmethod()
    st1.static_method()
