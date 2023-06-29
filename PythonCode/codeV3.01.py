# GamepadBTv3.01 - Program to send keystrokes via Bluetooth by BeardoGuy
# Instagram: @thatbeardoguy
# 29-06-2023
	
import appuifw
import graphics
import socket
import e32
import sysinfo
from key_codes import *

global running
running=0
global inemulator
inemulator = 0

w,h =0,0
#Colors in RGB
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
GREY = (80,80,80)
GREEN = (0,192,0)
ORANGE = (255,140,0)
ORANGERED = (255,69,0)
GAINSBORO = (220,220,220)

th = 20 # title bar height
kh = 20 # softkeybar height
ot = 8 # oval button thickness
ow = 10 # point oval button width
et = 6 # ellipse button thickness
ew = 13 #ellipse button thickness
pi = 3.14
torad = 3.14/180


def func_redraw():
	#print 'redraw dummy func called'
	random1 = 1
	
def handle_redraw(rect):
	func_redraw()

# you can use this class as a chunk as it is.
class Keyboard(object):
    def __init__(self):
        self._keyboard_state={}
    def handle_event(self,event):
        #print 'handle_event called'
        if event['type'] == appuifw.EEventKeyDown:
            #print 'key down func'
            self._keyboard_state[event['scancode']]=1          
        elif event['type'] == appuifw.EEventKeyUp:
            #print 'key up func'
            self._keyboard_state[event['scancode']]=0
    def is_down(self,scancode):
        return self._keyboard_state.get(scancode,0)

# set and instance of Keyboard (so you can use all the functions of
# that class later in the script by typing e.g. keyboard.pressed...)
keyboard=Keyboard()

img=appuifw.Canvas(event_callback=keyboard.handle_event, redraw_callback=handle_redraw)
appuifw.app.body = img
appuifw.app.screen = 'full'

w, h = img.size
hm = (h+th)/2 
ym = hm
wm = w/2
xm = wm
kxm = 0.75*w 
kym = hm -10 
jym=ym-10 
jxm=(xm/2)-5

upkey = jxm, (jym-12)
downkey = jxm, (jym+12)
leftkey = (jxm-12,jym)
rightkey = (jxm+12,jym)

okkey = (jxm+26,jym+24)

lskey = 20, h-10
rskey = w-20, h-10

yeskey = jxm-22,jym+24
clearkey = kxm+12, kym-36
editkey = 44, (kym-11)

onekey = kxm-20, kym-18
twokey = (kxm,kym-20)
threekey = kxm+19, kym-23

fourkey = kxm-19, kym-6
fivekey = (kxm+1,kym-7)
sixkey = kxm+23, kym-8

sevenkey = kxm-19, kym+6
eightkey = kxm+1, kym+7
ninekey = kxm+23, kym+8

starkey = kxm-20, kym+18
zerokey = (kxm,kym+20)
hashkey = kxm+19, kym+23


def about():
    appuifw.note(u'Gamepad BT v3.01\n(C)2023 BeardoGuy', 'info')
def quit():
    if (appuifw.query(u'Are you Sure you want to exit ? ', 'query') == True):
        appuifw.note(u'Follow on Instagram:\n@thatbeardoguy', 'info')
        exit_key_handler()

def rkeyhandler():
    nothing=1

appuifw.app.exit_key_handler = rkeyhandler
script_lock = e32.Ao_lock()

def exit_key_handler():
    global running
    running=0
    script_lock.signal()
    appuifw.app.set_exit()

def draw_title():
	img.rectangle((0,0,w,th),fill=BLACK)
	img.text((0,15),u"    Gamepad BT v3.01 ",fill=ORANGERED,font=u"LatinBold13")
	
def draw_status():
	if running==0:
		img.rectangle((0,th,w,th+18),fill=GAINSBORO)
		img.text((40,th+14),u"Status: Connecting...",fill=RED,font=u"LatinPlain12")
	else:
		img.rectangle((0,th,w,th+18),fill=GAINSBORO)
		img.text((40,th+14),u"Status: Connected",fill=BLACK,font=u"LatinPlain12")

def draw_softkeys_bar():
	img.rectangle((0,h-kh,w,h),fill=GAINSBORO)
	img.text((52,h-5),u"<- SoftKeys ->",fill=BLACK,font=u"LatinPlain12")

def draw_button_point(coords,col,size):
	img.point(coords, outline = col, width = size)
		
def draw_button_point_wide(coords,col,size,wide):
    posx,posy = coords
    x1=posx-(wide/2)
    for i in range (wide):
		img.point((x1+i,posy), outline = col, width = size)

def draw_button_ellipse(posx,posy,col): 
    x1=posx-(ew/2)
    x2=posx+(ew/2)
    y1=posy-(et/2)
    y2=posy+(et/2)
    img.ellipse((x1,y1,x2,y2), outline = col, fill = col, width = 1)
	
def draw_pointJ():
    img.point((44,80), outline = BLACK, width = 40)
    img.point((44,80), outline = WHITE, width = 36)
    img.point((44,69), outline = GREY, width = 10)
    img.point((44,91), outline = GREY, width = 10)
    img.point((33,80), outline = GREY, width = 10)
    img.point((55,80), outline = GREY, width = 10)
    img.point((76,80), outline = GREY, width = 7)
    img.point((77,80), outline = GREY, width = 7)
    img.point((78,80), outline = GREY, width = 7)
    img.point((79,80), outline = GREY, width = 7)

#jOYPAD QD
def draw_joypadQD():
    jRadius = 22
    btnsize = 11
    img.ellipse((jxm-jRadius,jym-jRadius,jxm+jRadius,jym+jRadius), outline = BLACK, width = 2)
    draw_button_point(upkey, GREY, btnsize) #up
    draw_button_point(downkey, GREY, btnsize) #down
    draw_button_point(leftkey, GREY, btnsize) #left
    draw_button_point(rightkey, GREY, btnsize) #right
    draw_button_point(okkey, GREY, btnsize) #okkey
    draw_button_point(yeskey, GREY, 10) #yeskey
	
def draw_pointB():
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

def draw_overlay():
	img.arc((kxm-250,0,kxm+45,h), -15*torad, 15*torad, outline = ORANGERED, width =5) #RIGHT ARC
	img.arc((jxm-40,0,jxm+250,h), (180-15)*torad, (180+15)*torad, outline = ORANGERED, width =5) #LEFT ARC
	img.arc((kxm-250+10,0,kxm+45+10,h), -20*torad, 20*torad, outline = ORANGERED, width =7) #RIGHT ARC 2
	img.arc((jxm-40-10,0,jxm+250-10,h), (180-20)*torad, (180+20)*torad, outline = ORANGERED, width =7) #LEFT ARC
	img.line((xm-6,kym-5,xm-7,kym+4),outline = RED, width =3) 
	img.line((xm+3,kym-5,xm+2,kym+4),outline = RED, width =3) 
	img.line((xm-6,kym-5,xm+2,kym+4),outline = RED, width =3)  
	img.line((xm-12,kym-1,xm-6,kym-1),outline = RED, width =1) 
	img.line((xm+3,kym-1,xm+9,kym-1),outline = RED, width =1) 
	img.line((xm-8,kym-3,xm-6,kym-3),outline = RED, width =2) 
	img.line((xm-9,kym-2,xm-6,kym-2),outline = RED, width =2) 
	img.line((xm+3,kym-1,xm+4,kym-1),outline = RED, width =2) 
	img.point((xm+4,kym+1), outline =RED,width=1) 
	
	
#BUTTONS RIGHT SIDE BOUNDRY QD
def draw_keypadQD():
	draw_button_point_wide(onekey, GREY, 7, 6)
	draw_button_point_wide(twokey, GREY, 9, 6)
	draw_button_point_wide(threekey, GREY, 10, 6)
	draw_button_point_wide(clearkey, GREY, 9, 5)
	
	draw_button_point_wide(fourkey, GREY, 8, 6)
	draw_button_point_wide(fivekey, GREY, 9, 7)
	draw_button_point_wide(sixkey, GREY, 10, 8)

	draw_button_point_wide(sevenkey, GREY, 8, 6)
	draw_button_point_wide(eightkey, GREY, 9, 7)
	draw_button_point_wide(ninekey, GREY, 10, 8)
	
	draw_button_point_wide(starkey, GREY, 7, 6)
	draw_button_point_wide(zerokey, GREY, 9, 6)
	draw_button_point_wide(hashkey, GREY, 10, 6)

def draw_softkeys():
	draw_button_point_wide(lskey, GREY, 8, 10)
	draw_button_point_wide(rskey, GREY, 8, 10)

def func_redraw():
	if keyboard.is_down(EScancodeLeftSoftkey):
		random1 = 1
	else:
		img.clear(WHITE)
		if running==1:
			draw_overlay()
		draw_title()
		draw_status()
		draw_joypadQD()
		draw_keypadQD()
		draw_softkeys()
		img.text((27,ym+50), u'(C) 2023 BeardoGuy', fill = BLACK)
		img.text((13,ym+70), u'Hold and release \'edit\' to exit', fill = GREY,font=u"LatinPlain12")

handle_redraw(None)

bt_errors = {
	13: "BT is not supported on the Emulator!",
	2: "Protocol not supported on the selected device",
	0: "Could not Connect to the selected device",
	32:"Device Disconnected"
}

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
	
def bt_disconnect():
    global sock
    sock.close()
	
def sendkey(data):
	try:
		sock.send(data)
	except Exception, e:
		try: 
			error_code = e.args[0]  
			error_message = e.args[1] 
			print 'catch code:', error_code
			print 'catch error:', error_message
		except Exception, f: 
			print 'error: ',str(e) 
			print '+error: ',str(f) 
			appuifw.note(u"Error: "+str(e), 'error')
		else:
			appuifw.note(u"Error: "+bt_errors.get(error_code, error_message), 'error')
		exit_key_handler()
	
try:
	if e32.in_emulator()==0:
		bt_connect()
	else:
		inemulator=1
except Exception, e:
	error_code = e.args[0] 
	error_message = e.args[1]  
	print 'catch code:', error_code
	print 'catch error:', error_message
	appuifw.note(u"Error: "+bt_errors.get(error_code, error_message), 'error')
	exit_key_handler()
else:	
	running=1
	draw_status()
	draw_overlay()
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
	zero=0
	lsoft=0
	rsoft=0
	yes=0
	bspace=0
	edit=0	
	while running:
		if keyboard.is_down(EScancodeLeftArrow):        	#Left 
			if left == 0:
				draw_button_point(leftkey, RED,12)
				sendkey(u"L\n")
				left=1
		else:
			if left == 1:
				draw_button_point(leftkey, WHITE,12)
				draw_button_point(leftkey, GREY,11)
				sendkey(u"l\n")
				left=0
		if keyboard.is_down(EScancodeRightArrow):			#Right
			if right==0:
				sendkey(u"R\n")
				draw_button_point(rightkey, RED,12)
				right=1
		else:
			if right==1:
				sendkey(u"r\n")
				draw_button_point(rightkey, WHITE,12)
				draw_button_point(rightkey, GREY,11)
				right=0
		if keyboard.is_down(EScancodeDownArrow):			#Down
			if down==0:
				sendkey(u"D\n")
				draw_button_point(downkey, RED,12)
				down=1
		else:
			if down==1:
				sendkey(u"d\n")
				draw_button_point(downkey, WHITE,12)
				draw_button_point(downkey, GREY,11)
				down=0

		if keyboard.is_down(EScancodeUpArrow):				#up
			if up==0:
				sendkey(u"U\n")
				draw_button_point(upkey, RED, 12) 		
				up=1
		else:
			if up==1:
				sendkey(u"u\n")
				draw_button_point(upkey, WHITE,12)
				draw_button_point(upkey, GREY,11)
				up=0
				   
		if keyboard.is_down(EScancodeSelect):  				 #ok
			if select==0:
				sendkey(u"S\n")
				draw_button_point(okkey, RED,12)
				select=1
		else:
			if select==1:
				sendkey(u"s\n")
				draw_button_point(okkey, WHITE,12)
				draw_button_point(okkey, GREY,11)
				select=0
				
		if keyboard.is_down(EScancode5):						#5
			if five==0:
				sendkey(u"F\n")
				draw_button_point_wide(fivekey, ORANGERED, 9, 7)
				five=1
		else:
			if five==1:
				sendkey(u"f\n")
				draw_button_point_wide(fivekey, GREY, 9, 7)
				five=0

		if keyboard.is_down(EScancode7):						#7
			if seven==0:
				sendkey(u"E\n")
				draw_button_point_wide(sevenkey, ORANGERED, 8, 6)
				seven=1
		else:
			if seven==1:
				sendkey(u"e\n")
				draw_button_point_wide(sevenkey, GREY, 8, 6)
				seven=0

		if keyboard.is_down(EScancode4):						#4
			if four==0:
				sendkey(u"O\n")
				draw_button_point_wide(fourkey, RED, 8, 6)
				four=1
		else:
			if four==1:
				sendkey(u"o\n")
				draw_button_point_wide(fourkey, GREY, 8, 6)
				four=0
				
		if keyboard.is_down(EScancode1):						#1
			if one==0:
				sendkey(u"N\n")
				draw_button_point_wide(onekey, RED, 7, 6)
				one=1
		else:
			if one==1:
				sendkey(u"n\n")
				draw_button_point_wide(onekey, GREY, 7, 6)
				one=0

		if keyboard.is_down(EScancode6):						#6
			if six==0:
				sendkey(u"X\n")
				draw_button_point_wide(sixkey, RED, 10, 8)
				six=1
		else:
			if six==1:
				sendkey(u"x\n")
				draw_button_point_wide(sixkey, GREY, 10, 8)
				six=0

		if keyboard.is_down(EScancode8):						#8
			if eight==0:
				sendkey(u"G\n")
				draw_button_point_wide(eightkey, RED, 9, 7)
				eight=1
		else:
			if eight==1:
				sendkey(u"g\n")
				draw_button_point_wide(eightkey, GREY, 9, 7)
				eight=0

		if keyboard.is_down(EScancode2):						#2
			if two==0:
				sendkey(u"W\n")
				draw_button_point_wide(twokey, RED, 9, 6)
				two=1
		else:
			if two==1:
				sendkey(u"w\n")
				draw_button_point_wide(twokey, GREY, 9, 6)
				two=0
					
				
		if keyboard.is_down(EScancodeStar):						#Star
			if star==0:
				sendkey(u"T\n")
				draw_button_point_wide(starkey, RED, 7, 6)
				star=1
		else:
			if star==1:
				sendkey(u"t\n")
				draw_button_point_wide(starkey, GREY, 7, 6)
				star=0

		if keyboard.is_down(EScancode3):						#3
			if three==0:
				sendkey(u"H\n")
				draw_button_point_wide(threekey, RED, 10, 6)
				three=1
		else:
			if three==1:
				sendkey(u"h\n")
				draw_button_point_wide(threekey, GREY, 10, 6)
				three=0

		if keyboard.is_down(EScancode9):						#9
			if nine==0:
				sendkey(u"I\n")
				draw_button_point_wide(ninekey, RED, 10, 8)
				nine=1
		else:
			if nine==1:
				sendkey(u"i\n")
				draw_button_point_wide(ninekey, GREY, 10, 8)
				nine=0

		if keyboard.is_down(EScancode0):						#0
			if zero==0:
				sendkey(u"Z\n")
				draw_button_point_wide(zerokey, RED, 9, 6)
				zero=1
		else:
			if zero==1:
				sendkey(u"z\n")
				draw_button_point_wide(zerokey, GREY, 9, 6)
				zero=0

		if keyboard.is_down(EScancodeYes):						#Yes
			if yes==0:
				sendkey(u"Y\n")
				draw_button_point(yeskey, RED, 10)
				yes=1
		else:
			if yes==1:
				sendkey(u"y\n")
				draw_button_point(yeskey, GREY, 10)
				yes=0

		if keyboard.is_down(EScancodeLeftSoftkey):				#LSoft
			if lsoft==0:
				sendkey(u"J\n")
				draw_button_point_wide(lskey, RED, 8, 10)
				lsoft=1
		else:
			if lsoft==1:
				sendkey(u"j\n")
				draw_button_point_wide(lskey, GREY, 8, 10)
				lsoft=0

		if keyboard.is_down(EScancodeRightSoftkey):				#RSoft
			if rsoft==0:
				sendkey(u"K\n")
				draw_button_point_wide(rskey, RED, 8, 10)
				rsoft=1
		else:
			if rsoft==1:
				sendkey(u"k\n")
				draw_button_point_wide(rskey, GREY, 8, 10)
				rsoft=0

		if keyboard.is_down(EScancodeEdit):
			if edit==0:
				#sendkey(u"V\n") #don't use it as a key, it will stick if not pressed for more than 2 seconds
				edit=1
		else:
			if edit==1:
				#sendkey(u"v\n")
				quit()
				edit=0

		if keyboard.is_down(EScancodeBackspace):				#clear
			if bspace==0:
				sendkey(u"C\n")
				draw_button_point_wide(clearkey, RED, 9, 5)
				bspace=1
		else:
			if bspace==1:
				sendkey(u"c\n")
				draw_button_point_wide(clearkey, GREY, 9, 5)
				bspace=0

		if keyboard.is_down(EScancodeHash):						#hash
			if hash==0:
				sendkey(u"A\n")
				draw_button_point_wide(hashkey, RED, 10, 6)
				hash=1
		else:
			if hash==1:
				sendkey(u"a\n")
				draw_button_point_wide(hashkey, GREY, 10, 6)
				hash=0
				
				
		e32.ao_yield()

script_lock.wait()



