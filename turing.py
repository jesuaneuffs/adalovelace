def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
    
Cada vez que você faz uma busca simples no Google ou em qualquer outro buscador, há princípios de lógica que foram concebidos há mais de 150 anos. Foi o matemático britânico George Boole que inventou um sistema de álgebra que é chave para a programação de hoje. Durante os últimos 17 anos de sua vida, Boole estabeleceu o conceito de lógica algébrica em matemática e simplificou o mundo em enunciados básicos que tinham “sim” ou “não” como resposta, usando a aritmética básica nessa tarefa. Esse conceito, que ele introduziu em 1847 e expandiu sete anos mais tarde, é o que está presente nos programas atuais de informática. A álgebra de Boole, ou álgebra booleana, é uma estrutura algébrica que esquematiza as operações lógicas, e está presente em todas as partes: desde a programação por trás dos videogames até o código dos aplicativos e programas de computador que usamos. Certa vez, Boole disse a um amigo que a lógica booleana poderia ser a “contribuição mais valiosa, se não a única, que fiz ou que provavelmente farei à ciência, e é o motivo pelo qual desejaria ser lembrado, se é que serei lembrado, postumamente”. E assim aconteceu: os tijolos que formam a programação (os comandos ou instruções dadas a um sistema informático) são todos baseados na lógica de Boole.
