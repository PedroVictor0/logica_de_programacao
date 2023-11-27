duração_em_segundos = int(input('digite o tempo de duração em segundos do evento na fábrica:'))
horas = duração_em_segundos // 3600
minutos = (duração_em_segundos % 3600) // 60
segundos = duração_em_segundos % 60
print(horas, ":", minutos, ":", segundos )