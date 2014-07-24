from Tkinter import Tk, Canvas, Button, Frame, BOTH, NORMAL, HIDDEN

def draw_a(e):	
	ii = (e.y-3) / cell_size
	jj = (e.x-3) / cell_size
	canvas.itemconfig(cell_matrix[addr(ii, jj)], state=NORMAL, tags='vis')

def addr(ii,jj):
	if(ii < 0 or jj < 0 or ii >= field_height or jj >= field_width):
		return len(cell_matrix)-1	
	else:
		return ii * (win_width / cell_size) + jj
	
def refresh():	
	for i in xrange(field_height):
		for j in xrange(field_width):
			k = 0
			for i_shift in xrange(-1, 2):
				for j_shift in xrange(-1, 2):
					if (canvas.gettags(cell_matrix[addr(i + i_shift, j + j_shift)])[0] == 'vis' and (i_shift != 0 or j_shift != 0)):
						k += 1		
			current_tag = canvas.gettags(cell_matrix[addr(i, j)])[0]							
			if(k == 3):
				canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_vis'))
			if(k <= 1 or k >= 4):
				canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_hid'))
			if(k == 2 and canvas.gettags(cell_matrix[addr(i, j)])[0] == 'vis'):
			    canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_vis'))		

def step():	
	refresh()
	repaint()		

def clear():
	for i in xrange(field_height):
		for j in xrange(field_width):
			canvas.itemconfig(cell_matrix[addr(i, j)], state=HIDDEN, tags=('hid','0'))

def repaint():
	for i in xrange(field_height):
		for j in xrange(field_width):			
			if (canvas.gettags(cell_matrix[addr(i, j)])[1] == 'to_hid'):
				canvas.itemconfig(cell_matrix[addr(i, j)], state=HIDDEN, tags=('hid','0'))
			if (canvas.gettags(cell_matrix[addr(i, j)])[1] == 'to_vis'):
				canvas.itemconfig(cell_matrix[addr(i, j)], state=NORMAL, tags=('vis','0'))
	

root = Tk()
root.title('4 cuba')
win_width = 350
win_height = 370
config_string = "{0}x{1}".format(win_width, win_height + 32)
fill_color = "green"
root.geometry(config_string)
cell_size = 20
canvas = Canvas(root, height=win_height)
canvas.pack(fill=BOTH)	

field_height = win_height / cell_size
field_width = win_width / cell_size

cell_matrix = []
for i in xrange(field_height):
	for j in xrange(field_width):
		square = canvas.create_rectangle(2 + cell_size*j, 2 + cell_size*i, cell_size + cell_size*j - 2, cell_size + cell_size*i - 2, fill=fill_color)
		canvas.itemconfig(square, state=HIDDEN, tags=('hid','0'))
		cell_matrix.append(square)
fict_square = canvas.create_rectangle(0,0,0,0, state=HIDDEN, tags=('hid','0'))
cell_matrix.append(fict_square)

canvas.itemconfig(cell_matrix[addr(8, 8)], state=NORMAL, tags='vis')
canvas.itemconfig(cell_matrix[addr(10, 9)], state=NORMAL, tags='vis')
canvas.itemconfig(cell_matrix[addr(9, 9)], state=NORMAL, tags='vis')
canvas.itemconfig(cell_matrix[addr(9, 8)], state=NORMAL, tags='vis')
canvas.itemconfig(cell_matrix[addr(9, 7)], state=NORMAL, tags='vis')
canvas.itemconfig(cell_matrix[addr(10, 7)], state=NORMAL, tags='vis')

frame = Frame(root)
btn1 = Button(frame, text='Eval', command = step)
btn2 = Button(frame, text='Clear', command = clear)
btn1.pack(side='left')
btn2.pack(side='right')
frame.pack(side='bottom')

canvas.bind('<B1-Motion>', draw_a)
canvas.bind('<ButtonPress>', draw_a)

root.mainloop()
