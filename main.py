#Neste começo do codigo eu dou as boas vindas ao usuario e lhe explico como parar o programa
print("---Calculadora Notas---\n")
print("Digite *0* para finalizar a qualquer momento")
#Crio uma função para somar notas dos alunos
def somar_notas(notas_alunos):
    soma = 0
    for nota in notas_alunos:
        soma += nota
    return soma
#Agora crio a minha lista e o meu loop para solicitar ao usuario as notas uso o .append para adicionar a ultima nota sempre no final
#Caso o usuario digite 0 entra em um if que para o loop
notas = []
while(True):
    entrada_nota = float(input("Insira as notas dos alunos: "))
    if entrada_nota == 0:
        break
    notas.append(entrada_nota)
#Agora faço um if para verificar se o número é maior que 0 para não ocorrer erro de divisão por 0
if len(notas) > 0:
    #Uso a função para armazenar os dados em uma variavel
    soma_notas = somar_notas(notas)
    #Calculo a media dos alunos
    media = soma_notas / len(notas)
    #Agora faço a verificação a situação do aluno
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    #Nessa parte final do codigo mostro ao usuario o resultado do aluno
    print("\n---Resultado---\n")
    print(f"Notas do aluno {notas}")
    print(f"Media do aluno {media:.2f}")
    print(f"Situação do aluno {situacao}")
    #Esse else caso o usuario digite 0 logo de inicio mostra ao usuario que nenhuma nota foi inserida.
else:
    print("Nenhuma nota inserida")