from Arc import*

class Node:
	def __init__(self,name,position):
		self.__name = name
		self.__arcs = []
		self.__position = position
		self.__community = None

	def addArc(self,arc):
		self.__arcs.append(arc)

	def getName(self):
		return self.__name

	def getArcs(self):
		return self.__arcs

	def getPosition(self):
		return self.__position

	def setCommunity(self,community):
		self.__community = community

	def getCommunity(self):
		return self.__community

	def isInCommunity(self):
		if self.__community != None:
			return True
		else:
			return False

	def printArcs(self):
		for i in range(len(self.__arcs)):
			print(" Extremité: "+self.__arcs[i].getExtremite().getName()+" dette: "+str(self.__arcs[i].getPoids()), end=" ")
		print("")
