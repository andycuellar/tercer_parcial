https://replit.com/@AndreaCuellar2/ollivanderspy?v=1

cliente = str(input("¿Entra un nuevo cliente?"))

while cliente == "sí" or cliente == "si":
  varitas = str(input("¿Compro varita? "))
  tipo = str(input("Tipo de varita"))
  if tipo == "Varita de sáuco":
    print("Varita de sáuco")
  if tipo == "Varita de espino":
    print("Varita de espino")
  if tipo == "Varita de sauce":
    print( "Varita de sauce")
  if tipo == "Varita de acebo":
    print("Varita de acebo")
    
  cliente = str(input("¿Entro un nuevo cliente?"))
