# one2.py file
import one

print('upper level of one2.py')

one.one_func()

print('one2.py lower lavel.')


if __name__ == '__main__':
    print('Execute in One2.py file')
else:    
    print('Imported to another file')