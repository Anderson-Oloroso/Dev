import json

data = "gym_data.json"
riesgos = ["Alto", "Medio", "Bajo"]

def registrar_clientes(data):
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




