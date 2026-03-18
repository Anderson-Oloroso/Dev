import json

data = "gym_data.json"
riesgos = ["Alto", "Medio", "Bajo"]

def registrar_clientes(data):
    try:
        dpi = int(input("DPI: "))
        nombre = input("Nombre: ")
        riesgo = input("Riesgo (Alto, Medio, Bajo): ")
    except Exception as e:
        print(f"Error de entrada: {e}")
        return

    if riesgo not in riesgos:
        print("Riesgo no válido. Por favor, ingrese Alto, Medio o Bajo.")
    elif not nombre.strip():
        print("Nombre no puede estar vacío.")
    elif dpi != 13:
        print("DPI debe tener 13 dígitos. Intente nuevamente.")
    else:
        print("Cliente registrado exitosamente.")

    try:
        cliente = {
            "DPI": dpi,
            "Nombre": nombre,
            "Riesgo": riesgo
        }
        with open(data, "r") as file:
            clientes = json.load(file)

        for doc in clientes:
            print(doc['dpi'])
            if dpi == doc['dpi']:
                print("DPI ya registrado. No se puede registrar el cliente.")
                break
            
        clientes.append(cliente)
    except Exception as e:
        print(f"Error con el archivo: {e}")

    try:
        with open(data, "w") as f:
            json.dump(clientes, f, indent=4)
    except Exception as e:
        print(f"Error con el archivo: {e}")

registrar_clientes(data)


