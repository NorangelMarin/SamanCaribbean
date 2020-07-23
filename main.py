import requests
import gestiondecruceros as gc
import gestiondehabitaciones as gh
import gestiontours as gt
import gestionderestaurantes as gr


def api():
    url = "https://saman-caribbean.vercel.app/api/cruise-ships"
    response = requests.request("GET", url)
    return response.json()

def save_data(inf, file_name):
  with open(file_name, 'a') as f:
    f.write(f'{inf} \n')

def main():
    samancaribbean = api()
    cruise1 = samancaribbean[0]
    cruise2 = samancaribbean[1]
    cruise3 = samancaribbean[2]
    cruise4 = samancaribbean[3]
    impuesto = 16
    descuento = 0
    users = []
    
    start = int(input(''' 
    
    ¡Bienvenido a Saman Caribbean!
    ¿Qué desea hacer?
    
    1. Ver nuestros cruceros disponibles
    2. Adquirir un boleto a uno de nuestros cruceros.
    3. Participar en un tour.
    4. Hacer un pedido en nuestro restaurante.
    5. Ver nuestras estadisticas.
    
    >>> '''))

#1. Informacion de los barcos
    if start == 1:
      gc.infoCruiseShips(samancaribbean)
#2. Comprar un Boleto    
    elif start == 2:

      boleto = int(input('''\nDesea comprar su boleto de acuerdo a:
      1. El barco.
      2. El Destino.
      
      >>> '''))
#2.1 De acuerdo al barco
      if boleto == 1:
        print("\nSeleccione uno de nuestros cruceros disponibles: ")
        gc.infoCruiseShips(samancaribbean)
        select_cruise = int(input(">>>  "))
        select_typerooms = int(input('''\nIndique el tipo de habitación que desea:
        1. Simple
        2. Premium
        3. VIP

        >>> '''))

        people = int(input("¿Con cuantas personas viaja?: ")) + 1
#Barco 1
        if select_cruise == 1:
#A. Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[0]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[0]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 2
        elif select_cruise == 2:
#A. Habitaciones simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")   
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[1]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[1]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 3
        elif select_cruise == 3:
#Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[2]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[2]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 4
        elif select_cruise == 4:
#A. Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[3]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[3]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#2.2 De acuerdo al destino
      elif boleto == 2:
        ideal_route = input("¿A donde desea viajar? ") 
        gc.searchRoutes(samancaribbean, ideal_route)
        select_cruise = int(input(">>>  "))
        select_typerooms = int(input('''\nIndique el tipo de habitación que desea:
        1. Simple
        2. Premium
        3. VIP

        >>> '''))
      
        people = int(input("¿Con cuantas personas viaja?: ")) + 1
#Barco 1
        if select_cruise == 1:
#A. Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[0]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[0]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[0]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[0]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[0]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[0]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 2
        elif select_cruise == 2:
#A. Habitaciones simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")   
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[1]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[1]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[1]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[1]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[1]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[1]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 3
        elif select_cruise == 3:
#Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[2]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[2]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[2]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[2]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[2]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[2]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Barco 4
        elif select_cruise == 4:
#A. Habitaciones Simples
          if select_typerooms == 1:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso S
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['simple'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['simple'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: SB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['simple']
              people -= capacity

            cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
              ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#B. Habitaciones Premium
          if select_typerooms == 2:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso P
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['premium'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['premium'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: PB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['premium']
              people -= capacity

            cost = samancaribbean[3]['cost']['premium'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")            
#C. Habitaciones VIP
          if select_typerooms == 3:
            capacity = 0
            roomstaking = []

            while capacity<=people:
              print('''
              Piso V
              Pasillos | Habitaciones disponibles''')
              pasillos_piso1 = samancaribbean[3]['rooms']['vip'][0]
              rooms_pasillo1 = samancaribbean[3]['rooms']['vip'][1]
              gh.selectRoom(samancaribbean,pasillos_piso1,rooms_pasillo1)
              select_rooms = input('''
              Indique su/s habitacion/es segun el piso, pasillo y número (Ej: VB3):

              >>> ''').upper()
              roomstaking.append(select_rooms)
              capacity = samancaribbean[3]['capacity']['vip']
              people -= capacity

            cost = samancaribbean[3]['cost']['vip'] * len(roomstaking)

            users.append(gh.register_user())

            for user in users:
              if user.dni > 1:
                  for i in range(2,user.dni):
                      if (user.dni % i) != 0:
                        descuento = 10
              if user.dni > 1:
                i = 1
                plus = 0
                while (i<user.dni):
                  if (user.dni%i==0):
                    plus+=i
                  i += 1
                if (plus>(user.dni)):
                    descuento = 15
              if user.age > 65:
                if select_typerooms == 1:
                  print("Usted puede optar por un upgrade de habitacion totalmente gratis de (simple --> premium)")
                if select_typerooms == 2:
                  cost = samancaribbean[3]['cost']['simple'] * len(roomstaking)
              if user.disability == 'S':
                  descuento = 30
              

              user.show_form()
              print(f'''
              Habitaciones seleccionadas: {roomstaking}
              Monto de la/s habitacion/es: {cost}
              Obtuvo un descuento del {descuento}% 
              Se le añade un impuesto del {impuesto}%
              Monto total: {cost+(cost*impuesto/100)-(cost*descuento/100)}
                      ''')
            
            confirmacion = input("Desea concretar su compra(Si/No): ").upper()

            if confirmacion == "SI":
              print("Gracias por su compra.")
              for user in users:
                  save_data(user.inf_user(), "SellsRooms.txt")
            elif confirmacion == "NO":
              print("Gracias por su tiempo.")
#Comprar un tour                     
    elif start == 3:
        name = input("Ingrese su nombre: ")
        dni = int(input("Ingrese su DNI: "))      
        buy = "SI"
        while buy == "SI":
          tour = int(input(f'''
          Seleccione el tour que desea:
          1. Tour en el puerto.
          2. Degustacion de comida local.
          3. Trotar por el pueblo/ciudad.
          4. Visita a lugares historicos. 
          >>> '''))
          people = int(input("\nIngrese el numero de personas: "))

          if tour == 1:
            print("\n"+gt.puertoTour(name,dni,tour,people))
            buy = input("\n¿Desea participar en otro tour?(Si o No): ").upper()
          
          elif tour == 2:
            print("\n"+gt.degustacionTour(name,dni,tour,people))
            buy = input("\n¿Desea participar en otro tour?(Si o No): ").upper()
    
          elif tour == 3:
            print("\n"+gt.trotarTour(name,dni,tour,people))
            buy = input("\n¿Desea participar en otro tour?(Si o No): ").upper()
          
          elif tour == 4:
            print("\n"+gt.visitaTour(name,dni,tour,people))
            buy = input("\n¿Desea participar en otro tour?(Si o No): ").upper()
          
          else:
            print("\nEl tour ingresado no es valido, intente nuevamente.")
            buy = input("\n¿Desea participar en un tour?(Si o No): ").upper()
#Restaurante
    elif start == 4:
      print("\nIndiquenos en cual de nuestros cruceros se encuentra: ")
      gc.infoCruiseShips(samancaribbean)
      select_cruise = int(input(">>>  "))
      if select_cruise == 1:
        print(gr.restaurant(cruise1))
      elif select_cruise == 2:
        print(gr.restaurant(cruise2))
      elif select_cruise == 3:
        print(gr.restaurant(cruise3))
      elif select_cruise == 4:
        print(gr.restaurant(cruise4))
    
main()
