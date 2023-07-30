import os
from PIL import Image
from tkinter import filedialog
import struct

bit_paint = bytearray()
targ_file = ""
targ_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select PNG or BMP", filetype=(('PNG file', '*.png'),('BMP file', '*.bmp'),("ALL file",'*.*')))
new_bin_file = ""

more_than_16 = False

if len(targ_file) != 0 :

    openpic = Image.open(targ_file)
    w,h = openpic.size

    n=len(targ_file)-5
    while n!= 0 and targ_file[n] != '/':
        new_bin_file = targ_file[n] + new_bin_file
        n -= 1 
    new_bin_file += " Converted.bin"

    b1, b2 = 0 , 0

    list_colors = []

    if w == 128 and h % 8 == 0:

        for y in range(0, h, 8):
            for x in range (0, w, 8):
                for iz in range(0, 8):
                    for ix in range(0, 8, 2):
                        RGB_1, RGB_2 = openpic.getpixel((x+ix,y+iz)) , openpic.getpixel((x+ix+1,y+iz))
                        if len(list_colors) < 16:
                            if not RGB_1 in list_colors:
                                list_colors.append(RGB_1)
                            if not RGB_2 in list_colors:
                                list_colors.append(RGB_2)
                        b1, b2 = 0 , 0
                        if RGB_1 in list_colors:
                            b1 = list_colors.index(RGB_1)
                        if RGB_2 in list_colors:
                            b2 = list_colors.index(RGB_2)
                        if more_than_16 == False and len(list_colors) == 16 and (not RGB_1 in list_colors or not RGB_2 in list_colors):
                                more_than_16 = True
                                print("This Picture has more than 16 colors")                        
                        bin_color = struct.pack("B", b1 * 16 + b2)
                        bit_paint += bin_color
                    
        out_file = open(new_bin_file, "wb+")
        out_file.write(bit_paint)
        out_file.close()

        print("Bin file done!")

    else:
        if w != 128:
            print("The picture's width must be 128 long")
        if h % 8 != 0:
            print("The picture's height have to be a multiple of 8")
else:
    print("No File Selected")

