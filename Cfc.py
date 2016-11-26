from Node import*
from Arc import*

class Cfc:

	def __init__(self,firstSummit):
		self.__cfcSummits = [firstSummit]
		self.__lowestDebt = float("inf")

	def addSummit(self,summit):
		self.__cfcSummits.append(summit)

	def printSum(self):
		for i in range(len(self.__cfcSummits)):
			print(self.__cfcSummits[i].getName())

	def initMarkedList(self):
		self.__markedList = [False for i in range(len(self.__cfcSummits))]

	def getLinkingArcs(self):
		self.__arcsBySum = []
		for i in range(len(self.__cfcSummits)):
			self.__arcsBySum.append([])
			currentSummitArcs = self.__cfcSummits[i].getArcs()
			for j in range(len(currentSummitArcs)):
				if currentSummitArcs[j].getPoids() != 0 and currentSummitArcs[j].getExtremite() in self.__cfcSummits:
					self.__arcsBySum[i].append(currentSummitArcs[j])
					if int(currentSummitArcs[j].getPoids()) < self.__lowestDebt:
						self.__lowestDebt = int(currentSummitArcs[j].getPoids())
						self.__startingArc = currentSummitArcs[j]
						self.__startingSummitIndex = i
		# print(self.__arcsBySum)
		# for m in range(len(self.__cfcSummits)):
		# 	print(self.__cfcSummits[m].getName(),end=" ")
		# print(self.__lowestDebt)
		# print(self.__startingSummitIndex)
		# print(self.__startingArc.getExtremite().getName())


	def suppressCycle(self,currentSummitIndex = None):
		if currentSummitIndex == None:
			currentSummitIndex=self.__startingSummitIndex
		if currentSummitIndex == self.__startingSummitIndex and self.__markedList[currentSummitIndex]:
			return 1
		elif self.__markedList[currentSummitIndex]:
			return 0
		else:
			self.__markedList[currentSummitIndex] = True
			for i in range(len(self.__arcsBySum[currentSummitIndex])):
				print("Sommet de départ: "+self.__cfcSummits[currentSummitIndex].getName()+" sommet d'arrivée: "+self.__arcsBySum[currentSummitIndex][i].getExtremite().getName())
				isOver = self.suppressCycle(self.__cfcSummits.index(self.__arcsBySum[currentSummitIndex][i].getExtremite()))
				if isOver:
					self.__arcsBySum[currentSummitIndex][i].substrToPoids(self.__lowestDebt)
					return 1
			return 0



		