from module.init import *

#Maps are made of blocks
#Block has 3 overlapping layers: 1-ground, 2-middle and 3-overlap
#When one layer is EMPTY then the underlying layer becomes visible
class Block():
	def __init__(self, ground=EMPTY, middle=EMPTY, overlap=EMPTY):
		self.ground = ground
		self.middle = middle
		self.overlap = overlap
	
	def __str__(self):
		if self.overlap != EMPTY: return str(self.overlap)
		elif self.middle != EMPTY: return str(self.middle)
		else: return str(self.ground)

	#Use ground="EMPTY" to set an empty ground
	#Use ground=None to preserve existing ground value
	def set_block(self, ground=None, middle=None, overlap=None):
		if ground is not None: self.ground = ground
		if middle is not None: self.middle = middle
		if overlap is not None: self.overlap = overlap


class Map():
	def __init__(self, width, height):
		assert 1 <= width <= 1000
		assert 1 <= height <= 1000
		self.max_x = width-1
		self.max_y = height-1
		self.block_location = {}#{  (x,y):Block()  }

	def __str__(self):
		string=''
		for y in range(0,self.max_y+1):
			for x in range(0,self.max_x+1):
				string+= str(  self[x,y] )
			string+='\n'
		return string

		
	#Creates any missing block before updating it
	def __setitem__(self, coordinates, args):
		(x,y) = coordinates
		if (x,y) not in self.block_location: self.block_location[ (x,y) ] = Block()
		self.block_location[ (x,y) ].set_block(*args)
		
	#Get block at given map coordinates
	def __getitem__(self, coordinates):
		(x,y) = coordinates
		#Dummy block when outside the map
		if not (0 <= x <= self.max_x and 0<= y <= self.max_y) : return Block( DUMMY, DUMMY, None  )
		#Empty block when map is empty
		elif (x,y) not in self.block_location: return Block( EMPTY )
		#Return block in nominal case
		else: return self.block_location[(x,y)]

	#Return only a slice of the map
	def view(self, x, y, x_range=0, y_range=0):
		slice=Map(x_range*2+1, y_range*2+1)
		for y_out, y_pos in enumerate(range(y-y_range, y+y_range+1)):
			for x_out, x_pos in enumerate(range(x-x_range, x+x_range+1)):
				slice[x_out,y_out] = (self[x_pos, y_pos].ground, self[x_pos, y_pos].middle, self[x_pos, y_pos].overlap)
		return slice

#Load map from an array
def from_array(array_map):
	map=Map(len(array_map[0]),len(array_map) )
	for x in range(0, map.max_x+1 ):
		for y in range(map.max_y+1):
			map[x,y] = (None, str(array_map[y][x]), None) #Switch from (row,line) to (x,y) notation
	return map

#Load map from a string representing an array. Empty rows will be ignored
def from_string(string_map):
	return from_array([ list(i) for i in string_map.split('\n') if len(i)>3 ])

#Load map from a file
def from_file(filename):
	f=open(filename, 'r+', encoding='utf-8') #Try without encoding
	return from_string(f.read())



#########################################################################
#a = Map(3,3)
#print(a)
#
#(TREE, CLOUD, SAND) = ('T', 'C', 'S')
#a[0,0]= ('S','T','C')
#a[1,1]= ('S',)
#print(a)
###exit()
##a[1,2]= (None, 'a', EMPTY)
##print(a)
##exit()
##
#string_map='''
#axxxxxxxxxxxxx..X.............
#x.............................
#..............................
#.................X............
#..............................
#..............................
#x............................x
#..............................
#..............................
#..............................
#x............................x
#..............................
#'''
#
#a = from_string(string_map)
#print(a)
#
#print(a.view(1,2,2,2))
#
##a = from_array( [ ['u','X','X'],['X','X','X'], ['a','b','c'] ] )
##print(a)
##
##
#print (   a.view(0,0,3,3)  )
###print(a[-1,2])
##
##
##
##for i in range(-1,2):
##	for j in range(-1,2):
##		print(i,j, a[i,j])