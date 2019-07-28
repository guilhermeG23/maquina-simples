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

#Cache
def cache(memoria):
    for i in range(0, len(memoria)):
        cache_cpu.append(memoria[i])

#Registrador
def registradores(cache):
    for i in range(0, len(cache_cpu)):
        registrador.append(cache_cpu[i])

#ULA
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
def dormir(tempo):
    sleep(tempo)

#Pausar completo
def pausar():
    input("Aperte <enter> para continuar...")

#Mensagem de entrada
def mensagem(frase):
    print("\n")
    print("=-"*20)    
    print(frase)
    print("=-"*20)
    
#Programa
def funcao_principal():
    try:
        mensagem("Simulando uma simples máquina de 4 bits multinível de 5 camadas!")
        dormir(1)
        mensagem("Demonstrando o fluxo de uma execução de um programa!")
        mensagem("Camada - 5")
        dormir(1)
        mensagem("Explicação simples do programa:\n1->Entre com 0/1\n2->Entre com o operador\n3->Ex: 0010-> 00 -> operador -> 1 -> primeiro valor -> 0 -> segundo valor!\n\nTipos de operação: \n00 -> Não fazer nada\n01 -> AND\n10 -> OR\n11 -> XOR")
        dormir(1)
        teclado()
        dormir(1)
        pausar()
        mensagem("Camada - 4")
        pausar()
        mensagem("Camada - 3")
        memoria_ram(cache_teclado)
        dormir(1)
        pausar()
        mensagem("Camada - 2")
        pausar()
        mensagem("Camada - 1")
        pausar()
        cache(memoria)
        registradores(cache)
        processo = ULA(registrador)
        mensagem("O valor processado tem a saida de {}".format(processo))
    except KeyboardInterrupt:
        mensagem("Finalizando máquina")
        exit()

#main
if __name__ == "__main__":
   funcao_principal()