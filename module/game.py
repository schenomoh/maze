from module.init import *

class Player():
	def __init__(self, id, name, x, y, view_width=19, view_height=6):
		#self.type = type
		self.id = id
		self.name = name
		self.x, self.y = (x, y)
		self.view_width=view_width
		self.view_height=view_height
	
	def __str__(self):
		string = ''
		string += self.name+ '('+str(self.id)+')\n'
		#string += ' > type: '+self.type+ '\n'

		string += ' > location: '+str(  (self.x, self.y)  )+'\n'
		return string
		
		
class Game():
	def __init__(self, map):
		self.map = map
		self.player_list = []
	
	def __str__(self):
		string =''
		string += str(self.map)
		string+= '\n'.join([str(p) for p in self.player_list])
		return string
		
	def add_player(self, name='Player',x=0,y=0):
		player_id=len(self.player_list)
		self.player_list.append(Player(player_id, name, x, y))
		self.map[x,y] = (None, player_id, None)
		return player_id
	
	def move_player(self, mobile_id, direction=None,to_x=None, to_y=None):
		player =self.player_list[mobile_id]
		if direction is not None: to_x, to_y = (player.x,player.y)
		if direction == MOVE_LEFT: to_x-=1
		if direction == MOVE_RIGHT:  to_x+=1
		if direction == MOVE_UP:  to_y-=1
		if direction == MOVE_DOWN:  to_y+=1
		print(direction)
		if self.map[to_x, to_y].middle != EMPTY: return ERROR
		#if self.map[to_x,to_y].ground != EMPTY: returqn
		self.map[player.x, player.y] = (None, EMPTY, None)
		self.map[to_x, to_y] = (None, mobile_id, None)
		player.x, player.y = to_x, to_y
		return OK

		
	def player_view(self, mobile_id):
		#print(  self.map.get_slice(self.player_list[mobile_id].x , self.player_list[mobile_id].y)   )
		player =self.player_list[mobile_id]
		return self.map.view(player.x,player.y, player.view_width, player.view_height)
		
		
