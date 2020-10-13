nome = input()
if len(nome)>1:
    nome.lower()
    print(f"Olá, {nome.capitalize()}!")
else:
    print(f"Olá, Mundo!")