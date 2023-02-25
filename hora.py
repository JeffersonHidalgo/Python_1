
#Preguntar al usuario el número de horas trabajadas
horas_trabajadas = float(input("¿Cuántas horas has trabajado? "))

#Preguntar al usuario el coste por hora
coste_hora = float(input("¿Cuál es el coste por hora? "))

#Calcular la paga
paga = horas_trabajadas * coste_hora

#Mostrar por pantalla la paga
print("Tu paga es:", paga, "euros")