class Community:

	def __init__(self,summit,cumminityId):
		self.__summits = [summit]
		self.__communityId = cumminityId

	def __add__(self,secCom):
		return self.__summits + secCom.getSummits()

	def addSummit(self,summitToAdd):
		self.__summits.append(summitToAdd)

	def getSummits(self):
		return self.__summits

	def getCommunityId(self):
		return self.__communityId