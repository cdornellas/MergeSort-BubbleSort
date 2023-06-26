import random # importa a função para gerar números aleatórios
import time # importa a função para medir o tempo de execução dos algoritmos
import matplotlib.pyplot as plt # importa a biblioteca para a criação de gráficos

# Algoritmo merge sort
def mergeSort(vetor):
    #Verifica se o tamanho do vetor é maior ou igual a 1
    if len(vetor) <= 1:
        return vetor

    #Divide o vetor ao meio
    meio = len(vetor) // 2
    esquerda = vetor[:meio]
    direita = vetor[meio:]

    # Chama o merge sort para cada metade
    esquerda = mergeSort(esquerda)
    direita = mergeSort(direita)

    # Combina as duas metades 
    return merge(esquerda, direita)

 # Combina dois subvetores em um único vetor ordenado
def merge(esquerda, direita):
    result = []
    i = j = 0

    # Percorre as duas metades, comparando-as e adicioando elementos em um vetor ordenado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            result.append(esquerda[i])
            i += 1
        else:
            result.append(direita[j])
            j += 1

    # Adiciona os elementos restantes da metade que não foi totalmente percorrida
    result.extend(esquerda[i:])
    result.extend(direita[j:])

    return result


# Algoritmo bubble sort
def bubbleSort(vetor):
    n = len(vetor)
    for i in range(n):
        troca = False
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                troca = True
        if not troca:
            break

# Definindo os tamanhos dos vetores
tamanhos = [50, 500, 5000, 50000]

# Cria vetor de ordem aleatória no tamanho do vetor
def aleatorio(tamanho):
    vetorAleatorio = random.sample(range(tamanho), tamanho)
    return vetorAleatorio

# Cria vetor em ordem crescente
def crescente(tamanho):
    vetorCrescente = list(range(tamanho))
    return vetorCrescente

# Cria vetor em ordem decrescente
def decrescente(tamanho):
    vetorDecrescente = list(range(tamanho, 0, -1))
    return vetorDecrescente

def analiseAlgoritmo(algoritmo, ordem):
    tempo = []
    for tamanho in tamanhos:
        vetor = ordem(tamanho)
        inicio = time.time()
        algoritmo(vetor)
        fim = time.time()
        execucao = fim - inicio
        tempo.append(execucao)
    return tempo

# Gerador de gráfico
def gerarGrafico(tamanhos, tempoMerge, tempoBubble, titulo):
    plt.plot(tamanhos, tempoMerge, marker='o', color='red', label='Merge-Sort')
    plt.plot(tamanhos, tempoBubble, marker='o', color='blue', label='Bubble-Sort')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Tempo (segundos)')
    plt.title(titulo)
    plt.legend()
    plt.show()

# Análise para vetores em ordem crescente
tempoMerge = analiseAlgoritmo(mergeSort, crescente)
tempoBubble = analiseAlgoritmo(bubbleSort, crescente)
gerarGrafico(tamanhos, tempoMerge, tempoBubble, "Análise de Vetores de Números Inteiros em Ordem Crescente")

# Análise para vetores em ordem decrescente
tempoMerge = analiseAlgoritmo(mergeSort, decrescente)
tempoBubble = analiseAlgoritmo(bubbleSort, decrescente)
gerarGrafico(tamanhos, tempoMerge, tempoBubble, "Análise de Vetores de Números Inteiros em Ordem Decrescente")

# Análise para vetores em ordem aleatória
tempoMerge = analiseAlgoritmo(mergeSort, aleatorio)
tempoBubble = analiseAlgoritmo(bubbleSort, aleatorio)
gerarGrafico(tamanhos, tempoMerge, tempoBubble, "Análise de Vetores de Números Inteiros em Ordem Aleatória")