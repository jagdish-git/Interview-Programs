import pickle

class XXX:
    def __init__(self, rollno, name, marks):
        self.a = rollno
        self.b = name
        self.c = marks

    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)


z = XXX(12,'hi',98)

f1 = open('data.txt', 'wb')
pickle.dump(z, f1)
f1.close()

f2 = open('data.txt', 'rb')
q = pickle.load(f2)
q.display()
f2.close()

