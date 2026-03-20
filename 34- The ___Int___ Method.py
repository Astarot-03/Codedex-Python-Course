"""
The __init__() Method: it allows us to construnct objects with unique attributes in one line.
from:
class Student: 
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

daniel = Student()
daniel.name = 'Daniel Li'
daniel.year = 10
daniel.gpa = 4.0
daniel.enrolled = True

print(vars(daniel))
# Output: {'name': 'Daniel Li', 'year': 10, 'gpa': 4.0, 'enrolled': True}

to:

class Student: 
  def __init__(self, name, year, gpa, enrolled): with self, we can assign the attributes to the object being created.
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)

print(vars(daniel))
# Output: {'name': 'Daniel Li', 'year': 10, 'gpa': 4.0, 'enrolled': True}
"""


class City: 
  def __init__(self, name, country, population, landmarks, founding_year, 
altitude):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.founding_year = founding_year
    self.altitude = altitude 

bogota = City('Bogota', 'Colombia', 7950000, ['Monserrate, Guadalupe, Museo del Oro'], 1538, 2600)
tokyo = City('Tokyo', 'Japon', 36900000, ['Tokio Tower, Shibuya, Ghibli Studies'], 660, 40)


print(vars(bogota))
print(vars(tokyo))
