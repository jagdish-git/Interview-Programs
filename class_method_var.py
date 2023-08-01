class Abc():
    w = 'Subas ch. Bose'
    def __init__(self):
        self.first_name = 'Mohandas'
        self.middle_name = 'Karamchand'
        self.last_name = 'Gandhi'
    
    def show(self):
        self.name = 'Father of Nation'

    @classmethod
    def display(cls):
        cls.baby = 'baby boss'

    @staticmethod
    def adult(age):
        return age > 18

x = Abc()
x.show()
x.display()

print(x.adult(23))