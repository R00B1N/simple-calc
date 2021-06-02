#!/usr/bin/python3

from colorama import Fore, init
import pyinputplus as pyip
import os
init()


"""
Trabajando con clases, metodos y objetos
"""

banner = """
 ######     ###    ##        ######  
##    ##   ## ##   ##       ##    ## 
##        ##   ##  ##       ##       
##       ##     ## ##       ##       
##       ######### ##       ##       
##    ## ##     ## ##       ##    ## 
 ######  ##     ## ########  ######  

"""

def inicio():
	print(Fore.BLUE)
	print(banner)
	print(Fore.GREEN)
	print("\n\t\tBy Blackster")
	menu = """
************** Menu *************

1-> Sumar
2-> Restar
3-> Multiplicar
4-> Dividir

99->> Salir

"""
	print(Fore.YELLOW)
	print(menu)


"""
Creamos la clase para nuestra calculadora.
"""

class Calculadora():
	def __init__(self):
		self.n1 = int(input("Introduce un numero: "))
		self.n2 = int(input("Introduce otro numero: "))


if __name__=="__main__":
	while True:
		os.system('clear')
		inicio()
		ask = int(input("Escoge una opcion: "))
		if ask==1:
			sumar = Calculadora()
			print("\nLa suma de los numeros es igual a: ", sumar.n1 + sumar.n2)
			print("\nPresione una tecla para continuar*.*")
			input()

		elif ask==2:
			restar = Calculadora()
			print("\nLa resta de los numeros es igual a: ", restar.n1 - restar.n2)
			print("\nPresione una tecla para continuar*.*")
			input()

		elif ask==3:
			multi = Calculadora()
			print("\nEl resultado de la multiplicacion es: ", multi.n1 * multi.n2)
			print("\nPresione una tecla para continuar*.*")
			input()

		elif ask==4:
			div = Calculadora()
			print("\nEl resultado de la division es igual a: ", int(div.n1 / div.n2))
			print("\nPresione una tecla para continuar*.*")
			input()

		else:
			if ask==99:
				exit = pyip.inputYesNo("Esta seguro que desea salir? (y/n): ")
				if exit=='yes':
					print("See you...")
					break
				else:
					inicio()