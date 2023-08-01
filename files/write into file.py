f1 = open('zigu.jpg', 'rb')
f2 = open('GOLD.jpg', 'wb')

d = f1.read()
f2.write(d)
f1.close()
f2.close()
