diccionario={}
datos={1:"colombia",
       2:"Ecuador",
       3:"venezuela"}

datos={"Documento": 10224564,
      "Nombre": "Ricardo Jorge",
      "celular":[310557634],
      "correo":"ricardoj@gmail.com",
      "Deporte favorito": {1:"Natacion",2:"Futbol"}
      }

print(data.keys())
print(data.values())
print(data.items())
data["edad"] = 20
data["nombre"] = "Diego"
print(data)

for i in datos.values():
    print(i)