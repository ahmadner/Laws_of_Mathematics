#===================================================|
#   [1]  [Laws of geometric shapes]                 |
#   [2]  coding by : python 3.8                     |
#   [3]  coder : Ahmad nueirat                      |
#   [4]  github : https://www.github.com/ahmadner   |
#===================================================| 

#   Circle
#   Square
#   triangle  
#   A rectangle


from os import system


def info ():
    _info ='''
|===================================================|
|   [*]  [Laws of geometric shapes]                 |
|   [*]  coding by : python 3.8                     |
|   [*]  coder : Ahmad nueirat                      |
|   [*]  github : https://www.github.com/ahmadner   |
|===================================================| 
    
    '''
    return _info

def mainFrame():
    _ = system ('clear')
    print ('''
[*] Laws of geometric shapes

[1] Circle
[2] Square
[3] triangle
[4] rectangle                   (   comming soon    )
[5] Laws of geometric shapes    (   comming soon    )
[6] for info
[7] exit
[0] clear

    ''')
    
def circleFrame():
    _ = system ('clear')
    print ('''<====================>    
[*] Circuit laws

[1] Circle area
[2] Circumference of a circle
[3] Back ...
<====================>
    ''')

def squareForm():
    _ = system ('clear')
    print ('''<====================>

[*] Square laws

[1] area of square
[2] Back ...

<====================>
    ''')  

def triangleForm():
    _ = system ('clear')
    print ('''<====================>

[*] Square laws

[1] area of triangle
[2] Back ...

<====================>
    ''')
#<======================================>
def circleRules():
    circleFrame()
    pi = 3.14159265359
    choice = str (input('Select a number ==> '))
    if choice == '1': # Circle area
        radius = float(input ('\nRadius of the circle [Centimeter] ==> '))
        area = (radius ** 2 * pi)
        res = f'\nThe result is : {area} cm\n'
        mainFrame()
        return res
    elif choice == '2': # Circumference of a circle
        radius = float(input ('\nRadius of the circle [Centimeter] ==> '))
        area = (radius * 2 * pi)
        res = f'\nThe result is : {area} cm\n'
        mainFrame()
        return res
    elif choice == '3': # back
        mainFrame()
    else:
        return circleRules()
#<======================================>

def squareRules():

    squareForm() 
    choice = str (input('Select a number ==> '))

    if choice == '1':
        lng = float(input ('Side square length [Centimeter] ==> '))
        area = lng**2
        res = f'\nThe result is : {area} cm\n'
        mainFrame()
        return res
    elif choice == '2':
        mainFrame()
    else:
        squareForm()

#<======================================>

def triangleRules():
    triangleForm()
    choice = str (input('Select a number ==> '))
    if choice == '1':
        bace = float (input ('\nBase side length [Centimeter] ==> '))
        height = float (input ('\nThe height of the triangle [Centimeter] ==> '))
        area = 0.5*bace*height
        res = f'\nThe result is : {area} cm\n'
        mainFrame()
        return res
    elif choice == '2':
        mainFrame()
    else:
        triangleForm()

mainFrame()
while True :    
    choice = str (input('Select a number ==> '))
    if choice == '0':
        mainFrame()
    elif choice == '1':
        print (circleRules())
    elif choice == '2':
        print (squareRules())
    elif choice == '3':
        print (triangleRules())
    elif choice == '4':
        mainFrame()
        print ('[4] comming soon ...\n')
    elif choice == '5':
        mainFrame()
        print ('[5] comming soon ...\n')
    elif choice == '6':
        print (info())

    elif choice == '7':
        print ('\n\n')
        break    
    else:
        mainFrame()