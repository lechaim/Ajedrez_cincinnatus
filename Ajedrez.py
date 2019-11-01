class Trebejo:  #Trebejo es el nombre de las piezas con las que se juega ajedrez
	#def __init__ ():
	#	pass
	def move(self, symbol, movement):
		print("Do nothing")

class Rey(Trebejo):
	pass

class Reina(Trebejo):
	pass

class Torre(Trebejo):
	pass

class Alfil(Trebejo):
	pass

class Caballo(Trebejo):
	pass

class Peon(Trebejo):
	pass

class Tablero:
	#def __init__ (self):
		


	def mostrar_tabla():
		numero = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ",]
		letra = ["    a", "    b","    c","    d","    e","    f","    g","    h" ]
		columna = 1
		viga = 1

		imprimir_letra = "  "
		for l in letra:
			imprimir_letra+= l + "   "


		print(imprimir_letra)

		# Counting every piece from left to right
		board = [[["TN1"],["CN1"],["AN1"],["KiN"],["QuN"],["AN2"],["CN1"],["TN2"]],
				[["AN1"],["AN2"],["AN3"],["AN4"],["AN5"],["AN6"],["AN7"],["AN8"]],
				[[],[],[],[],[],[],[],[]],
				[[],[],[],[],[],[],[],[]],
				[[],[],[],[],[],[],[],[]],
				[[],[],[],[],[],[],[],[]],
				[["AB1"],["AB2"],["AB3"],["AB4"],["AB5"],["AB6"],["AB7"],["AB8"]],
				[["TB1"],["CB1"],["AB1"],["KiB"],["QuB"],["AB2"],["CB1"],["TB2"]]]

		for e in range (8):
			stored = ""
			for a in range (8):
				if a == 0:
					stored += numero[e] + " "

				if len(board[e][a]) == 0:
					stored += "[     ]" + " "
				else:
					stored += str(board[e][a]) + " "

				if a == 7:
					print(stored)
	


Tablero.mostrar_tabla()


#rama test
#rama continuin test








''' -----------------################## INFORMACION DE LOS TREBEJOS #################-----------------------
Un trebejo tiene forma
Un trebejo se mueve
Un trebejo  come

Trebejo (forma, movimiento, direccion en la que come, numero de fichas en el juego)

rey = R , 1 hacia cualquier cuadro, donde caiga, 1
dama = D, donde quiera, donde caiga, 1
torre = T, forma de cruz (vertical y horizontal), donde caiga, 2
alfil = A, forma de cruz (diagonales), en donde caiga, 2
caballo = C, forma de L a tres cuadros, encima de donde caiga, 2
peon = P, si está en posicion inicial puede hacer un paso o dos de lo contrario solo uno, 8




Se llamará a cada ficha con una letra y un numero. Ejemplo: P1, P2, *P1, *P2

	-----------------################## INFORMACION DE LOS TREBEJOS #################----------------------- '''

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\



''' -----------------################## INFORMACION DE LA TABLA #################-----------------------

8x8 lista
De a-h (horizontal)
de 1-8 (vertical)
	-----------------################## INFORMACION DE LA TABLA #################----------------------- '''


