'''
def main():
    arq = open("teste.txt", "w")
    arq.write("Oi\n")
    arq.write("Oi\n")
    arq.write("Oi\n")
    arq.write("Oi\n")
    arq.close()
    arq = open("teste.txt", "r")
    x = arq.read()
    print(x)
main()
'''
# .a = append .r = read  .w = write try = tente com  exept = ecessao

#
import datetime
def ler_arquivo():
    try:
        with open("registro.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print("Conteudo Atual: ")
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo ainda nao foi criado.")

#função para escrever no arquivo
def escrever_arquivo():
    with open("registro.txt", "w") as arquivo:
        mensagem = "Registro Inicial: {}".format(datetime.datetime.now)
        arquivo.write(mensagem)
        print("Registro escrito com sucesso!")

def adicionar_conteudo():
    with open("registro.txt", "a") as arquivo:
        mensagem = "Adição posterior: {}\n".format(datetime.datetime.now())
        arquivo.write(mensagem)
        print("Conteúdo adicionado com sucesso!")

#Execução do exemplo
def main():
    ler_arquivo()
    escrever_arquivo()
    adicionar_conteudo()
    ler_arquivo()

if __name__ == "__main__":
    main()