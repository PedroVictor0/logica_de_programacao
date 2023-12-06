idade = int(input("Diga sua idade em dias:"))
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30
total = (anos)
total2 = (meses)
total3 = (dias)
print(total, "anos", total2, "meses", total3, "dias")