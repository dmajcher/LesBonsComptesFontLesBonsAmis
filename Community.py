from Node import *


class Community:
	def __init__(self, community = []):
		_community = community
		_hubs = []

	def getCommunity(self):
		return self._community

	def setHubs(self):




	def __getitem__(self,key):
		return self._community[key]

	def __len__(self):
		return len(self._community)
