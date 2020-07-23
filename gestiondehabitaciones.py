from user import User

def register_user():
  while True:
    try:
      name = input("Ingrese su nombre: ")
      dni = int(input("Ingrese su DNI: "))
      age = int(input("Ingrese su edad: "))
      disability = input("Tiene alguna discapacidad (S) o (N): ").upper()
      break
    except:
      print("Error! Verifique los datos ingresados.")
  return User(name, dni, age, disability)

def selectRoom(samancaribbean, pasillos, habitaciones):
  matriz = []
  dic = {}
  j = 1

  while j <= habitaciones:
    matriz.append(j)
    j+=1
    
  for letra in range(97, pasillos+97):
    i = chr(letra).upper()
    dic[i] = matriz
    print(f'''
                {i}      | {dic[i]}''')  
  
