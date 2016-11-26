from Node import*
from Arc import*
from Cfc import*

class Graph:
	def __init__(self,fileName):
		self.__nodesNames = []
		self.__stack = []
		self.createGraph(fileName)
		self.simplific()

	def createGraph(self,fileName):
		try:
			graphFile = open(fileName)
			nodeNb = graphFile.readline()
			self.__graphOrder = int(nodeNb)
		except FileNotFoundError :                               
			raise SystemExit("Le fichier "+(fileName)+" n'existe pas.")
		for line in graphFile:
			stripedLine = line.strip().split(" ")
			firstPerson = stripedLine[0]
			secondPerson = stripedLine[1]
			debt = stripedLine[2]
			self.checkAndUpdateGraph(firstPerson,secondPerson,debt)
		for i in range(int(nodeNb)):
			print("sommet : "+self.__nodesNames[i].getName(),end="")
			self.__nodesNames[i].printArcs()

	def checkAndUpdateGraph(self,fPerson,sPerson,debt):
		fPresent = 0
		sPresent = 0
		i = 0
		while (not fPresent or not sPresent) and i< len(self.__nodesNames):
 			if not fPresent and fPerson == self.__nodesNames[i].getName():
 				fPresent = 1
 				nodeF = self.__nodesNames[i]
 			if not sPresent and sPerson == self.__nodesNames[i].getName():
 				sPresent = 1
 				nodeS = self.__nodesNames[i]
 			i+=1
		if not fPresent:
			nodeF = Node(fPerson,len(self.__nodesNames))
			self.__nodesNames.append(nodeF)
		if not sPresent:
			nodeS = Node(sPerson,len(self.__nodesNames)) 
			self.__nodesNames.append(nodeS)

		if fPresent and sPresent:
			oldDebt = debt
			debt = self.checkAndSuppressMutualDebt(nodeS,nodeF,debt)
		newArc = Arc(nodeS,debt,oldDebt)
		nodeF.addArc(newArc)

	def checkAndSuppressMutualDebt(self,nodeF,nodeS,debtSF):
		for i in range(len(nodeF.getArcs())):
			arc = nodeF.getArcs()[i]
			if arc.getExtremite() == nodeS:
				debtFS = arc.getPoids()
				arc.addOldDebt(debtFS)
				if debtFS >= int(debtSF):
					arc.setPoids(debtFS-int(debtSF))
					return 0
				else:
					arc.setPoids(0)
					return int(debtSF)-debtFS
					
		return debtSF

	def simplific(self):
		self.findCFC()
		self.saveCFC()
		self.suppressCycles()

	def findCFC(self):
		self.__id = 0
		self.__sid = 0
		self.__pre = [-1 for i in range(self.__graphOrder)]
		self.__low = [0 for i in range(self.__graphOrder)]
		self.__comp = [0 for i in range(self.__graphOrder)]
		for v in range(self.__graphOrder):
			if self.__pre[v]==-1:
				self.explore(v)
		print(self.__comp)
		for i in self.__nodesNames:
			print(i.getName(),end = " ")
		print(" ")

	def explore(self,k):
		print(" ")
		print("Nouvelle réc")
		print("Sommet: "+self.__nodesNames[k].getName())
		self.__id += 1
		self.__pre[k] = self.__id
		self.__low[k] = self.__id
		minimum = self.__id
		print("minimum in: "+ str(minimum))
		self.__stack.append(k)
		for i in self.__nodesNames[k].getArcs():
			if i.getPoids()!= 0:
				t = i.getExtremite().getPosition()
				print("Sommet suivant: "+self.__nodesNames[t].getName())
				if self.__pre[t] == -1: 
					self.explore(t)
				print("plus petit ordre sommet rencontré: "+str(self.__low[t]))
				print("minimum: "+ str(minimum))
				if self.__low[t] < minimum:
					minimum = self.__low[t]
				print("minimum after: "+ str(minimum))	
		if (minimum < self.__low[k]):
			self.__low[k]=minimum
		else:
			t = self.__stack.pop()
			self.__comp[t] = self.__sid
			self.__low[t] = 100000000
			while t!=k:
				t = self.__stack.pop()
				self.__comp[t] = self.__sid
				self.__low[t] = 100000000
			self.__sid+=1

	def saveCFC(self):
		self.__CFCs =[]
		temp = []
		for i in range (len(self.__comp)):
			if len(temp)-1 < self.__comp[i]:
				for j in range ((self.__comp[i]-(len(temp)-1))):
					temp.append([])
			temp[self.__comp[i]].append(i)
		for k in range(len (temp)):
			if len(temp[k])>1:
				tempCfc = Cfc(self.__nodesNames[temp[k][0]])
				for l in range(len(temp[k])-1):
					tempCfc.addSummit(self.__nodesNames[temp[k][l+1]])
				self.__CFCs.append(tempCfc)
				self.__CFCs[-1].printSum()
				self.__CFCs[-1].getLinkingArcs()
				self.__CFCs[-1].initMarkedList()

	def suppressCycles(self):
		for i in range(len(self.__CFCs)):
			self.__CFCs[i].suppressCycle()
		for j in range(len(self.__nodesNames)):
			print("sommet : "+self.__nodesNames[j].getName(),end="")
			self.__nodesNames[j].printArcs()	

	def identifyCommunities(self):
		for i in range(len(self.__nodesNames)):
			if not self.__inCommunity[i]:
				self.browseAndAddtoCom(self.__nodesNames[i])

	# def browseAndAddtoCom(self,currentSummit):