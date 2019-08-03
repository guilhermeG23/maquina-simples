#Python3

from time import sleep

#Máquina-virtual-simples em code

#Modelo de 5 camadas simples

#Variaveis
global entrada_teclado
cache_teclado = []
memoria = []
cache_cpu = []
registrador = []
memoria_retorno = 0

#Funcoes

#teclado
def teclado():
    for i in range(0,4):
        print("Entre com o valor {} de 4".format(i + 1))
        entrada = int(input("Entre com o valor a operar(1/0): "))
        cache_teclado.append(entrada)

#Ram
def memoria_ram(cache_teclado):
    for i in range(0, len(cache_teclado)):
        memoria.append(cache_teclado[i])
    cache_teclado.clear()

#Escrevendo na RAM
def memoria_ram_retorno(entrada):
    return entrada

#Cache
def cache(memoria):
    for i in range(0, len(memoria)):
        cache_cpu.append(memoria[i])

#Registrador
def registradores(cache):
    for i in range(0, len(cache_cpu)):
        registrador.append(cache_cpu[i])

#ULA
#Unica funcao registrada na ULA e a de soma
def ULA(registrador):
    operador = str(registrador[0]) + str(registrador[1])
    
    if operador == "00":
        valor = "None"
    elif operador == "01":
        if registrador[2] == 0 and registrador[3] == 0:
            valor = 0             
        elif registrador[2] == 0 and registrador[3] == 1:
            valor = 0             
        elif registrador[2] == 1 and registrador[3] == 0:
            valor = 0             
        elif registrador[2] == 1 and registrador[3] == 1:
            valor = 1
        else:
            valor = 0
    elif operador == "10":
        if registrador[2] == 0 and registrador[3] == 0:
            valor = 0             
        elif registrador[2] == 0 and registrador[3] == 1:
            valor = 1             
        elif registrador[2] == 1 and registrador[3] == 0:
            valor = 1             
        elif registrador[2] == 1 and registrador[3] == 1:
            valor = 1
        else:
            valor = 0
    elif operador == "11":
        if registrador[2] == 0 and registrador[3] == 0:
            valor = 0             
        elif registrador[2] == 0 and registrador[3] == 1:
            valor = 1             
        elif registrador[2] == 1 and registrador[3] == 0:
            valor = 1             
        elif registrador[2] == 1 and registrador[3] == 1:
            valor = 0
        else:
            valor = 0
    else:
        valor = 0            

    return valor

#Sleep no sistema
#Simulando o tempo que leva para processar uma instrução de um nivel para outro
def dormir(tempo):
    sleep(tempo)

#Pausar completo
def pausar():
    input()

#Mensagem de entrada
def mensagem(frase):
    print("\n")
    print("=-"*20)    
    print(frase)
    print("=-"*20)
    
#Programa
def funcao_principal():
    try:
        mensagem("Simulando uma simples máquina de 4 bits multinível de 6 camadas!")
        dormir(1)
        mensagem("Demonstrando o fluxo de uma execução de um programa!")
        mensagem("Camada - 6 -> Auto nível -> Nível de usuário")
        dormir(1)
        mensagem("Explicação simples do programa:\n1->Entre com 0/1\n2->Entre com o operador\n3->Ex: 0010-> 00 -> operador -> 1 -> primeiro valor -> 0 -> segundo valor!\n\nTipos de operação: \n00 -> Não fazer nada\n01 -> AND\n10 -> OR\n11 -> XOR")
        dormir(1)
        teclado()
        dormir(1)
        pausar()
        mensagem("Camada - 5 -> Baixo nível")
        dormir(1)
        pausar()
        mensagem("Camada - 4 -> S.O")
        dormir(1)
        pausar()
        mensagem("Camada - 3 -> Conjunto de instruções -> Fornecido pelo fabricante")
        memoria_ram(cache_teclado)
        dormir(1)
        pausar()
        mensagem("Camada - 2 -> Firmware -> Microprogramas e microinstuções")
        dormir(1)
        pausar()
        mensagem("Camada - 1 -> Hardware -> Microarquitetura")
        dormir(1)
        pausar()
        cache(memoria)
        registradores(cache)
        processo = ULA(registrador)
        pausar()
        dormir(1)
        mensagem("Camada - 2 -> Firmware -> Microprogramas e microinstuções")
        pausar()
        dormir(1)
        mensagem("Camada - 3 -> Conjunto de instruções -> Fornecido pelo fabricante")
        memoria_retorno = processo
        pausar()
        dormir(1)
        mensagem("Camada - 4 -> S.O")
        pausar()
        dormir(1)
        mensagem("Camada - 5 -> Baixo nível")
        pausar()
        dormir(1)
        mensagem("Camada - 6 -> Auto nível -> Nível de usuário")
        mensagem("O valor processado tem a saída de {}".format(memoria_retorno))
    except KeyboardInterrupt:
        mensagem("Finalizando máquina")
        exit()

#main
if __name__ == "__main__":
   funcao_principal()