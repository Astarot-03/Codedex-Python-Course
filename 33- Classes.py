"""
Classes: serve as a template for creating objects, class is a blueprint for creating objects, and objects are instances of a class.

class Name:
the class name is always capitalized, and the class body is indented.

example:

class Student:
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

The Student class has four attributes:

.name of the type str (text string)
.year of the type int (integer number)
.gpa of the type float (decimal number)
.enrolled of the type bool (boolean value)


class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

wednesday = Student() # creates an instance of the Student class and assigns it to the variable wednesday
wednesday.student_id = 1113
wednesday.name = 'Wednesday Addams'
wednesday.year = 11
wednesday.gpa = 4.0
wednesday.enrolled = True

print(vars(wednesday)) # vars() function returns the __dict__ attribute of the object, which is a dictionary containing all the attributes of the object and their values.

# Output: {'student_id': 1113, 'name': 'Wednesday Addams', 'year': 11, 'gpa': 4.0, 'enrolled': True}

"""

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True

Bobs_Burgers = Restaurant()
Bobs_Burgers.name = 'Bob\'s Burgers'
Bobs_Burgers.category = 'American Diner'
Bobs_Burgers.rating = 4.7
Bobs_Burgers.delivery = False

Punto_Burger = Restaurant()
Punto_Burger.name = 'Punto Burger'
Punto_Burger.category = 'Fast food'
Punto_Burger.rating = 3.9
Punto_Burger.delivery = True

Pizzeta = Restaurant()
Pizzeta.name = 'Pizzeta'
Pizzeta.category = 'Pizzeria'
Pizzeta.rating = 4.1
Pizzeta.delivery = True

print(vars(Bobs_Burgers))
print(vars(Punto_Burger))
print(vars(Pizzeta))