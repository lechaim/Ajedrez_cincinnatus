board = ["TN1","CN1","AN1","KiN","QuN","AN2","CN1","TN2",
		 "AN1","AN2","AN3","AN4","AN5","AN6","AN7","AN8",
		 "   ","   ","   ","   ","   ","   ","   ","   ", 
		 "   ","   ","   ","   ","   ","   ","   ","   ",
		 "   ","   ","   ","   ","   ","   ","   ","   ",
		 "   ","   ","   ","   ","   ","   ","   ","   ",
		 "AB1","AB2","AB3","AB4","AB5","AB6","AB7","AB8",
		 "TB1","CB1","AB1","KiB","QuB","AB2","CB1","TB2"]

def displayBoard():

	counter = 0

	numero = ["1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 "]

	display_board = "    A    B    C    D    E    F    G    H\n" + "0 "

	for e in range(len(board)):
		
		if e > 0 and e % 8 == 0:
			display_board += "\n" +numero[counter]
			counter += 1 

		display_board += "{}{}{}".format("[",board[e],"]")

	return display_board



print(displayBoard())