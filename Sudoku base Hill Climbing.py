import random
import numpy as np
from collections import Counter

#Sudoku (4x4)
class Sudoku:
    def __init__(self, filas, columnas):
        self.matriz = [
                  [0,2,4,0],
                  [1,0,0,3],
                  [4,0,0,2],
                  [0,1,3,0]]
        self.bloqueados=[]
        self.estados=None

    #Generate positions of sudoku estipulated numbers
    def generateNumLocked(self):
        for i in range(4):
            for j in range(4):
                if self.matriz[i][j] != 0:
                    self.bloqueados.append((i,j))

    # There are no repeated numbers per quadrant
    def UniqueSquares(self):
        NotAvailable = [0]
        for i in range(2):
            for j in range(2):
                if self.matriz[i][j] is not 0:
                    NotAvailable.append((self.matriz[i][j]))
        
        for i in range(2):
            for j in range(2):
                if self.matriz[i][j] is 0:
                    val = 0
                    while val in NotAvailable:
                        val = random.randint(1,4)
                    self.matriz[i][j]=val
                    NotAvailable.append(val)

        NotAvailable = [0]

        for i in range(2):
            for j in range(2,4):
                if self.matriz[i][j] is not 0:
                    NotAvailable.append((self.matriz[i][j]))

        for i in range(2):
            for j in range(2,4):
                if self.matriz[i][j] is 0:
                    val = 0
                    while val in NotAvailable:
                        val = random.randint(1,4)
                    self.matriz[i][j]=val
                    NotAvailable.append(val)

        NotAvailable = [0]

        for i in range(2,4):
            for j in range(2):
                if self.matriz[i][j] is not 0:
                    NotAvailable.append((self.matriz[i][j]))

        for i in range(2,4):
            for j in range(2):
                if self.matriz[i][j] is 0:
                    val = 0
                    while val in NotAvailable:
                        val = random.randint(1,4)
                    self.matriz[i][j]=val
                    NotAvailable.append(val)

        NotAvailable = [0]

        for i in range(2,4):
            for j in range(2,4):
                if self.matriz[i][j] is not 0:
                    NotAvailable.append((self.matriz[i][j]))

        for i in range(2,4):
            for j in range(2,4):
                if self.matriz[i][j] is 0:
                    val = 0
                    while val in NotAvailable:
                        val = random.randint(1,4)
                    self.matriz[i][j]=val
                    NotAvailable.append(val)

    #Printing matrix
    def printm(self, matriz):
        for i in range(4):
            for j in range(4):
                print(self.matriz[i][j], ' ', end='')
            print('\n')

    #Our heuristic counts the errors in the columns, that is, 
    #how many numbers are repeated in a row. It will only add 1 error per number.
    def CostFunctionFilas(self, matriz):
        error = 0
        number= 0
        for i in range(len(self.matriz)):
            obj = np.array(self.matriz[i])
            error = [item for item, count in Counter(obj).items() if count > 1]
            number = len(error) + number
        return number

    #Our heuristic counts the errors in the columns, that is, 
    #how many numbers are repeated in a column. It will only add 1 error per number.
    def CostFunctionColumnas(self, matriz):
        array = np.array(self.matriz)
        array = np.transpose(array)
        error = 0
        number=0
        for i in range(len(self.matriz)):
            obj = array[i]
            error = [item for item, count in Counter(obj).items() if count > 1]
            number = len(error) + number
        return number
    
    #Sum of the two cost functions(Rows + Columns)
    def CostFunction(self, matriz):
        return self.CostFunctionColumnas(matriz) + self.CostFunctionFilas(matriz)
    
    #Change two numbers inside the sudoku if it is not a fixed number
    def swap(self, matriz):
        i = random.randint(0,3)
        j = random.randint(0,3)
        ii = random.randint(0,3)
        jj = random.randint(0,3)
        pos1 = (i,j)
        pos2 = (ii,jj)

        if pos1 in self.bloqueados or pos2 in self.bloqueados:
            self.swap(matriz)
        else:
            matriz[i][j], matriz[ii][jj] = matriz[ii][jj], matriz[i][j]
            return matriz

    #HillClimbing Algorithm
    def HillClimbing(self,matriz):
        score = self.CostFunction(matriz)

        if score <= 0:
            self.printm(matriz)
            return matriz
        
        while score >= 0:
            actual = matriz
            self.swap(actual)
            nuevo_score = self.CostFunction(actual)

            if nuevo_score <= 0:
                print("Solucion: ")
                self.printm(actual)
                return actual
            elif nuevo_score < score:
                print("Iterando: ")
                self.printm(actual)
                score = nuevo_score
    

def game_loop():
    s = Sudoku(4,4)
    s.generateNumLocked()
    s.UniqueSquares()
    solve = s.HillClimbing(s.matriz)
       
#Program
game_loop()
