seconds = int(input("Segundos"))
days = seconds // 86400
remainder_days = seconds % 86400
hours = remainder_days // 3600
remainder_hours = seconds % 3600
minutes = remainder_hours // 60
seconds = remainder_hours % 60
print(days,"dias,",hours,"horas,",minutes,"minutos e",seconds,"segundos")
