__author__ = 'Aidan'
import copy

class foo():
    notagoodidea = "what am I now?"
    pass

newinst = foo()
newinst.x = "who knows"
#print(foo.notagoodidea)
#print(newinst.x)

newc = foo()
newc.notagoodidea = "who's on first?"
#print(newc.notagoodidea)

cpy = copy.copy(newinst)
cpy.notagoodidea = "I'm lost"
#print(cpy.notagoodidea)
print(foo.notagoodidea)
print(newinst.x)
print(newc.notagoodidea)
print(cpy.notagoodidea)
print(id(newinst),id(newc))