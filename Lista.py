'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''
# Actualización
'''Retorna la suma de los elementos de una lista de enteros dada'''
def sumarLista(lista):
    if(lista==[]):
        return 0
    else:
        return lista[0]+sumarLista(lista[1:])
    
'''Retorna la lista entregada invertida'''
def invertir(lista):
    if(len(lista)==1):
        return lista
    else:
        return lista[-1:]+invertir(lista[:-1])
    
numero = input("Cuantos numeros desea en la lista: ")
lista = range(numero)
for i in lista:
    lista[i] = input("Digite un numero ")

opcion = input("1 - Invertir lista\n2 - Sumar elementos\n Seleccione una opcion: ")
if(opcion==1):
    print invertir(lista)
elif(opcion==2):
    print sumarLista(lista)
