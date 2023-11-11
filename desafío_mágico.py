https://replit.com/@AndreaCuellar2/desafio-magico?v=1

gryffindor_score=0
slytherin_score=0
while True:
  quidditch_events=input("Ingresa un evento (goal/snitch/foul)").lower()
  if quidditch_events=="goal":
   equipo=input("¿Qué equipo anotó? (Gryffindor o Slytherin").lower()
    if equipo=="gryffindor":
      gryffindor_score+=10
      print("El equipo Gryffindor anotó un gol, gana 10 puntos!")
    elif equipo=="slytherin":
      slytherin_score+=10
      print("El equipo Slytherin anotó un gol, gana 10 puntos!")
    elif quidditch_events=="snitch":
      equipo=input("¿Qué equipo anotó? (Gryffindor o Slytherin").lower()
    if equipo=="gryffindor":
      gryffindor_score+=150
      print("El equipo Gryffindor anotó un snitch, gana 150 puntos!")
    elif equipo=="slytherin":
      slytherin_score+=150
      print("El equipo Slytherin anotó un snitch, gana 150 puntos!")
    elif quidditch_events=="foul":
      equipo=input("¿Qué equipo anotó? (Gryffindor o Slytherin").lower()
    if equipo=="gryffindor":
      gryffindor_score+=30
      print("El equipo Gryffindor anotó un falta, gana 30 puntos!")
    elif equipo=="slytherin":
      slytherin_score+=30
      print("El equipo Slytherin anotó un falta, gana 30 puntos!")
