import math
import time
import random
import timeit

def seleção(x):
    n=len(x)
    t = time.time()
    for i in range(0,n-1):
        minimo=i
        for j in range(i+1,n):
            if(x[j]<x[minimo]):
                minimo=j
        x[i],x[minimo]=x[minimo],x[i]

    t2 = time.time()
    return("%.2f"%(t2-t))

def nativo(x):
    t = time.time()
    x.sort()
    t2 = time.time()
    return("%.2f"%(t2-t))

def merge(esquerda, direita, x):
  i = 0
  j = 0
  k = 0
 
  while (i<len(esquerda) and j<len(direita)):
    if(esquerda[i]<direita[j]):
      x[k] = esquerda[i]
      i = i+1
    else:
      x[k] = direita[j]
      j = j+1
 
    k = k+1
  
  while(i<len(esquerda)):
    x[k] = esquerda[i]
    i = i+1
    k = k+1
  
  while(j<len(direita)):
    x[k] = direita[j]
    j = j+1
    k = k+1
        
def mergesort(x):
  n = len(x)
  if(n<2):
    return
 
  mid = n//2
  esquerda = []
  direita = []
  
  for i in range(mid):
    num = x[i]
    esquerda.append(num)  
   
  for i in range(mid,n):
    num = x[i]
    direita.append(num)
 
  mergesort(esquerda)
  mergesort(direita)
 
  merge(esquerda,direita,x)

def temp_merge(x):
    t = time.time()
    mergesort(x)
    t2 = time.time()
    return("%.2f"%(t2-t))

def temp_quick(x):
    t = time.time()
    quicksort(x,0,len(x)-1)
    t2 = time.time()
    return("%.2f"%(t2-t))
 
def quicksort(A, esquerda, direita):
    if esquerda < direita:
        indice_pivo = particao(A, esquerda, direita)
        quicksort(A, esquerda, indice_pivo - 1)
        quicksort(A, indice_pivo + 1, direita)
        
def particao(A, esquerda, direita):
    i = esquerda
    j = direita
    while i <= j:
        while A[i] <= A[esquerda]:
            i += 1
            if i == direita:
                break

        while A[esquerda] <= A[j]:
            j -= 1
            if j == esquerda:
                break
        
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
    
    A[esquerda], A[j] = A[j], A[esquerda]
    return j

i = 0
lista = []

print('----------------------------------------------')
print('          |          tempo(s)                |')
print('----------------------------------------------')
print('          | merge  quick  selection   native |')

while i < 11:
    lista_aux =random.sample(range(1,20000), 2000)
    lista = lista +lista_aux
    random.shuffle(lista)
    lista1 = lista+[]
    lista2 = lista+[]
    lista3 = lista+[]
    lista4 = lista+[]
    
    if(len(lista) >= 10000):
        n_s = seleção(lista3)
        if(float(n_s)<10):
            print('%d     | %s    %s     %s     %s   |'%(len(lista),temp_merge(lista1),temp_quick(lista2),n_s,nativo(lista4)))
        else:
            print('%d     | %s    %s     %s    %s   |'%(len(lista),temp_merge(lista1),temp_quick(lista2),n_s,nativo(lista4)))
        i +=1
        continue
    
    print('%d      | %s    %s     %s     %s   |'%(len(lista),temp_merge(lista1),temp_quick(lista2),seleção(lista3),nativo(lista4)))
    i+=1
    
print('----------------------------------------------')
