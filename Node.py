from Arc import*

class Node:
	def __init__(self,name,position):
		self.__name = name
		self.__arcs = []
		self.__position = position

	def addArc(self,arc):
		self.__arcs.append(arc)

	def getName(self):
		return self.__name

	def getArcs(self):
		return self.__arcs

	def getPosition(self):
		return self.__position

	def printArcs(self):
		for i in range(len(self.__arcs)):
			print(" Extremité: "+self.__arcs[i].getExtremite().getName()+" dette: "+str(self.__arcs[i].getPoids()), end=" ")
		print("")
