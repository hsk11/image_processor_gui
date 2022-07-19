from tkinter import *
from tkinter import colorchooser
from PIL import Image , ImageTk,ImageFont,ImageDraw
from tkinter import filedialog
from tkinter import messagebox
import glob
import os

FunctNo = 0
image_list =[]
image =Image.open("guru-gobind-singh.jpg")
image_FORMAT =image.format
img_change_arr=[image]
file_path =os.getcwd()
canvas_img = None
imageid = None
delta = 0.75
imscale = 1.0
rect_x = 0,
rect_y = 0,
rect_x1 = 0
rect_y1 = 0
H_scale=0
V_scale=0
color = "#000000"
color2="#000000"
color_RGB=(0,0,0)
img_resize_width=200;
img_resize_height=200;
zoom=False
cr_box=[0,0,1394,893]
zoomed_img=image

class ImgProcessing:
    global image
    tc=image


    # --------------------------------------------------------
    # --------------- INITIALIZE -----------------------
    # --------------------------------------------------------
    def __init__(self,current_inst, inst_listbox,user_input,window,canvas_image_holder,Scale_inputH,Scale_inputV,color_btn, color2_btn,status_label,image_frame):
        global image, img_change_arr

        self.current_inst=current_inst
        self.inst_listbox=inst_listbox
        self.user_input=user_input
        img_change_arr = [image]
        self.window=window
        Image.MAX_IMAGE_PIXELS = 1000000000
        self.canvas_image_holder=canvas_image_holder
        self.Scale_inputH=Scale_inputH
        self.Scale_inputV=Scale_inputV
        self.color_btn=color_btn
        self.color2_btn = color2_btn
        self.status_label=status_label

        self.image_frame=image_frame
        #BIND
        self.item = self.canvas_image_holder.create_rectangle(0, 0, 0, 0)
        self.canvas_image_holder.bind('<MouseWheel>', self.wheel)
        self.canvas_image_holder.bind('<Button-5>', self.wheel)
        self.canvas_image_holder.bind('<Button-4>', self.wheel)
        self.canvas_image_holder.bind("<ButtonPress-1>", self.motion_start)
        self.canvas_image_holder.bind('<B1-Motion>', self.motion_end)
        self.Scale_inputH.bind('<B1-Motion>', lambda event:self.scaleH(event,image))
        self.Scale_inputV.bind('<B1-Motion>',lambda event:self.scaleV(event,image))


        #-------------------------- INITIALIZATION END HERE ---------------------------
        ###############################################################################





#--------------------------------------------------------
# --------------- CALL FUNCTION ON OK Button-------------------
#--------------------------------------------------------

    def call_functions(self):
        global FunctNo, image, img_change_arr


        print(FunctNo)
        if FunctNo == 1:
            self.crop(image)
        elif FunctNo ==2:
            self.border(image)
        elif FunctNo ==3:
            self.blackNwhite(image)
        elif FunctNo ==4:
            self.resize(image)
        elif FunctNo ==5:
            self.convert(image)
        elif FunctNo ==6:
            self.watermark(image)
        elif FunctNo ==7:
            self.rotate(image)
        elif FunctNo ==8:
            self.flip(image)
        elif FunctNo ==9:
            img_change_arr.append(image)
            self.draw_text(image)
        elif FunctNo ==10:
            self.save_image(image)
        elif FunctNo ==11:
            self.select_image()
        self.current_image_update(image)
        img_change_arr.append(image)
        self.canvas_image_holder.coords(self.item,0, 0, 0, 0)
        self.current_inst.delete(0.0, END)
        self.user_input.delete(0, END)
        self.current_inst.insert(END,"Select operations to perform:")
        if FunctNo !=11:
            self.inst_listbox.delete(0, END)

#####################################################################################
    ######################################################################
    ######################################################################
        ##########################################################
            ##############################################








    # --------------------------------------------------------
    # --------------- SET COLORS -----------------------------
    # --------------------------------------------------------

    def set_color(self):
        global color, color_RGB
        clr= colorchooser.askcolor(title="Choose Primary color")
        color=clr[1]
        color_RGB=tuple(map(int,clr[0]))
        self.color_btn.configure(bg=color)
        self.window.update()
        print(self.image_frame.winfo_width())
        print(self.image_frame.winfo_height())
    def set_color2(self):
        global color2
        clr= colorchooser.askcolor(title="Choose Secondary color")
        color2=clr[1]
        self.color2_btn.configure(bg=color2)

    # --------------------------------------------------------
    # --------------- SET COLORS END-----------------------------
    # --------------------------------------------------------



    # --------------------------------------------------------
    # --------------- SCALE BUTTONS Functions  ---------------
    # --------------------------------------------------------

    def scaleH(self,event,img):
        global H_scale, V_scale,FunctNo,color2
        # FOR BORDER
        if FunctNo==2:
            image_size=img.size
            H_scale= self.Scale_inputH.get()
            brV, brH = V_scale, H_scale
            if (brV >= 3001 or brH >= 3001):
                messagebox.showwarning("Border Size Too big",
                                       "Max allowed border size is: vertical:3000px horizontal:3000px ")
            else:
                new_size = (image_size[0] + brH, image_size[1] + brV)

                br_color =color2
                br_im = Image.new("RGB", new_size, br_color)
                br_im.paste(img, (int((new_size[0] - image_size[0]) / 2), int((new_size[1] - image_size[1]) / 2)))
                self.show_image(br_im)
                self.user_input.delete(0, END)
                msg = str(brV) + " " + str(brH)
                self.user_input.insert(0, msg)
        # For Rotate
        elif FunctNo==7:
            degree = H_scale= self.Scale_inputH.get()
            rotate_im = img.rotate(degree)
            self.show_image(rotate_im)
            msg = H_scale
            self.user_input.delete(0, END)
            self.user_input.insert(0, msg)



    def scaleV(self,event,img):
        global H_scale, V_scale, FunctNo, color
        if FunctNo == 2:
            image_size=img.size
            V_scale= self.Scale_inputV.get()
            brV, brH = V_scale, H_scale
            if (brV >= 3001 or brH >= 3001):
                messagebox.showwarning("Border Size Too big",
                                       "Max allowed border size is: vertical:3000px horizontal:3000px ")
            else:
                new_size = (image_size[0] + brH, image_size[1] + brV)
                br_color = color
                br_im = Image.new("RGB", new_size, br_color)
                br_im.paste(img, (int((new_size[0] - image_size[0]) / 2), int((new_size[1] - image_size[1]) / 2)))
                self.show_image(br_im)
                self.user_input.delete(0, END)
                msg= str(brV)+" "+str(brH)
                self.user_input.insert(0, msg)

    # --------------------------------------------------------
    # --------------- SCALE BUTTONS END ---------------
    # --------------------------------------------------------





    # --------------------------------------------------------
    # --------------- DRAW CROP AREA ---------------
    # --------------------------------------------------------

    def motion_start(self,event):
        global rect_x, rect_y, rect_x1, rect_y1,image
        x, y = event.x, event.y
        rect_x = x
        rect_y = y
        rect_x1 = x
        rect_y1 = y
        event.widget.coords(self.item, 0, 0, 0, 0)
        #box=[x-200, y-200,x+200,y+200]
        #img=image
        #img=img.crop(box)
        #self.show_image(img)
        #img.show()
        #print("croped")
        #self.canvas_image_holder.scan_mark(event.x, event.y)


    def motion_end(self,event):
        global rect_x, rect_y, rect_x1, rect_y1, FunctNo,cr_box,image
        x, y = event.x, event.y
        rect_x1 = x
        rect_y1 = y
        if FunctNo==1:
            self.user_input.delete(0, END)
            msg = str(rect_x) + " " + str(rect_y)+" "+str(rect_x1) + " " + str(rect_y1)
            self.user_input.insert(0, msg)
            self.canvas_image_holder.coords(self.item, rect_x, rect_y, rect_x1, rect_y1)
        else:

            imgRatio=image.size[0]/image.size[1]
            ydif=abs(rect_y1-rect_y)
            xdif=abs(rect_x1-rect_x)
            # Right to left
            if(rect_x>rect_x1):
                if ( (cr_box[2] + xdif <= image.size[0]) and (cr_box[2] + xdif) >= 0 ):
                    cr_box=[ cr_box[0]+(xdif),  cr_box[1],cr_box[2]+(xdif),cr_box[3]]
                else:
                    xFix=abs(image.size[0]-cr_box[2])
                    cr_box = [cr_box[0] + xFix, cr_box[1], cr_box[2]+xFix, cr_box[3]]

            #Left to right
            elif(rect_x1>rect_x):
                if ((cr_box[0]-xdif>=0) and (cr_box[2]-xdif)<=image.size[0] ):
                    cr_box = [cr_box[0] - (xdif), cr_box[1], cr_box[2] - (xdif), cr_box[3]]
                else:
                    xFix = abs(0-cr_box[0])
                    cr_box = [0, cr_box[1], cr_box[2]-xFix, cr_box[3]]

            #top to bottom

            if (rect_y1 < rect_y):
                print(rect_y1)
                if ((cr_box[3] + ydif) <= image.size[1] and (cr_box[1] + ydif) >= 0):
                    cr_box =  cr_box = [cr_box[0], cr_box[1]+ ydif, cr_box[2], cr_box[3]+ydif]
                else:
                    yFix=abs(image.size[1]-cr_box[3])
                    cr_box = cr_box = [cr_box[0], cr_box[1] + yFix, cr_box[2], cr_box[3] + yFix]

            #bottom to top
            elif (rect_y1 > rect_y):
                if ((cr_box[1] - ydif) >= 0 and (cr_box[3] - ydif) <= image.size[1]):
                    cr_box =  cr_box = [cr_box[0], cr_box[1]- ydif, cr_box[2], cr_box[3]-ydif]
                else:
                    yFix = abs(0 - cr_box[1])
                    cr_box = cr_box = [cr_box[0], 0, cr_box[2], cr_box[3] - yFix]
            if cr_box[0] < 0: cr_box[0] = 0
            if cr_box[1] < 0: cr_box[1] = 0
            if cr_box[2] > image.size[0]: cr_box[2] = image.size[0]
            if cr_box[3] > image.size[1]: cr_box[3] = image.size[1]

        print(cr_box)
        self.show_image(image)


        #self.canvas_image_holder.scan_dragto(event.x, event.y, gain=1)



    # --------------------------------------------------------
    # --------------- DRAW CROP AREA ---------------
    # --------------------------------------------------------



    # --------------------------------------------------------
    # --------------- DRAG AND DROP IMAGE  Currently Disabled ---------------
    # --------------------------------------------------------
    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''


    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''

    # --------------------------------------------------------
    # --------------- DRAG AND DROP IMAGE  END ---------------
    # --------------------------------------------------------


    # --------------------------------------------------------
    # ---------------IMAGE ZOOM ON WHEEL Scroll --------------
    # --------------------------------------------------------
    def wheel(self,event):
        global delta, imscale,image,zoom,cr_box,zoomed_img
        ''' Zoom with mouse wheel '''

        scale = 1.0
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if image.size[0]>2500:
            Zoom_level=40
        elif image.size[0]>1800:
            Zoom_level=30
        else:
            Zoom_level=20

        #cr_box = [0, 0, zoomed_img.size[0], zoomed_img.size[1]]
        imgRatio=image.size[0]/image.size[1]
        if event.num == 5 or event.delta == -120:
            scale *= delta
            imscale *= delta
            zoom = False
            print("out")
            cr_box = [cr_box[0] -Zoom_level, cr_box[1] - Zoom_level, int(cr_box[2] +Zoom_level), int(cr_box[3]+(Zoom_level))]


        if event.num == 4 or event.delta == 120:
            scale /= delta
            imscale /= delta

            print("zoom")
            zoom = True
            cr_box=[cr_box[0]+Zoom_level,cr_box[1]+Zoom_level,int(cr_box[2]-Zoom_level), int(cr_box[3]-(Zoom_level))]

        cr_w = cr_box[0] - cr_box[2]
        cr_h = cr_box[1] - cr_box[3]
        req_cr_h = int(cr_w / imgRatio)
        cr_box[3] = abs(req_cr_h - cr_box[1])

        if cr_box[0] < 0: cr_box[0] = 0
        if cr_box[1] < 0: cr_box[1] = 0
        if cr_box[2]>image.size[0]: cr_box[2]=image.size[0]
        if cr_box[3]> image.size[1]: cr_box[3] = image.size[1]
        #print(f" {cr_box} BOX AFTER")
        #print(f"cord {event.x} y {event.y}")
        # LET THE RAM Breate more
        '''
                if (imscale>=3 and image.size[0]>1500) or (imscale>=3 and image.size[1]>1500) :
            messagebox.showwarning("Image ZOOM", "Currently Max image scale allowed is:3x")
            imscale=3
        elif (imscale>=4 and image.size[0]>1000) or (imscale>=4 and image.size[1]>1000) :
            messagebox.showwarning("Image ZOOM", "Currently Max image scale allowed is:4x")
            imscale=4
        elif (imscale>=5 and image.size[0]>500) or (imscale>=5 and image.size[1]>500) :
            messagebox.showwarning("Image ZOOM", "Currently Max image scale allowed is:5x")
            imscale=5
        elif imscale>6:
            imscale = 6
        '''


        cr_img=image

        #cr_img.crop()

        # Rescale all canvas objects
        x = self.canvas_image_holder.canvasx(event.x)
        y = self.canvas_image_holder.canvasy(event.y)
        self.canvas_image_holder.scale('all', 1, 1, 1, 1)
        self.show_image(image,x,y)
        #self.canvas_image_holder.configure(scrollregion=self.canvas_image_holder.bbox('all'))

    # --------------------------------------------------------
    # ---------------IMAGE ZOOM ON WHEEL END --------------
    # --------------------------------------------------------











    # --------------------------------------------------------
    # ---------------SHOW UPDATED IMAGE ----------------------
    # --------------------------------------------------------

    def show_image(self,img,x="0",y="0"):


        #Show image on the Canvas
        global imageid,image, img_resize_width,img_resize_height, FunctNo,image_FORMAT,cr_box,zoom,zoomed_img,imscale
        imageGet=img
        self.window.update()
        winW = self.image_frame.winfo_width()-20
        winH = self.image_frame.winfo_height()-20
        wH=winH
        wW=winW
        winR = winW / winH
        width, height = imageGet.size
        imgRatio = imageGet.size[0] / imageGet.size[1]


        actual_width=imageGet.size[0]
        actual_height=imageGet.size[1]
        #winW =int(winH*imgRatio)
        new_size = int(imscale * width), int(imscale * height)
        print(f" New Size={new_size} scale:{imscale}")

        if (new_size[0]>winW or new_size[1]>winH):


                cr_img=imageGet.copy()
                print(f"Image Ratio{imgRatio}")
                # CORRECT RATIO
                if (actual_width>actual_height):
                    winH=int(winW/imgRatio)
                    if (winH>wH):
                        winH=wH
                        winW = int(wH * imgRatio)


                else:
                    winW = int(winH * imgRatio)

                new_size = [winW, winH]

                if (winH<=actual_height or winW<=actual_width):

                    cr_w= cr_box[0]-cr_box[2]
                    cr_h= cr_box[1]-cr_box[3]
                    req_cr_h=int(cr_w / imgRatio)
                    #cr_box[3]= abs(req_cr_h-cr_box[1])
                    #cr_box[3] = cr_box[3]

                    print(f" {cr_box} box h {req_cr_h}")
                    imageGet =cr_img.crop(cr_box)
                    print(f"image size={imageGet.size[0]}{ imageGet.size[1]}")
                    print("First IF")
                else:
                    #winH = int(winW / imgRatio)
                    #new_size = [winW, winH]
                    #print(f"image size={imageGet.size[0]}{ imageGet.size[1]}")
                    #cr_box[2]=int(cr_box[3]*imgRatio)
                    #print(cr_box)
                    #cr_img = imageGet.resize(new_size, Image.ANTIALIAS)
                    cr_img.crop(cr_box)
                    imageGet = cr_img.crop(cr_box)

                    zoomed_img=imageGet
                    #print(f"Second I{cr_box}")


                #print(f"B ratio{bRatio}  win ratio{winR}")
                #print("YES")
                #print(cr_box)
                #print(new_size)
                #imageGet=imageGet
                imagetk = ImageTk.PhotoImage(imageGet)
                imagetk = ImageTk.PhotoImage(imageGet.resize(new_size))



        else:
            imagetk = ImageTk.PhotoImage(imageGet.resize(new_size))
            winH=new_size[1]
            winW=new_size[0]
            cr_box=[0,0,imageGet.size[0],imageGet.size[1]]
            print("OUTER")


        if imageid:
            self.canvas_image_holder.delete(imageid)
            imageid = None
            self.canvas_image_holder.imagetk = None  # delete previous image from the canvas

        img_resize_width=new_size[0]
        img_resize_height=new_size[1]

        imageid = self.canvas_image_holder.create_image((0, 0),anchor=NW, image=imagetk)
        self.canvas_image_holder.configure(width=winW, height=winH)
        self.canvas_image_holder.lower(imageid)  # set image to background
        self.canvas_image_holder.imagetk = imagetk
        #cr_box = [0, 0, new_size[0]-2, new_size[1]-2]










        if FunctNo==4:
            self.user_input.delete(0, END)
            msg = str(img_resize_width) + " " + str(img_resize_height)
            self.user_input.insert(0, msg)
        # canvas_image_holder.bind('<ButtonPress-1>', move_from) DRAG DROP
        # canvas_image_holder.bind('<B1-Motion>', move_to)

        # -------------------------- UPDATE STATUS LABEL ----------------------
        msg="Actual Image Size:"+str(imageGet.size[0])+"x"+str(imageGet.size[1])+", Image Scale:"+str(round(imscale, 2))+"x"+", Format="+image_FORMAT
        self.status_label.configure(text=msg)


    # --------------------------------------------------------
    # ---------------SHOW UPDATED IMAGE END ----------------------
    # --------------------------------------------------------



















    def disp_image(self):
        global image
        image.show()

############################################################
#--------------------------------------------------------
# --------------- GET USER INPUTS -----------------------
#--------------------------------------------------------
    def get_inputs(self,strReturn=False):
        result= str(self.user_input.get())

        if not self.user_input.get():
            result = "0"

        else:
            result = str(self.user_input.get())
            print(result)
        if strReturn:
            return list(map(str, result.split()))
        else:
            return list(map(int, result.split()))

#-------------------------------------------------------



# --------------------------------------------------------
# --------------- SELECT working folder -----------------------
# --------------------------------------------------------
    def choose_file_path(self):
        global file_path
        current_path=filedialog.askdirectory()
        if current_path:
            file_path = current_path
            messagebox.showinfo("info", "NEW Working Folder Selected")

# --------------------------------------------------------
# --------------- SELECT working folder -----------------------
# --------------------------------------------------------



# --------------------------------------------------------
# --------------- ON EXIT -----------------------
# --------------------------------------------------------
    def on_Exit(self):

        if messagebox.askyesno("Exit","Do you want to exit the window?"):
            self.window.quit()



# --------------------------------------------------------
# --------------- Image Information -----------------------
# --------------------------------------------------------
    def image_info(self):
        global image,image_FORMAT
        size=image.size
        size=list(map(str,size))
        print(size)
        msg="Width:"+size[0]+"px\nHeight: "+size[1]+"px\n Format: "+image_FORMAT
        messagebox.showinfo("Image Info", msg)


# --------------------------------------------------------
# --------------- Show in Folder -----------------------
# --------------------------------------------------------
    def show_folder(self):
        global file_path
        path = file_path
        os.system('xdg-open "%s"' % path)
#--------------------------------------------------------
# --------------- UPDATE CURRENT IMAGE -----------------------
#--------------------------------------------------------

    def current_image_update(self,img):

        """
                global canvas_img

        img_size = img.size
        if img_size[0] < 600:
            mul = 600 / img_size[1]
            w = int(img_size[0] * mul)
            h = int(img_size[1] * mul)
            if w > 600: w = 600
            rsize_im = img.resize((w, h))
        else:
            ratio = img_size[0] / 600
            w = int(img_size[0] / ratio)
            if w > 600: w = 600
            rsize_im = img.resize((w, int(img_size[1] / ratio)))
        disp_imges = ImageTk.PhotoImage(img)

        # rsize_im.show()
        if canvas_img:
            self.canvas_image_holder.delete(canvas_img)
            canvas_img = None
            self.canvas_image_holder.disp_imges = None

        canvas_img = self.canvas_image_holder.create_image(0, 0, anchor=NW, image=disp_imges)

        self.canvas_image_holder.lower(canvas_img)
        self.canvas_image_holder.disp_img = disp_imges
        :param img:
        :return:
        """
        self.show_image(img)



#--------------------------------------------------------
# --------------- CURRENT INSTRUCTION -----------------------
#--------------------------------------------------------

    def current_instruction(self,msg):
        self.current_inst.delete('0.0', END)
        self.current_inst.insert(INSERT, msg)


#--------------------------------------------------------
# --------------- LIST / CHOICE INPUT -----------------------
#--------------------------------------------------------
    def list_choice(self,lists):
        self.inst_listbox.delete(0, END)
        for choice in lists:
            self.inst_listbox.insert(END, choice)

#--------------------------------------------------------
# --------------- ON LIST SELECT -----------------------
#--------------------------------------------------------

    def onselect(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.user_input.delete(0, END)
        self.user_input.insert(0, index)


#--------------------------------------------------------
# --------------- SELECT IMAGE -----------------------
#--------------------------------------------------------

    def select_image_msg(self):
        global FunctNo,image_list,file_path


        cwd = file_path
        msg = "Select Image to Edit:"
        self.current_instruction(msg)
        ext_names = ["JPG", "PNG", "JPEG", "GIF", "BMP", "PPM", "TIFF", "MPM"]
        image_list = []
        for ext in ext_names:
            image_list = glob.glob(cwd + "/*." + ext) + image_list
            image_list = glob.glob(cwd + "/*." + str(ext).lower()) + image_list
        img_choice=[i.replace(cwd+"/",'') for i in image_list]
        for i in range(len(img_choice)):
            img_choice[i]=" "+str(i)+". "+img_choice[i]
        self.list_choice(img_choice)
        FunctNo =11
        print(image_list)




    def select_image(self):
        global FunctNo, image_list,image,image_FORMAT, img_change_arr,cr_box,imscale
        input=self.get_inputs()
        image_name=image_list[input[0]]
        image=Image.open(image_name)
        image_FORMAT=image.format
        img_change_arr.append(image)
        #
        imscale=1.0
        cr_box=[0,0,image.size[0],image.size[1]]


# ------------------------------------------------------






#--------------------------------------------------------
# --------------- SAVE IMAGE -----------------------
#--------------------------------------------------------
    def save_image(self,img):
        global image,image_FORMAT
        ext = image_FORMAT
        print(ext)
        ext_names = [".jpg", '.png', '.jpeg', ".gif", ".mpm", ".ppm", ".tiff",".bmp"]
        save_img="newEdit"
        path_name = filedialog.asksaveasfilename()
        if path_name:
            save_img = path_name
        # MAKE SURE USER image name is with extension
        with_ext = True
        for s_img in ext_names:
            if s_img in save_img:
                with_ext = True
                break;
            else:
                with_ext = False

        if not with_ext: save_img = save_img + "." + ext
        img.save(save_img)
        messagebox.showinfo("info", save_img+" saved")

#---------------------------------------------------------



# --------------- PROCESS Functions --------------------------------
# ------------------------------------------------------------------
#------------------------------------------------------------------

    # --------------------------------------------------------
    # --------------- CANCEL/ UNDO -----------------------
    # --------------------------------------------------------

    def cancelUndo(self):
        global img_change_arr,FunctNo,image
        changes = len(img_change_arr)

        if changes>=0:
            image=img_change_arr[changes-1]
            self.show_image(image)
            if changes>2:
                img_change_arr = img_change_arr[:-1]





    # --------------------------------------------------------
    # --------------- CROP-----------------------
    # --------------------------------------------------------
    def get_crop(self):
        global rect_x, rect_y, rect_x1, rect_y1, imscale,img_resize_width,img_resize_height,image

        if rect_x>rect_x1:
            temp=rect_x
            rect_x=rect_x1
            rect_x1=temp
            temp=rect_y
            rect_y=rect_y1
            rect_y1=temp

        if imscale==1:
            crop_coord = (rect_x, rect_y, rect_x1, rect_y1)
        elif imscale>1:
            crop_coord = (int(rect_x/imscale),int(rect_y/imscale), int(rect_x1/imscale), int(rect_y1/imscale))
        else:
            imScal= image.size[0]/img_resize_width
            #print(f" RESIZE= {img_resize_width} {img_resize_height}")
            crop_coord = (int((rect_x * imScal)), int((rect_y * imScal)), int((rect_x1 * imScal)), int((rect_y1 * imScal)))

        return crop_coord


    def crop(self,img):
        global rect_x, rect_y, rect_x1, rect_y1,image


        ccord=self.get_crop()
        print(rect_x, rect_y, rect_x1, rect_y1)
        #input=self.get_inputs()
        #x1, y1, x2, y2 = input[0],input[1],input[2],input[3]
        #box = (x1, y1, x2, y2)
        cropped_image = img.crop(ccord)
        image=cropped_image.copy()


    # --------------------------------------------------------
    # --------------- BORDER -----------------------
    # --------------------------------------------------------
    def border(self,img):
        global image,color
        image_size = img.size
        input=self.get_inputs(True)
        brV, brH= int(input[0]),int(input[1])
        if (brV>=3001 or brH>=3001):
            messagebox.showwarning("Border Size Too big", "Max allowed border size is: vertical:3000px horizontal:3000px ")
        else:
            new_size = (image_size[0]+brH, image_size[1]+brV)
            br_color=color
            br_im = Image.new("RGB", new_size,  br_color)
            br_im.paste(img,  (int((new_size[0]-image_size[0]) / 2), int((new_size[1]-image_size[1])/2)))
            image = br_im.copy()


    # --------------------------------------------------------
    # --------------- BLACK AND WHITE -----------------------
    # --------------------------------------------------------
    def blackNwhite(self,img):
        global image
        input = self.get_inputs()
        ch= input[0]
        if ch==2:
            bW_im = img.convert('1')
        else:
            bW_im =img.convert('L')
        image = bW_im.copy()


    # --------------------------------------------------------
    # --------------- RESIZE -----------------------
    # --------------------------------------------------------
    def resize(self,img):
        global image
        input = self.get_inputs()
        wd, hg = input[0],input[1]
        if (wd>=7501 or hg>=5501):
            messagebox.showwarning("Image Size Too BIG","Max Allowed Width:7500 & height:5500")
        else:
            resize_im= img.resize((wd, hg))
            image = resize_im.copy()


    # --------------------------------------------------------
    # --------------- Convert -----------------------
    # --------------------------------------------------------
    def convert(self,img):
        global image
        conv_im=img.copy()
        image = conv_im.copy()


    # --------------------------------------------------------
    # --------------- WATERMARK -----------------------
    # --------------------------------------------------------
    def watermark(self,img):
        global image

        ext_type=[".jpg", '.png', '.jpeg', ".gif", ".mpm", ".ppm", ".tiff",".bmp"]
        ext_type=[x.lower() for x in ext_type]+[x.upper() for x in ext_type]
        logo_path=filedialog.askopenfilenames( title="Choose the Watermark Image",filetypes=[('image files',ext_type ),('all files', '.*')])
        print(logo_path[0])
        if logo_path:
            logo = Image.open(logo_path[0])
        else:
            logo = Image.open("slogo.PNG")
        water_im = img.copy()
        input=self.get_inputs()
        loc=input[0]

        # LOCATION OF THE WATERMARK
        if loc == 1:
            position = (0,0)
        elif loc == 2:
            position = ((water_im.width - logo.width), 0)
        elif loc == 3:
            position = (0,(water_im.height - logo.height))
        elif loc == 4:
            position = ((water_im.width - logo.width), (water_im.height - logo.height))
        elif loc == 5:
            position = (int(water_im.width/2), int(water_im.height/2))
        else:
            position = ((water_im.width - logo.width), (water_im.height - logo.height))

        # BACKGROUND FOR THE Watermark
        water_im.paste(logo, position, logo)
        image=water_im.copy()


    # --------------------------------------------------------
    # --------------- ROTATE -----------------------
    # --------------------------------------------------------
    def rotate(self,img):
        global image
        input = self.get_inputs()
        degree = input[0]
        rotate_im= img.rotate(degree)
        image = rotate_im.copy()

    def flip(self,img):
        global image
        input = self.get_inputs()
        trans_choice= input[0]
        if trans_choice==1:
            flip_img= img.transpose(Image.FLIP_LEFT_RIGHT)
        elif trans_choice==2:
            flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        elif trans_choice==3:
            flip_img = img.transpose(Image.TRANSPOSE)
        else:
            flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        image = flip_img.copy()


    # --------------------------------------------------------
    # --------------- DRAW TEXT -----------------------
    # --------------------------------------------------------

    def font_get(self,txt,img):
        global image, color_RGB
        img_fraction = 0.80
        fontsize = 1
        font = ImageFont.truetype("arial.ttf", fontsize)
        while font.getsize(txt)[0] < img_fraction * img.size[0]:
            fontsize += 1
            font = ImageFont.truetype("arial.ttf", fontsize)
        return fontsize

    def draw_text(self,img):

        global image


        draw = ImageDraw.Draw(image)
        txt = str(self.user_input.get())
        while txt[-1:] == "#":
                txt = txt[:-1]
        if len(txt)>0:
            txt_list = txt.split("#")
            prev = 25
            for Tlist in txt_list:
                fontsize = self.font_get(Tlist,img)
                fontsize -= 1
                font = ImageFont.truetype("arial.ttf",fontsize)
                print(color_RGB)
                draw.text((10, prev), Tlist, font=font, fill=color_RGB)
                prev = prev + 20 + fontsize






# ---------------------FUNCTIONS END HERE -------------------------




# --------------- MESSAGE for Functions --------------------------------
# ------------------------------------------------------------------
#-------------------------------------------------------------------



    def save_image_msg(self,image):
        global FunctNo
        FunctNo = 10
        msg = "\nEnter the image Name to Save: "
        #self.current_instruction(msg)
        self.call_functions()


    def crop_msg(self,img):
        global FunctNo,image
        FunctNo = 1
        image_size = image.size
        image_size=list(map(str,image_size))
        msg ="Image is of / Width:"+image_size[0]+"Height:"+image_size[1]
        msg = msg +"\nEnter Starting (x1,y1) & and Ending (x2,y2) coordinates:"
        self.current_instruction(msg)



    def border_msg(self,image):
        global FunctNo
        FunctNo = 2
        image_size = image.size
        msg="\nEnter the border Size Vertically and Horizontally in px: "
        self.current_instruction(msg)


    def blackNwhite_msg(self,image):
        global FunctNo
        FunctNo = 3

        lists= ["","1.Grayscale","2. Pure Black & White"]
        self.list_choice(lists)
        msg = "Enter your choice: (default Grayscale)"
        self.current_instruction(msg)




    def resize_msg(self,image):
        global FunctNo
        FunctNo = 4
        msg="\nEnter the desired Width and Height of the image: "
        self.current_instruction(msg)


    def convert_msg(self,img):
        global FunctNo,image
        FunctNo = 5

        msg = "Your Current Image is in "+image.format+" format.\n Click on Save button to change the format"
        self.current_instruction(msg)



    def watermark_msg(self,image):
        global FunctNo

        FunctNo = 6
        lists= ["","1. Top Left","2. Top Right","3. Bottom Left","4. Bottom Right","5. Center"]
        self.list_choice(lists)
        msg = "Choose Location for watermark:\n# default bottom left\n Enter your choice:"
        self.current_instruction(msg)




    def rotate_msg(self,image):
        global FunctNo
        FunctNo = 7
        msg = "Enter the degrees to rotate the image: "
        self.current_instruction(msg)


    def flip_msg(self,image):
        global FunctNo
        FunctNo = 8
        lists= ["","1. Left to Right","2. TOP to bottom","3. Transpose"]
        self.list_choice(lists)
        msg = "Enter your choice:"
        self.current_instruction(msg)


    def draw_text_msg(self,image):
        global FunctNo
        FunctNo = 9
        msg = "Enter the Text you want to paste on image: SPLIT Lines Using '#'"
        self.current_instruction(msg)


#im = Image.open("Ba_b_do8mag_c6_big.png")
#rgb_im = im.convert('RGB')
#rgb_im.save('colors.jpg',quality=95) )
