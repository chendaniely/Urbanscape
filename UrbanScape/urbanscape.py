'''
UrbanScape v2.0

Module for UrbanScape substrate class definition

Author: Niels Bantilan
'''

import numpy as np
import matplotlib.pyplot as pyplot
import set_distribution as setdist

class UrbanScape(object):

	#class variables: hard-coded variables
	population_per_block = 20

	def __init__(self, size, rent_floor, rent_ceiling, create_rule=None, setDist=setdist.random_distribution):
		
		blocks = np.ones( (size,size) ) #a reference variable for defining block-related variables
		err = 0.1

		#instance variables relating to baseline UrbanScape attributes
		self.time = 0
		self.size = size
		self.rent_ceiling = rent_ceiling
		self.rent_floor = rent_floor
		#self.rent = np.ones_like(blocks) * self.rent_ceiling #by default set to rent_ceiling, modified by set distribution functions
		self.rent = np.ones_like(blocks) * self.rent_ceiling
		setDist(self) ; setdist.apply_variation(self) #applies rent distribution and random variation

		#instance variables relating to agents
		self.agents = [] #a list of all agents in urbanscape
		self.create_rule = create_rule #rule for creating agents in UrbanScape
		self.agent_locations = np.zeros( (self.size, self.size) ) # an array shaped nxn of agent locations
		self.agent_coords = {} # dictionary for keeping track of agents coordinates

		#instance variables relating to implicit underlying population
		rand_error = np.random.uniform( (1 - err), (1 + err), (self.size, self.size) )
		self.income = np.ones_like(blocks) * self.rent * 4 * rand_error #income is 4 times the rent, with error_range variability
		## add random error to income distribution ##

		#instance variables relating to underlying population at the block level
		self.externalities = np.zeros_like(blocks) #total count of exposure to negative externality
		self.ffexposure = np.zeros_like(blocks) #exposure to fast food at time 't' 
		self.gsexposure = np.zeros_like(blocks) #exposure to grocery store at time 't'
		self.work_ability = np.ones_like(blocks) #the ability of block residents to work
		self.food_away = np.ones_like(blocks) #income spent on food away from home
		self.fast_food = np.ones_like(blocks) #income spent on fast food
		self.grocery = np.ones_like(blocks) #income spent on groceries


if __name__ == "__main__":
	u = UrbanScape(3, 5000, 200000)
	print "\n\nRent\n-----\n", u.rent
	print "\n\nIncome\n-----\n", u.income
	print "\n\nAgent Locations\n------------\n", u.agent_locations, "\n\n"