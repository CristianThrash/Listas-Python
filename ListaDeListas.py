'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna una lista cuyo unico elemento es el menor de los elementos de la lista entregada.'''
def retornarMenor(lista):
    if len(lista)==1:
        return lista[:1]
    elif(lista[0]<lista[-1]):
        return retornarMenor(lista[:-1])
    else:
        return retornarMenor(lista[1:])

'''Retorna una lista con el menor elemento de cada lista ingresada.'''
def retornarMenores(listaDeListas):
    if(len(listaDeListas)==1):
        return retornarMenor(listaDeListas[0])
    else:
        return retornarMenor(listaDeListas[0])+retornarMenores(listaDeListas[1:])
    
numeroListas = input("Cuantas listas desea?: ")
listaListas = range(numeroListas)

for i in listaListas:
    numero = input("Cuantos numeros desea en la lista "+str(i+1)+"?: ")
    listaListas[i] = range(numero)
    for j in listaListas[i]:
        listaListas[i][j] = input("Digite un numero ")
        
print "los menores de cada lista son: " + str(retornarMenores(listaListas))
