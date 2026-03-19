import json

mensaje = "===================================="

data = "gym_data.json"
riesgos = ["Alto", "Medio", "Bajo"]

def registrar_clientes(data):
    print(mensaje)
    print("     Registrar Clientes")
    print(mensaje)
    try:
        dpi = int(input("DPI: "))
        nombre = input("Nombre: ")
        riesgo = input("Riesgo (Alto, Medio, Bajo): ").capitalize().strip()
    except Exception as e:
        print(f"Error de entrada: {e}")
        return

    try:
        cliente = {
            "dpi": dpi,
            "Nombre": nombre,
            "Riesgo": riesgo
        }
        with open(data, "r") as file:
            clientes = json.load(file)
            
        clientes.append(cliente)
    except Exception as e:
        print(f"Error: {e}")

    encontrado = False

    for i, doc in enumerate(clientes):
        docp = doc.get('dpi')
        if dpi == docp:
            encontrado = True

    if encontrado == True:
        print("El DPI que intenta registrar ya existe")
        return
    elif riesgo not in riesgos:
        print("Riesgo no válido. Por favor, ingrese Alto, Medio o Bajo.")
        return
    elif not nombre.strip():
        print("Nombre no puede estar vacío.")
        return
    elif len(str(dpi))!= 13:
        print("DPI debe tener 13 dígitos. Intente nuevamente.")
        return
    else:
        try:
            with open(data, "w") as f:
                json.dump(clientes, f, indent=4)
                print("Cliente registrado exitosamente.")
                
        except Exception as e:
            print(f"Error: {e}")

#registrar_clientes(data)

def configurar_servicio(data):
    print(mensaje)
    print("     Configurar Servicio")
    print(mensaje)
    try:
        nombre_servicio = input("Nombre del servicio: ").strip()
        if not nombre_servicio:
            print("El nombre del servicio no puede quedar en blanco")
            return
        capacidad_maxima = int(input("Capacidad máxima: "))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    servicio = {
            "nombre": nombre_servicio,
            "capacidad": capacidad_maxima,
            "disponibles": capacidad_maxima,
            "matriculados": 0
    }
    
    try:
        with open(data, "r") as file:
            datos = json.load(file)            
    except Exception as e:
        print(f"Error: {e}")

    servicios = datos['servicios']
        
    for _ in servicios:
        name = _.get('nombre')
        if name is not None and nombre_servicio.lower() == name.lower():
           print("El servicio que intenta agregar ya existe")
           return
        
    if not nombre_servicio.strip():
        print("El campo nombre no puede estar en blanco")
        return
    else:
        servicios.append(servicio)  
        datos['servicios'] = servicios  
        
        try:
            with open(data, "w") as file:
                json.dump(datos, file, indent=4)
            print("Servicio agregado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

#configurar_servicio(data)

def mostrar_catalogos(data):
    print(mensaje)
    print("     Mostrar Catálogo")
    print(mensaje)
    try:
        with open(data, "r") as file:
            servicios = json.load(file)
            service = servicios.get('servicios')
        print("Servicios disponibles:")
        _ = 0
        for servicio in service:
            _+=1
            print(f"{_}. {servicio['nombre']}\nCapacidad: {servicio['capacidad']}\nCupos Disponibles: {servicio['disponibles']}\nPersonas Matriculadas: {servicio['matriculados']}\n")
    except Exception as e:
        print(f"Error: {e}")

mostrar_catalogos(data)

def mantenimiento_servicio(data):
    print(mensaje)
    print("     Mantenimiento de Servicio")
    print(mensaje)

    try:
        with open(data, "r") as file:
            datos = json.load(file)  
        servicios = datos.get('servicios')          
    except Exception as e:
        print(f"Error: {e}")

    servicios = datos['servicios']
    nombre_servicio = input("Ingrese el nombre del servicio que desea modificar: ").strip()
    for _ in servicios:
        name = _.get('nombre')
        if nombre_servicio.lower() == name.lower():
           print("Servicio encontrado.")
           print(mensaje)
           print("¿Qué desea modificar?")
           print("1. Capacidad máxima")
           print("2. Cupos disponibles")
           print("3. Personas matriculadas")
           print("4. Eliminar servicio")
           print("5. Volver")
        else:
            print("Servicio no encontrado.")
            return
    
    try:
        opcion = int(input("Ingrese el número de la opción: "))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    if opcion == 1:
        try:
            nueva_capacidad = int(input("Ingrese la nueva capacidad máxima: "))
            for i in servicios:
                if i['nombre'].lower() == nombre_servicio.lower():
                    i['capacidad'] = nueva_capacidad
                    print("Capacidad máxima actualizada.")
        except Exception as e:
            print(f"Error: {e}")
            return
    elif opcion == 2:
        try:
            nuevos_cupos = int(input("Ingrese el nuevo número de cupos disponibles: "))
            for i in servicios:
                if i['nombre'].lower() == nombre_servicio.lower():
                    i['disponibles'] = nuevos_cupos
                    print("Cupos disponibles actualizados.")
        except Exception as e:
            print(f"Error: {e}")
            return
    elif opcion == 3:
        try:
            nuevas_matriculas = int(input("Ingrese el nuevo número de personas matriculadas: "))
            for i in servicios:
                if i['nombre'].lower() == nombre_servicio.lower():
                    i['matriculados'] = nuevas_matriculas
                    print("Número de personas matriculadas actualizado.")
        except Exception as e:
            print(f"Error: {e}")
            return  
    elif opcion == 4:
        for i, j in enumerate(servicios):
            if j['nombre'].lower() == nombre_servicio.lower():
                servicios.pop(i)
                print("Servicio eliminado.")
                break
    elif opcion == 5:
        return
    else:
        print("Opción no válida.")
        return  

mantenimiento_servicio(data)
    

