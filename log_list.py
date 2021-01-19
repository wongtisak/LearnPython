Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['Toyota','Honda','Isuzu']
>>> garage.append['Suzuki']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    garage.append['Suzuki']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> garage.append('Suzuki')
>>> print garage
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(garage)?
>>> print (garage)
['Toyota', 'Honda', 'Isuzu', 'Suzuki']
>>> print(grage(2))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(grage(2))
NameError: name 'grage' is not defined
>>> print(grage[2])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(grage[2])
NameError: name 'grage' is not defined
>>> print(garage[2])
Isuzu
>>> garage.remove('Honda')
>>> print(garage)
['Toyota', 'Isuzu', 'Suzuki']
>>> garage.insert(1,'Benz')
>>> print (garage)
['Toyota', 'Benz', 'Isuzu', 'Suzuki']
>>> del garage[2]
>>> print (garage)
['Toyota', 'Benz', 'Suzuki']
>>> garage.append('Suzuki')
>>> print(garage)
['Toyota', 'Benz', 'Suzuki', 'Suzuki']
>>> garage[1]='Tesla'
>>> print(garage)
['Toyota', 'Tesla', 'Suzuki', 'Suzuki']
>>> garage.remove(Suzuki')
	      
SyntaxError: EOL while scanning string literal
>>> garage.remove('Suzuki')
>>> print (garage)
['Toyota', 'Tesla', 'Suzuki']
>>> print (len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> user.sort()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    user.sort()
NameError: name 'user' is not defined
>>> users.sort()
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(revers=True)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    users.sort(revers=True)
TypeError: 'revers' is an invalid keyword argument for sort()
>>> users.sort(reverse=True)
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> users.reverse()
>>> print(users)
['p', 'n', 'b', 't', 'r', 'z']
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in users.revers():
	print(u)

	
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for u in users.revers():
AttributeError: 'list' object has no attribute 'revers'
>>> users.reverse()
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> 