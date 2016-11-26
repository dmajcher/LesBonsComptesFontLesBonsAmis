
class Arc:
	def __init__(self,extremite,debt,oldDebt=None):
		self.__extremite = extremite
		self.__poids = int(debt)
		self.__oldDebt =[]
		if oldDebt != None:
			self.oldDebt.append(oldDebt)
	
	def getPoids(self):
		return self.__poids

	def getExtremite(self):
		return self.__extremite

	def addOldDebt(self,oldDebt):
		self.__oldDebt.append(oldDebt)

	def setPoids(self,poids):
		self.__poids = poids

	def substrToPoids(self,toSub):
		self.addOldDebt(self.poids)
		self.__poids -= toSub