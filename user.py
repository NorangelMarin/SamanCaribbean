class User:

  def __init__(self, name, dni, age, disability):
     self.name = name
     self.dni = dni
     self.age = age
     self.disability = disability
    


  def show_form(self):
    print(f'''
              
              Nombre: {self.name}
              DNI: {self.dni}
              Edad: {self.age}
              Discapacidad: {self.disability} 
              ''')

  def inf_user(self):
      return f'''
      Nombre: {self.name}
      DNI: {self.dni}
      Edad: {self.age}
      Discapacidad: {self.disability} 
      '''

  
