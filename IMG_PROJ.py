from img_gui_func import *
import os
from tkinter import *
from PIL import Image , ImageTk
import glob
import os

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#----------------------------------------------------------------------
# ------------------- CREATING MENU ITEMS ------------------------
# ---------------------------------------------------------------------
menu = Menu(window,bg="#1c4064",fg="#eee")
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Select Working folder',command=(lambda: IMP.choose_file_path()))
filemenu.add_command(label='Show in Folder',command=(lambda: IMP.show_folder()))
filemenu.add_command(label='Show Image',command=(lambda: IMP.disp_image()))
filemenu.add_separator()
filemenu.add_command(label='Exit',  command=(lambda:IMP.on_Exit()))

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About Image',command=(lambda: IMP.image_info()))
helpmenu.add_command(label='Guide')

#-----------------------------------------------------------------------







#----------------------------------------------------------------------
# ------------------- CREATING SCROLLBAR FRAME ------------------------
# ---------------------------------------------------------------------


def _on_mousewheel(event):
    print("scroll")

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    #canvas.configure(scrollregion=canvas.bbox('all'))
    print("heelo")
#
#canvas = Canvas(window,width=112,height=741)


#scrollbarY = Scrollbar(window, orient="vertical", command=canvas.yview,relief="raised",bg="#666666",activebackground="#85929e",troughcolor="#85929e",highlightbackground="#85929e",bd=1,highlightthickness=0)
#scrollbarY.grid(sticky="NS",row=0,column=2)
#scrollbarX = Scrollbar(window, orient="horizontal", command=canvas.xview,relief="raised",bg="#666666",activebackground="#85929e",troughcolor="#85929e",highlightbackground="#85929e",bd=2,highlightthickness=5)
#scrollbarX.grid(sticky="WE",row=1,column=0)
#canvas.configure(xscrollcommand = scrollbarX.set)


# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
#canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

#frame = Frame(canvas,)
#canvas.create_window((300,300), window=frame, anchor='nw',)

inst_info_frame =Frame(window,)
input_Frame =Frame(window,)
button_Frame =Frame(window,)

image_Frame=Canvas(window,)
#canvas.grid()
'''
inst_info_frame.grid(row=0,column=0, columnspan="1", sticky=N,)
button_Frame.grid(row=0, columnspan="1", sticky=NW,)
input_Frame.grid(row=1, columnspan="1", sticky=NW,)

image_Frame.grid(row=0, column=1,sticky=NW,rowspan="3")

inst_info_frame.pack(side=TOP)
button_Frame.pack(side=LEFT)
input_Frame.pack(side=RIGHT)

image_Frame.pack(anchor=CENTER)
'''
inst_info_frame.pack(anchor=CENTER)
button_Frame.pack(side=LEFT,anchor=CENTER)
input_Frame.pack(side=RIGHT,anchor=CENTER)

image_Frame.pack(anchor=CENTER, fill=BOTH, expand=1)

#----------------------------------------------------------------------
# ------------------- CREATING SCROLLBAR FRAME ------------------------
# ---------------------------------------------------------------------


window.title("Image Processing")
# COLOR MAIN PRIMARY
#frame.configure(bg="#555555",highlightthickness=0,bd=0)
#canvas.configure(bg="#555555",bd=0,highlightthickness=0)
window.configure(bg="#555555",bd=0,highlightthickness=0)



# Label
title = Label(inst_info_frame, text="### Welcome to IMAGE PROCESSING project by Harpal Singh####", fg="white",bg="#0088ff")
status_label = Label(inst_info_frame, text="", fg="white",bg="#000000")
# ---- Function BUTTONS


# ------ ESSENTIAL BUTTONS----

select_image = Button(button_Frame, text="Select Image", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white", command=(lambda: IMP.select_image_msg()))
save_btn = Button(button_Frame, text="Save Image", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white", command=(lambda: IMP.save_image_msg(image)))
cancel_btn = Button(button_Frame, text="Cancel", bg="#000000", fg="white",activebackground="#0061b5",activeforeground="white",  command=(lambda: IMP.cancelUndo()))
exit_btn = Button(button_Frame, text="Exit", bg="#000000", fg="white",activebackground="red",activeforeground="white",  command=(lambda:IMP.on_Exit()))
Ok_btn = Button(input_Frame, text="OK", bg="#0088ff", fg="white",activebackground="#000000",activeforeground="white", relief="raised", command=(lambda: IMP.call_functions()))
color_btn = Button(input_Frame, text="Color 1", bg="#000000", fg="white",activebackground="#0088ff",activeforeground="white", relief="raised", command=(lambda: IMP.set_color()))
color2_btn = Button(input_Frame, text="Color 2", bg="#000000", fg="white",activebackground="#0088ff",activeforeground="white", relief="raised", command=(lambda: IMP.set_color2()))
# ----- ESSENTIAL BUTTONS-----

crop_btn = Button(button_Frame, text="Crop", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.crop_msg(image)))
border_btn = Button(button_Frame, text="Add Border", bg="#000000", fg="white",activebackground="#0061b5",activeforeground="white", command=(lambda: IMP.border_msg(image)))
bw_btn = Button(button_Frame, text="Black/White", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.blackNwhite_msg(image)))
resize_btn = Button(button_Frame, text="Resize", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.resize_msg(image)))
wmark_btn = Button(button_Frame, text="Add Watermark", bg="#000000", fg="white",activebackground="#0061b5",activeforeground="white", command=(lambda: IMP.watermark_msg(image)))
rotate_btn = Button(button_Frame, text="Rotate", bg="#000000", fg="white",activebackground="#0061b5",activeforeground="white", command=(lambda: IMP.rotate_msg(image)))
text_btn = Button(button_Frame, text="Add Text", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.draw_text_msg(image)))
convert_btn = Button(button_Frame, text="Convert", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.convert_msg(image)))
flip_btn = Button(button_Frame, text="Flip", bg="#000000", fg="white", activebackground="#0061b5",activeforeground="white",command=(lambda: IMP.flip_msg(image)))
show_btn = Button(button_Frame, text="Show Image", bg="#000000", fg="white",command=(lambda: image.show()))

# ---- Function BUTTONS END----


# ----- Display ESSENTIAL boxes  ---





current_inst = Text(inst_info_frame,height=2,bd=0,relief="raised", highlightthickness=0, selectbackground="#000000",selectforeground="white",highlightcolor="#666666", bg="#666666",fg="#ffffff")
current_inst.insert(INSERT, "Instructions / messages will appear here:")
#-List Options Choices

scrollbarList = Scrollbar(input_Frame,orient="vertical",bg="#666666",relief="raised",activebackground="#85929e",troughcolor="#85929e",highlightbackground="#85929e",bd=3,highlightthickness=5)
inst_listbox = Listbox(input_Frame,yscrollcommand=scrollbarList.set, relief="raised", highlightthickness=5, selectbackground="#000000",
                       bd=0, selectforeground="white",height=5,highlightcolor="#85929e")
scrollbarList.config(command=inst_listbox.yview)

# ---- List Options Choices ----


# ---- ENTRY Input from users
user_input = Entry(input_Frame,relief="raised", highlightthickness=5, selectbackground="#000000",selectforeground="white",highlightcolor="#85929e")
Scale_inputH = Scale(input_Frame,from_=0, to=360, orient=HORIZONTAL)
Scale_inputV = Scale(input_Frame,from_=0, to=500, orient=VERTICAL)
# ---- ENTRY Input from users


# ----- Display ESSENTIAL boxes  ---
###
#
#
#
##
#





canvas_image_holder=Canvas(image_Frame, bg="#555555",bd=0,highlightthickness=0)



item = canvas_image_holder.create_rectangle(0,0,0,0)
'''
canvas_img= Canvas(canvas_image_holder,width=600, height=700, bg="red")
canvas_img.grid(stick=NSEW)
image_label = Label(canvas_img,image=disp_img,bg="#000000",relief="raised",bd=0)
image_label.grid(row=0)
image_label.bind("<Key>", key)
image_label.bind("<ButtonRelease-1>", motion)
item = canvas_image_holder.create_rectangle(0,0,0,0)
'''




#
##
#
#
#
#

#----------------------------------------------
# ------ PLACING WIDGETS ON THE SCREEN --------
#----------------------------------------------


#-------------------------------------------------
#------------- INFO FRAME----------------------
#-------------------------------------------------

title.pack(fill="both")

current_inst.pack(fill="both")
status_label.pack(fill="both")
# -------------------------------------------------------------------------
#--------------------------------------------------------------------------


#-------------------------------------------------
#------------- IMAGE FRAME----------------------
#-------------------------------------------------
canvas_image_holder.pack(anchor="center",)

# ------------------------------------------------

#-------------------------------------------------
#------------- INPUT FRAME----------------------
#-------------------------------------------------
inst_listbox.grid(row=0, columnspan="2", column=1, sticky=NSEW)
scrollbarList.grid(row=0,column=0, sticky=NS)
user_input.grid(row=1, column=1, sticky=NSEW, columnspan=2)
Ok_btn.grid(row=2, column=1, sticky=NSEW, columnspan=2)
Scale_inputH.grid(row=4, column=1, sticky="WE", columnspan=2)
Scale_inputV.grid(row=5, column=1, sticky="NSEW", rowspan=2,columnspan=2)
color_btn.grid(row=7, column=1, sticky=NSEW, )
color2_btn.grid(row=7, column=2,sticky=NSEW, )
# ----- ---------------------------------------------


# Function Buttons

#-------------------------------------------------
#------------- Button FRAME----------------------
#-------------------------------------------------
select_image.grid(row=1, column=1,sticky=NSEW, columnspan=1, )
save_btn.grid(row=1, column=2,sticky=NSEW, columnspan=1 )
cancel_btn.grid(row=2, column=1,sticky=NSEW, columnspan=1)
exit_btn.grid(row=2, column=2, sticky=NSEW, columnspan=1)
# Essential
bw_btn.grid(row=3, column=1, sticky=NSEW, columnspan=1)
border_btn.grid(row=3, column=2, sticky=NSEW, columnspan=1)
resize_btn.grid(row=4, column=1,sticky=NSEW, columnspan=1)
crop_btn.grid(row=4, column=2,sticky=NSEW, columnspan=1 )

text_btn.grid(row=5, column=1,sticky=NSEW, columnspan=1 )
convert_btn.grid(row=5, column=2,sticky=NSEW, columnspan=1 )
rotate_btn.grid(row=6, column=1,sticky=NSEW, columnspan=1)
flip_btn.grid(row=6, column=2,sticky=NSEW, columnspan=1)
wmark_btn.grid(row=7, column=1, columnspan=2,sticky=NSEW, )

#---------------------------------------------------------
#---------------------------------------------------------










# Function Buttons

# ---------------------- INITIALIZE Class and Create Object --------------------------------------




IMP = ImgProcessing(current_inst, inst_listbox, user_input,window,canvas_image_holder,Scale_inputH,Scale_inputV,color_btn,color2_btn, status_label,image_Frame)

#---------------------------------------------------
#--------------- MANAGING MOUSE SCROLL -------------
#---------------------------------------------------
list_c_focus=False
def list_focused(event):
    global list_c_focus
    list_c_focus=True

def list_unfocused(event):
    global list_c_focus
    list_c_focus = False
def MouseWheelHandler(event):
    direction = 0
    if event.num == 5 or event.delta == -120:
     direction = 1
    if event.num == 4 or event.delta == 120:
     direction = -1
    #if list_c_focus==False:
        #canvas.yview_scroll(direction, UNITS)


#---------------------------------------------------
#--------------- MANAGING MOUSE SCROLL -------------
#---------------------------------------------------

# --------------------------------------------------------
# --------------- ON EXIT -----------------------
# --------------------------------------------------------
ignore_first_hit=True
def call(event):
    IMP.call_functions()







# --- CENTER WIDGETS ---------------
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# --- CENTER WIDGETS ---------------

# --------- BIND EVENTS -----------------
inst_listbox.bind('<<ListboxSelect>>', IMP.onselect)
inst_listbox.bind("<FocusIn>", list_focused)
#frame.bind("<FocusIn>", list_unfocused)
inst_listbox.bind("<FocusOut>", list_unfocused)
user_input.bind('<<Ok_btn>>', IMP.call_functions)
user_input.bind('<Return>',call)
inst_listbox.bind('<Return>',call)
window.bind("<MouseWheel>",MouseWheelHandler)
#------------------ NO NEDEED JUST ADDED TO MAKE THE EVENT WORKING LINUX-----------------

#window.geometry(str(screen_width)+"x"+str(screen_height))

window.bind("<Button-4>",MouseWheelHandler)
window.bind("<Button-5>",MouseWheelHandler)
#
window.protocol("WM_DELETE_WINDOW", IMP.on_Exit)
window.mainloop()