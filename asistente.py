https://replit.com/@AndreaCuellar2/asistentepy?v=1

nombre=input("Soy tu asistente Alexa, si quieres hablar conmigo ingresa mi nombre:")
x=nombre.split()
y=x.count("Alexa")

if y==1:
    ayuda=input("Dime, ¿En que puedo ayudarte?")
while y>1:
  print("Tranquilo, solo di mi nombre una vez")
  nombre=input("Soy tu asistente Alexa, si quieres hablar conmigo ingresa mi nombre:")
  if nombre=='Alexa':
    ayuda=input("Dime, ¿En que puedo ayudarte?")
else:
  print("No te entiendo, por favor decir Alexa")
