import json

mensaje = "===================================="

data = "gym_data.json"
riesgos = ["Alto", "Medio", "Bajo"]

'''def registrar_clientes(data):
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
            datos = json.load(file)
        clientes = datos['clientes']
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

registrar_clientes(data)
'''
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
            datos = json.load(file)
            service = datos.get('servicios')
        print("Servicios disponibles:")
        _ = 0
        print("========   CLIENTES   =========")
        for servicio in service:
            _+=1
            print(f"{_}. {servicio['nombre']}\nCapacidad: {servicio['capacidad']}\nCupos Disponibles: {servicio['disponibles']}\nPersonas Matriculadas: {servicio['matriculados']}\n")
    
    except Exception as e:
        print(f"Error: {e}")

#mostrar_catalogos(data)

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
    for i, j in enumerate(servicios):
        if nombre_servicio.lower() == j['nombre'].lower():
           print("Servicio encontrado.")
           print(mensaje)
           print("¿Qué desea modificar?")
           print("1. Capacidad máxima")
           print("2. Eliminar servicio")
           print("3. Volver")
    
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
        for i, j in enumerate(servicios):
            if j['nombre'].lower() == nombre_servicio.lower():
                servicios.pop(i)
                print("Servicio eliminado.")
                break
    elif opcion == 3:
        return
    else:
        print("Opción no válida.")
        return  
    
    with open(data, "w") as file:
        json.dump(datos, file, indent=4)

#mantenimiento_servicio(data)
    
def matricular_en_servicio(data):
    print(mensaje)
    print("     Matricular en Servicio")
    print(mensaje)
    try:
        dpi = int(input("DPI del cliente: "))
        nombre_servicio = input("Nombre del servicio: ").strip()
        fecha = input("Fecha inicio: ")
        duracion = int(input("Duracion (en dias): "))
    except Exception as e:
        print(f"Error: {e}")
        return
    
    try:
        with open(data, "r") as file:
            datos = json.load(file)  
        servicios = datos.get('servicios')          
    except Exception as e:
        print(f"Error: {e}")

    servicio_encontrado = None
    for servicio in servicios:
        if servicio['nombre'].lower() == nombre_servicio.lower():
            servicio_encontrado = servicio
            servicio['matriculados'] += 1
            servicio['disponibles'] -= 1
            break

    if not servicio_encontrado:
        print("Servicio no encontrado.")
        return
    elif servicio_encontrado['disponibles'] <= 0:
        print("No hay cupos disponibles para este servicio.")
        return
    else:
        matricula = {
        "dpi": dpi,
        "servicio": nombre_servicio,
        "fecha": fecha,
        "duracion": duracion,
        "asistencias": 0
        }
        try:
            with open(data, "r") as file:
                datos = json.load(file)  
            matriculas = datos.get('matriculas')      
            dpiP = datos.get('clientes')    
        except Exception as e:
            print(f"Error: {e}")

        encontrado = True
        for _ in dpiP:
            if _['dpi'] == dpi:
                encontrado = False

        if len(str(dpi)) != 13:
            print("Su dpi debe contener 13 caracteres")
            return
        elif encontrado != False:
            print("Lo sentimos, dpi no registrado")
        else:
            for m in matriculas:
                if m['dpi'] == dpi and m['servicio'].lower() == nombre_servicio.lower():
                    print("El cliente ya está matriculado en este servicio.")
                    break
                else:
                    matriculas.append(matricula)

                    datos['matriculas'] = matriculas
                    datos['servicios'] = servicios
                    with open(data, "w") as file:
                        json.dump(datos, file, indent=4)
                    
                    print("Cliente matriculado exitosamente.")
                    break

#matricular_en_servicio(data)

def evaluar_progreso(data):
    print(mensaje)
    print("     Evaluar progreso")
    print(mensaje)
    try:
        dpi = int(input("DPI del cliente: "))
        nombre_servicio = input("Servicio matriculado: ").strip()
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        with open(data, "r") as file:
            datos = json.load(file)  
        matriculados = datos.get('matriculas')          
    except Exception as e:
        print(f"Error: {e}")

    encontrado = None
    for _ in matriculados: 
        dpiP = _.get('dpi')
        if dpiP == dpi:
            encontrado = True
        
    if len(str(dpi)) != 13:
        print("Su dpi debe contener 13 caracteres")
        return
    elif encontrado != False:
       for m in matriculados:
            if m['dpi'] == dpi and m['servicio'].lower() == nombre_servicio.lower() and m['duracion'] > m['asistencias']:
                m['asistencias'] += 1
                datos['matriculas'] = matriculados
                with open(data, "w") as file:
                    json.dump(datos, file, indent=4)
                    
                print("Asistencia registrada")
                break
            elif m['asistencias'] == m['duracion'] or m['asistencias'] > m['duracion']:
                print("Curso terminado satisfactoriamente")
                break
            elif m['servicio'].lower() != nombre_servicio.lower():
                print("Servicio no entrado o no matriculado")
                return
            elif m['dpi'] != dpi:
                print("DPI no registrado o no tiene ningun servicio matriculado")
                return
            
#evaluar_progreso(data)

def gestionar_instructores(data):
    print(mensaje)
    print("    Gestionar instructores")
    print(mensaje)
    try:
        dpi = int(input("DPI del instructor: "))
        nombre_instructor = input("Nombre del instructor: ").strip()
        area_instructor = input("Area de especializacion: ").strip()
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        with open(data, "r") as file:
            datos = json.load(file)  
        instructores = datos.get('instructores')          
    except Exception as e:
        print(f"Error: {e}")

    encontrado = False

    for i, doc in enumerate(instructores):
        docp = doc.get('dpi')
        area = doc.get('area')
        if dpi == docp and area.lower() == area_instructor.lower():
            encontrado = True

    if encontrado == True:
        print("El instructor ya esta regsitrado en esa area")
        return

    elif not nombre_instructor.strip():
        print("Nombre no puede estar vacío.")
        return
    elif len(str(dpi))!= 13:
        print("DPI debe tener 13 dígitos. Intente nuevamente.")
        return
    else:
        try:
            instructor = {
            "dpi": dpi,
            "nombre": nombre_instructor,
            "area": area_instructor
            }

            datos['instructores'] = instructores
            instructores.append(instructor)
            
            with open(data, "w") as f:
                json.dump(datos, f, indent=4)
                print("Instructor registrado exitosamente.")   
        except Exception as e:
            print(f"Error: {e}")

#gestionar_instructores(data)

def asignar_instructor(data):
    print(mensaje)
    print("    Asignar instructor")
    print(mensaje)
    
    try:
        with open(data, "r") as file:
            datos = json.load(file)  
        instructores = datos.get('instructores') 
        clientes = datos.get('matriculas')    
        i = 0
        print("===== Instructores =====")
        for instructor in instructores:
            i += 1
            print(f"{i}. DPI: {instructor['dpi']}\nNombre: {instructor['nombre']}\nArea: {instructor['area']}\n") 

        print("===== Clientes Matriculados =====")
        for cliente in clientes:
            i += 1
            print(f"{i}. DPI: {cliente['dpi']}\nServicio: {cliente['servicio']}\n") 
    except Exception as e:
        print(f"Error: {e}")

    try:
        instruct = int(input("DPI instructor: "))
        client = int(input("DPI cliente: ")) 

        if len(str(instruct)) != 13 or len(str(client)) != 13:
            print("EL DPI debe tener 13 caracteres validos")
            return
    except Exception as e:
        print("Error", e)

asignar_instructor(data)