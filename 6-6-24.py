# Print function
print('Hello world \'in quote\'')
s = 'variable'
print('Hello world with',s,'in between')
#using % format
n = 5
print('Hello world with %d %s in between'%(n,s))
#using format method
print('Hello world with {} {} using format method'.format(n,s))
#concatenate
print('Hello world with'+ str(n) + s+'using concatenation')
#multiline
print(f'''Hello word
\t with {n} {s}
\t Using f string and multiline''')

#diff variables
a = 5
b = 6
s = 'yes'
l = ['yes','no','hello','bye']
sets = (3,5,67,3)
dictionary = {'a':1,'b':4,'c':6}

print(len(l) > len(sets))
if 2>3:
    print('false')

for i in l:
    print(len(i))
c = 0
e = ''
while e != 'hello':
    e = l[c]
    c += 1
    print('while loop')
print('While loop exit')

print(id(l))

lis = list(s)
print(lis)