# one.py file
# import one2

print('This upper level of one.py')

def one_func():
    print('This is One.py Func()')

print('This is one.py lower lavel.')


if __name__ == '__main__':
    print('Execute in One.py file')
else:
    print('Imported to one2.py file')