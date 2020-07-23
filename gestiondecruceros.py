def infoCruiseShips(samancaribbean):
  i = 0
  while i < len(samancaribbean):
    name = samancaribbean[i]['name']
    route = samancaribbean[i]['route']
    date = samancaribbean[i]['departure']
    cost = samancaribbean[i]['cost']
    capacity = samancaribbean[i]['capacity']
    pasillos_piso1 = samancaribbean[i]['rooms']['simple'][0]
    pasillos_piso2 = samancaribbean[i]['rooms']['premium'][0]
    pasillos_piso3 = samancaribbean[i]['rooms']['vip'][0]
    rooms_pasillo1 = samancaribbean[i]['rooms']['simple'][1]
    rooms_pasillo2 = samancaribbean[i]['rooms']['premium'][1]
    rooms_pasillo3 = samancaribbean[i]['rooms']['vip'][1]
    rooms_simple = pasillos_piso1 * rooms_pasillo1
    rooms_premium = pasillos_piso2 * rooms_pasillo2
    rooms_vip = pasillos_piso3 * rooms_pasillo3

    print(f'''
    {i+1}. Nombre del Barco: {name}.
    Rutas: {route}.
    Fecha de salida: {date}.
    Precio por habitacion: {cost}. 
    Costa de 3 pisos.
    En el piso uno tiene {pasillos_piso1} pasillos y un total de {rooms_simple} habitaciones simples distribuidas en los mismos.
    En el piso dos tiene {pasillos_piso2} pasillos y un total de {rooms_premium} habitaciones premium distribuidas en los mismos.
    En el piso tres tiene {pasillos_piso3} pasillos y un total de {rooms_vip} habitaciones vip distribuidas en los mismos.
    Capacidad por tipo de habitacion: {capacity}.
    
    ''')
    i+=1

def searchRoutes(samancaribbean, route):
  coincidences = []
  for i in range(len(samancaribbean)):
    for j in range(len(samancaribbean[i]["route"])):
      if samancaribbean[i]["route"][j].upper() == route.upper():
        coincidences.append(i)
  if len(coincidences) > 0:
    for k in coincidences:
      name = samancaribbean[k]['name']
      route = samancaribbean[k]['route']
      date = samancaribbean[k]['departure']
      cost = samancaribbean[k]['cost']
      capacity = samancaribbean[k]['capacity']
      pasillos_piso1 = samancaribbean[k]['rooms']['simple'][0]
      pasillos_piso2 = samancaribbean[k]['rooms']['premium'][0]
      pasillos_piso3 = samancaribbean[k]['rooms']['vip'][0]
      rooms_pasillo1 = samancaribbean[k]['rooms']['simple'][1]
      rooms_pasillo2 = samancaribbean[k]['rooms']['premium'][1]
      rooms_pasillo3 = samancaribbean[k]['rooms']['vip'][1]
      rooms_simple = pasillos_piso1 * rooms_pasillo1
      rooms_premium = pasillos_piso2 * rooms_pasillo2
      rooms_vip = pasillos_piso3 * rooms_pasillo3
      
      print(f'''
      {k+1}.Nombre del Barco: {name}.
      Rutas: {route}.
      Fecha de salida: {date}.
      Precio por habitacion: {cost}. 
      Costa de 3 pisos.
      En el piso uno tiene {pasillos_piso1} pasillos y un total de {rooms_simple} habitaciones simples distribuidas en los mismos.
      En el piso dos tiene {pasillos_piso2} pasillos y un total de {rooms_premium} habitaciones premium distribuidas en los mismos.
      En el piso tres tiene {pasillos_piso3} pasillos y un total de {rooms_vip} habitaciones vip distribuidas en los mismos.
      Capacidad por tipo de habitacion: {capacity}.

      ''')
  else:
    print("No tenemos cruceros con esa ruta...")
