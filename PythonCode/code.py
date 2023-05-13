# Program to send keystrokes to the serial port of the HC-06/HC-05 by BeardoGuy 
# 20-04-2023

import appuifw
import graphics
# import the module socket
import socket
import e32
import sysinfo
from key_codes import *

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GREY = (80,80,80)

def about():
    appuifw.note(u'Gamepad BT v1.02\n(C)2023 BeardoGuy', 'info')
def quit():
    if (appuifw.query(u'Are you Sure ? ', 'query') == True):
        appuifw.note(u'Follow on Instagram:\n@thatbeardoguy', 'info')
        exit_key_handler()
	
#jOYPAD
def draw_pointJ():
    img.point((44,80), outline = BLACK, width = 40)
    img.point((44,80), outline = WHITE, width = 36)
    img.point((44,69), outline = GREY, width = 10)
    img.point((44,91), outline = GREY, width = 10)
    img.point((33,80), outline = GREY, width = 10)
    img.point((55,80), outline = GREY, width = 10)
    #select button
    img.point((76,80), outline = GREY, width = 7)
    img.point((77,80), outline = GREY, width = 7)
    img.point((78,80), outline = GREY, width = 7)
    img.point((79,80), outline = GREY, width = 7)
	
#BUTTONS RIGHT SIDE
def draw_pointB():
    img.point((132,80), outline = BLACK, width = 40)
    img.point((132,80), outline = WHITE, width = 36)
    #Y
    img.point((132,69), outline = GREY, width = 10)
    #A
    img.point((132,91), outline = GREY, width = 10)
    #X
    img.point((121,80), outline = GREY, width = 10)
    #B
    img.point((143,80), outline = GREY, width = 10)
    #start button
    img.point((100,80), outline = GREY, width = 7)
    img.point((99,80), outline = GREY, width = 7)
    img.point((98,80), outline = GREY, width = 7)
    img.point((97,80), outline = GREY, width = 7)

#BUTTONS FRONT LEFT	
def draw_buttonsL():
    img.point((41,52), outline = GREY, width = 6)
    img.point((42,52), outline = GREY, width = 6)
    img.point((43,52), outline = GREY, width = 6)
    img.point((44,52), outline = GREY, width = 6)
    img.point((45,52), outline = GREY, width = 6)
    img.point((46,52), outline = GREY, width = 6)
    img.point((47,52), outline = GREY, width = 6)
    #L2
    img.point((41,40), outline = GREY, width = 6)
    img.point((42,40), outline = GREY, width = 6)
    img.point((43,40), outline = GREY, width = 6)
    img.point((44,40), outline = GREY, width = 6)
    img.point((45,40), outline = GREY, width = 6)
    img.point((46,40), outline = GREY, width = 6)
    img.point((47,40), outline = GREY, width = 6)
    img.text((24,45), u'L2', fill = BLACK)
    img.text((24,57), u'L1', fill = BLACK)

#BUTTONS FRONT RIGHT	
def draw_buttonsR():
    img.point((135,52), outline = GREY, width = 6)
    img.point((129,52), outline = GREY, width = 6)
    img.point((130,52), outline = GREY, width = 6)
    img.point((131,52), outline = GREY, width = 6)
    img.point((132,52), outline = GREY, width = 6)
    img.point((133,52), outline = GREY, width = 6)
    img.point((134,52), outline = GREY, width = 6)
    #R2
    img.point((129,40), outline = GREY, width = 6)
    img.point((130,40), outline = GREY, width = 6)
    img.point((131,40), outline = GREY, width = 6)
    img.point((132,40), outline = GREY, width = 6)
    img.point((133,40), outline = GREY, width = 6)
    img.point((134,40), outline = GREY, width = 6)
    img.point((135,40), outline = GREY, width = 6)
    img.text((142,45), u'R2', fill = BLACK)
    img.text((142,57), u'R1', fill = BLACK)

def draw_pointU(col,size):
    img.point((44,69), outline = col, width = size)

def draw_pointD(col,size):
    img.point((44,91), outline = col, width = size)
	
def draw_pointL(col,size):
    img.point((33,80), outline = col, width = size)
	
def draw_pointR(col,size):
    img.point((55,80), outline = col, width = size)
	
def draw_select(col,size):
    img.point((76,80), outline = col, width = size)
    img.point((77,80), outline = col, width = size)
    img.point((78,80), outline = col, width = size)
    img.point((79,80), outline = col, width = size)
	
def draw_start(col,size):
    img.point((100,80), outline = col, width = size)
    img.point((99,80), outline = col, width = size)
    img.point((98,80), outline = col, width = size)
    img.point((97,80), outline = col, width = size)

def draw_buttonX(col,size):
    img.point((121,80), outline = col, width = size)
	
def draw_buttonY(col,size):
    img.point((132,69), outline = col, width = size)
	
def draw_buttonA(col,size):
    img.point((132,91), outline = col, width = size)
	
def draw_buttonB(col,size):
    img.point((143,80), outline = col, width = size)

def draw_buttonL1(col,size):
    img.point((41,52), outline = col, width = size)
    img.point((42,52), outline = col, width = size)
    img.point((43,52), outline = col, width = size)
    img.point((44,52), outline = col, width = size)
    img.point((45,52), outline = col, width = size)
    img.point((46,52), outline = col, width = size)
    img.point((47,52), outline = col, width = size)
	
def draw_buttonL2(col,size):
    img.point((41,40), outline = col, width = size)
    img.point((42,40), outline = col, width = size)
    img.point((43,40), outline = col, width = size)
    img.point((44,40), outline = col, width = size)
    img.point((45,40), outline = col, width = size)
    img.point((46,40), outline = col, width = size)
    img.point((47,40), outline = col, width = size)
	
def draw_buttonR1(col,size):
    img.point((135,52), outline = col, width = size)
    img.point((129,52), outline = col, width = size)
    img.point((130,52), outline = col, width = size)
    img.point((131,52), outline = col, width = size)
    img.point((132,52), outline = col, width = size)
    img.point((133,52), outline = col, width = size)
    img.point((134,52), outline = col, width = size)
	
def draw_buttonR2(col,size):
    img.point((129,40), outline = col, width = size)
    img.point((130,40), outline = col, width = size)
    img.point((131,40), outline = col, width = size)
    img.point((132,40), outline = col, width = size)
    img.point((133,40), outline = col, width = size)
    img.point((134,40), outline = col, width = size)
    img.point((135,40), outline = col, width = size)	
	
def handle_redraw(rect):
    if img: canvas.blit(img)


# you can use this class as a chunk as it is.
class Keyboard(object):
    def __init__(self,onevent=lambda:None):
        self._keyboard_state={}
        self._downs={}
        self._onevent=onevent
    def handle_event(self,event):
        if event['type'] == appuifw.EEventKeyDown:
            code=event['scancode']
            if not self.is_down(code):
                self._downs[code]=self._downs.get(code,0)+1
                #handle_redraw(None)
            self._keyboard_state[code]=1
            #handle_redraw(None)
        elif event['type'] == appuifw.EEventKeyUp:
            self._keyboard_state[event['scancode']]=0
            #handle_redraw(None)
        self._onevent()
    def is_down(self,scancode):
        return self._keyboard_state.get(scancode,0)
    def pressed(self,scancode):
        if self._downs.get(scancode,0):
            self._downs[scancode]-=1
            return True
        return False

# set and instance of Keyboard (so you can use all the functions of
# that class later in the script by typing e.g. keyboard.pressed...)
keyboard=Keyboard()


appuifw.app.screen='normal'
appuifw.app.title = u"Gamepad BT"
appuifw.app.menu = [(u"About", about),(u"Exit",quit)]

# use the appuifw.Canvas function and as "event_callback" put "
# keyboard.handle_event", a function which does the keyboard scan
canvas=appuifw.Canvas(event_callback=keyboard.handle_event, redraw_callback=handle_redraw)

# set the application body to canvas
# appuifw.app.body=canvas
img = None
appuifw.app.body = canvas
# appuifw.app.screen = 'full'

w, h = canvas.size
img = graphics.Image.new((w, h))
img.clear(WHITE)
draw_pointJ()
draw_pointB()
draw_buttonsR()
draw_buttonsL()
img.text((30,120), u'(C) 2023 BeardoGuy', fill = BLACK)

# function that handles the bluetooth connection:
def bt_connect():
    global sock
    # create a bluetooth socket
    sock=socket.socket(socket.AF_BT,socket.SOCK_STREAM)
    target=''# here you can give the bt address of the other mobile if you know it
    if not target:
        # scan for bluetooth devices
        address,services=socket.bt_discover()
        print "Discovered: %s, %s"%(address,services)
        if len(services)>1:
            choices=services.keys()
            choices.sort()
            # bring up a popup menu and show the available bt devices for selection
            choice=appuifw.popup_menu([unicode(services[x])+": "+x
                                        for x in choices],u'Choose port:')
            target=(address,services[choices[choice]])
        else:
            target=(address,services.values()[0])
    print "Connecting to "+str(target)
    # connect to the serial port of the HC-06/HC-05
    sock.connect(target)
    print "OK."

    # call the text input field function   
    #bt_typetext()
# call the function that handles the bluetooth connection
bt_connect()	
	
def exit_key_handler():
    global running
    running=0
    script_lock.signal()
    appuifw.app.set_exit()
	
running=1
left=0
right=0
up=0
down=0
select=0
five=0
seven=0
four=0
one=0
six=0
eight=0
two=0
star=0
three=0
nine=0
lkey=0
hash=0
	
while running:
    # check if the left arrow key has been pressed
    if keyboard.is_down(EScancodeLeftArrow):
	    if left == 0:
			draw_pointL(RED,12)
			handle_redraw(None)
			sock.send(u"L\n")
			left=1
			# send the typed in characters over bluetooth to the PC
    else:
	    if left == 1:
			draw_pointL(WHITE,12)
			draw_pointL(GREY,10)
			handle_redraw(None)
			sock.send(u"l\n")
			left=0
    if keyboard.is_down(EScancodeRightArrow):
        if right==0:
			sock.send(u"R\n")
			draw_pointR(RED,12)
			handle_redraw(None)
			right=1
    else:
		if right==1:
			sock.send(u"r\n")
			draw_pointR(WHITE,12)
			draw_pointR(GREY,10)
			handle_redraw(None)
			right=0
    if keyboard.is_down(EScancodeDownArrow):
        if down==0:
			sock.send(u"D\n")
			draw_pointD(RED,12)
			handle_redraw(None)
			down=1
    else:
		if down==1:
			sock.send(u"d\n")
			draw_pointD(WHITE,12)
			draw_pointD(GREY,10)
			handle_redraw(None)
			down=0

    if keyboard.is_down(EScancodeUpArrow):
        if up==0:
			sock.send(u"U\n")
			draw_pointU(RED,12)
			handle_redraw(None)
			up=1
    else:
		if up==1:
			sock.send(u"u\n")
			draw_pointU(WHITE,12)
			draw_pointU(GREY,10)
			handle_redraw(None)
			up=0
               
    if keyboard.is_down(EScancodeSelect):
        if select==0:
			sock.send(u"S\n")
			draw_start(RED,8)
			handle_redraw(None)
			select=1
    else:
		if select==1:
			sock.send(u"s\n")
			draw_start(WHITE,8)
			draw_start(GREY,7)
			handle_redraw(None)
			select=0
			
    if keyboard.is_down(EScancode5):
        if five==0:
			sock.send(u"F\n")
			draw_buttonB(RED,12)
			handle_redraw(None)
			five=1
    else:
		if five==1:
			sock.send(u"f\n")
			draw_buttonB(WHITE,12)
			draw_buttonB(GREY,10)
			handle_redraw(None)
			five=0

    if keyboard.is_down(EScancode7):
        if seven==0:
			sock.send(u"E\n")
			draw_buttonA(RED,12)
			handle_redraw(None)
			seven=1
    else:
		if seven==1:
			sock.send(u"e\n")
			draw_buttonA(WHITE,12)
			draw_buttonA(GREY,10)
			handle_redraw(None)
			seven=0

    if keyboard.is_down(EScancode4):
        if four==0:
			sock.send(u"O\n")
			draw_buttonX(RED,12)
			handle_redraw(None)
			four=1
    else:
		if four==1:
			sock.send(u"o\n")
			draw_buttonX(WHITE,12)
			draw_buttonX(GREY,10)
			handle_redraw(None)
			four=0
			
    if keyboard.is_down(EScancode1):
        if one==0:
			sock.send(u"N\n")
			draw_buttonY(RED,12)
			handle_redraw(None)
			one=1
    else:
		if one==1:
			sock.send(u"n\n")
			draw_buttonY(WHITE,12)
			draw_buttonY(GREY,10)
			handle_redraw(None)
			one=0

    if keyboard.is_down(EScancode6):
        if six==0:
			sock.send(u"X\n")
			six=1
    else:
		if six==1:
			sock.send(u"x\n")
			six=0

    if keyboard.is_down(EScancode8):
        if eight==0:
			sock.send(u"G\n")
			draw_buttonR2(RED,7)
			handle_redraw(None)
			eight=1
    else:
		if eight==1:
			sock.send(u"g\n")
			draw_buttonR2(WHITE,7)
			draw_buttonR2(GREY,6)
			handle_redraw(None)
			eight=0

    if keyboard.is_down(EScancode2):
        if two==0:
			sock.send(u"W\n")
			draw_buttonL1(RED,7)
			handle_redraw(None)
			two=1
    else:
		if two==1:
			sock.send(u"w\n")
			draw_buttonL1(WHITE,7)
			draw_buttonL1(GREY,6)
			handle_redraw(None)
			two=0
				
			
    if keyboard.is_down(EScancodeStar):
        if star==0:
			sock.send(u"T\n")
			draw_buttonL2(RED,7)
			handle_redraw(None)
			star=1
    else:
		if star==1:
			sock.send(u"t\n")
			draw_buttonL2(WHITE,7)
			draw_buttonL2(GREY,6)
			handle_redraw(None)
			star=0

    if keyboard.is_down(EScancode3):
        if three==0:
			sock.send(u"H\n")
			draw_buttonR1(RED,7)
			handle_redraw(None)
			three=1
    else:
		if three==1:
			sock.send(u"h\n")
			draw_buttonR1(WHITE,7)
			draw_buttonR1(GREY,6)
			handle_redraw(None)
			three=0

    if keyboard.is_down(EScancode9):
        if nine==0:
			sock.send(u"I\n")
			nine=1
    else:
		if nine==1:
			sock.send(u"i\n")
			nine=0

    if keyboard.is_down(EScancodeHash):
        if hash==0:
			sock.send(u"A\n")
			draw_select(RED,8)
			handle_redraw(None)
			hash=1
    else:
		if hash==1:
			sock.send(u"a\n")
			draw_select(WHITE,8)
			draw_select(GREY,7)
			handle_redraw(None)
			hash=0
			
			
    e32.ao_yield()
	



script_lock = e32.Ao_lock()

appuifw.app.exit_key_handler = quit

script_lock.wait()


