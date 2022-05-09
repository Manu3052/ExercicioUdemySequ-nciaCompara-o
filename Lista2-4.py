from fileinput import close
print(
    "         TABELA"
    "\n 1 - Lê o arquivo x"
    "\n 2 - Imprime o arquivo x"
    "\n 3 - Sair do progama"
)

resposta = int(input("O que deseja? "))

arquivox = open("arquivox.txt", "a")
arquivox.write("\nSaudoso amigo")
close()

while resposta != 3:
    if resposta == 1:
        arquivox = open("arquivox.txt", "r")
        lerarquivo = arquivox.readline()
    elif resposta ==2:
        arquivox = open("arquivox.txt", "r")
        imprime = arquivox.readline()
        print(imprime)
    else:
        print("Opção inexistente")