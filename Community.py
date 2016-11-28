class Community:
	def __init__(self, community = []):
		_comunity = community

	def getCommunity(self):
		return self._comunity

	def __getitem__(self,key):
		return self._comunity[key]
		
	def __len__(self):
		return len(self._comunity)
