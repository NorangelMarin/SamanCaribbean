def restaurant(cruzer1):

  menu = []

  foods = cruzer1["sells"]
  cocacola = foods[0]["name"]
  cocacola_price = foods[0]["price"]
  pizza = foods[1]["name"]
  pizza_price = foods[1]["price"]
  hamburguesa = foods[2]["name"]
  hamburguesa_price = foods[2]["price"]
  hamburguesa_refresco = foods[3]["name"]
  hamburguesa_refresco_price = foods[3]["price"]
  ron = foods[4]["name"]
  ron_price = foods[4]["price"]

  name = input("Ingrese su nombre: ")
  dni = int(input("Ingrese su dni: "))


  add_more = "SI"

  while add_more == "SI":
    options = input(f''' ¿Qué desea comprar?
    Alimentos: 

    1. {pizza} --> ${pizza_price}
    2. {hamburguesa} --> ${hamburguesa_price}

    Bebidas: 

    3. {cocacola} --> ${cocacola_price}
    4. {ron} --> ${ron_price}

    Menú de Combos:

    5. {hamburguesa_refresco} --> ${hamburguesa_refresco_price}
    
    >>> ''')
    menu.append(options)
    add_more = input("¿Desea añadir algo más a su compra? ").upper()
  return f'''
  Su pedido fue de los alimentos {menu}.
  Gracias por su compra.'''
