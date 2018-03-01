### Hash code ###

class Road():
	def __init__(self,nr,start_inter_r, start_inter_c,_finish_inter_r,finish_inter_c,earliset_start,finish,bonus):
		self.nr = nr
		self.start_position = [start_inter_r,start_inter_c]
		self.finish_position = [_finish_inter_r,finish_inter_c]
		self.start_time = earliset_start
		self.finish_time = finish
		self.length = abs(start_inter_r-_finish_inter_r)+abs(finish_inter_c-start_inter_c)
		self.max=self.length+bonus
'''
	def __repr__(self):
		return str(self.nr)+str(self.start_position)

	def number(self):
		return self.nr

	def length(self):
		return self.length

	def max(self):
		return self.max

	def start_position(self):
		return self.start_position

	def start_time(self):
		return self.start_time

	def finish_time(self):
		return self.finish_time

	def finish_position(self):
		return self.finish_position
'''
class Car():
	def __init__(self):
		self.position=[0,0]
		self.free=True
		self.roads=[]
		self.free_in=0

data = open("input.txt","r")

data_in = [dates.split() for dates in data.read().splitlines()]

for i in range(len(data_in)):
	data_in[i] = [int(data_in_row) for data_in_row in data_in[i]]

general = data_in[0]
roads = data_in[1:]

rows = general[0]
cols = general[1]
vehicles = [[] for i in range(int((general[2])))]
rides = general[3]
bonus = general[4]
print(bonus)
steps = general[5]


for i in range(len(roads)):
	roads[i]=Road(i,roads[i][0],roads[i][1],roads[i][2],roads[i][3],roads[i][4],roads[i][5],bonus)
	print(roads[i].max)

cars=[]

for i in range(general[2]):
	cars.append(Car())

for i in range(steps):
	continue

