from module.map import from_file as load_map_from_file
from module.game import Game
from module.init import *
from client.shell_init import *

import datetime

sysdate = datetime.datetime.now


game = Game(map = load_map_from_file('database/001.map'))

player_h = game.add_player("Huginn",1,5)
player_m = game.add_player("Muninn",0,0)
print(game)
#print( game.map.get_slice(0,0,5,5)  )
#game.move_player(toto, 1,3)

#game.down(toto_id)q
#print(game.map.view(1,3,5,5)  )

#print(game.player_view(1  ))

import curses



def pbar(window):
	w_height, w_width = window.getmaxyx()
	curses.curs_set(0)

	if w_height < 10 or w_width < 40: raise BaseException('Terminal size must be at least 10 lines and 40 columns wide')

	#curses.newpad(nlines, ncols)
	pad_player_h = curses.newpad(PLAYER_H_HEIGHT, PLAYER_H_WIDTH+50)
	pad_player_h.nodelay(True)
	pad_player_h.scrollok(True)
	pad_player_h.keypad(True)
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	COLORPAIR_BLUE = curses.color_pair(1)
	pad_player_h.bkgd(COLORPAIR_BLUE)

	pad_player_m = curses.newpad(PLAYER_M_HEIGHT, PLAYER_M_WIDTH+50)

	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	COLORPAIR_BLUE = curses.color_pair(1)
	pad_player_m.bkgd(COLORPAIR_BLUE)
	
	pad_menu = curses.newpad(MENU_HEIGHT, MENU_WIDTH)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
	COLORPAIR_MENU = curses.color_pair(2)
	pad_menu.bkgd(COLORPAIR_MENU)
	
	key_list = (MOVE_UP, MOVE_RIGHT, MOVE_DOWN, MOVE_LEFT)
	key_player_h = dict(zip(PLAYER_H_KEYS, key_list))
	key_player_m = dict(zip(PLAYER_M_KEYS, key_list))
	#print(key_player_h)
	#print(key_player_m)
	
	last_dt = sysdate()
	
	while True:

		#################################################
		#Capture key
		try: ch = pad_player_h.getch()
		except: ch = -1
		
		
		pad_menu.addstr(0,0, 'TIME '+str(sysdate()-last_dt)) 
		pad_menu.refresh(0,0, MENU_TOP_ROW ,MENU_TOP_COL, MENU_BOTTOM_ROW, MENU_BOTTOM_COL)
		
		pad_player_h.addstr(0,0,str(  game.player_view(0)) )
		pad_player_h.refresh(0,0, PLAYER_H_TOP_ROW,PLAYER_H_TOP_COL, PLAYER_H_BOTTOM_ROW, PLAYER_H_BOTTOM_COL )

		pad_player_m.addstr(0,0,str(  game.player_view(1)) )
		pad_player_m.refresh(0,0, PLAYER_M_TOP_ROW,PLAYER_M_TOP_COL, PLAYER_M_BOTTOM_ROW, PLAYER_M_BOTTOM_COL)
		
		
		#################################################
		# Handle key
		if ch == -1: continue
		pad_menu.addstr(1,0, 'KEY  ' + str(ch).ljust(4) ) 
		if ch in QUIT: break
		elif ch in(MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT):  game.move_player(0, ch)
		elif ch in key_player_h:  game.move_player(player_h, key_player_h[ch] )
		elif ch in key_player_m:  game.move_player(player_m, key_player_m[ch] )




curses.wrapper(pbar)


