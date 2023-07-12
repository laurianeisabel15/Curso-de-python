identidade= input("Qual é o número do seu BI?")
resultado= identidade.strip()
base de dados= {
    "004843261LA047"
    {
        "Nome":"Lauriane Vunge",
        "Cursos":["Python","Desenvolvimento Web"]
        "Computador":"Mediateca"
        }
    }
aluna=base_de_dados.get(resultado)
if aluna:
    print("aluna foi encontrada com sucesso")
    else:
        print("O BI não corresponde a nenhuma aluna")
