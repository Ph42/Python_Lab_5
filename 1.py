class test:
    name = 'Larry'
    def setname(self, value):
        self.name = value

x = test()
print ('x.name = ',x.name,' test.name = ',test.name)
test.setname(x, "Tom")
print ('x.name = ',x.name,' test.name = ',test.name)
x.setname("Baggins")
print ('x.name = ',x.name,' test.name = ',test.name)
test.name = 'Dwane'
print ('x.name = ',x.name,' test.name = ',test.name)