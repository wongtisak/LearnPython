Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.shape('Rabbit')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tao.shape('Rabbit')
  File "C:\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named Rabbit
>>> tao.shape('Dog')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tao.shape('Dog')
  File "C:\Python39\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named Dog
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> tao.forward(100)
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> tao.reset()
>>> for i in range(4):
	tao.forward(100)
	tao.left(45)

	
>>> tao.reset()
>>> for i in range(8):
	tao.forward(100)
	tao.left(45)

	
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x0000029E4E28ECA0>>
>>> tao.reset()
>>> for j in range 4():
	
SyntaxError: invalid syntax
>>> for j in rage(4):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
		tao.left(90)

		
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    for j in rage(4):
NameError: name 'rage' is not defined
>>> for j in range(4):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
		tao.left(90)

		
>>> tao.reset()
>>> for j in range(4):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(90)

	
>>> tao.reset()
>>> for j in range(4):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(180)

	
>>> tao.reset()
>>> for j in range(4):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(145)

	
>>> tao.reset()
>>> for j in range(10):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(36)

	
>>> tao.reset()
>>> for j in range(20):
	for i in range(8):
		tao.forward(100)
		tao.left(45)
	tao.left(18)

	
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> for i in range(10):
	regtangle()
	toa.left(36)

	
Traceback (most recent call last):
  File "<pyshell#74>", line 3, in <module>
    toa.left(36)
NameError: name 'toa' is not defined
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> tao.reset()
>>> for i in range(36):
	regtangle()
	tao.left(10)

	
>>> 