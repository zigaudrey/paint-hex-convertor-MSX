import os
import struct

from PIL import Image
from tkinter import filedialog

PAL_path = ""
PAL_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Pal File", filetype=(('BIN file', '*.bin'),("ALL file",'*.*')))

if len(PAL_path) != 0:
    PAL_open = open(PAL_path, 'rb')
    PAL_data = PAL_open.read()
    PAL_open.close()

    if len(PAL_data) == 32:

        PAL_List = []

        R, G, B = 0, 0, 0

        bin_hex = bytearray()
        for i in range(0,len(PAL_data),2):
            Dec_Color = struct.unpack(">L",b'\x00\x00' + PAL_data[i:i+2])[0]
            R = Dec_Color % 16 * 16
            G = (Dec_Color // 16) % 16 * 16
            B = (Dec_Color // 16 // 16) % 16 * 16
            PAL_List.append((R, G, B))

        if PAL_List.count(PAL_List[0]) != 16:

            if PAL_List[0] in PAL_List[1:]:
                print("The first color is doubled. Change to (0, 224, 224).")
                PAL_List[0] = (0, 224, 224)
            
            BIN_name = ""
            BIN_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Sprite Bin File", filetype=(('BIN file', '*.bin'),("ALL file",'*.*')))

            if len(BIN_name) != 0:

                BIN_path = open(BIN_name, "rb")
                BIN_file = BIN_path.read()
                BIN_path.close()

                if len(BIN_file) % 32 == 0:

                    n=len(BIN_name)-1
                    SHORT_name = ""
                    while n!= 0 and BIN_name[n] != '.':
                        n -= 1
                    n -= 1
                    while n!= 0 and BIN_name[n] != '/':
                        SHORT_name = BIN_name[n] + SHORT_name
                        n -= 1
                    
                    tile_COUNT = 0

                    while tile_COUNT == 0:
                        tile_COUNT = int(input("Choose Tile Number (4 to 32)"))
                        if 4 > tile_COUNT or tile_COUNT > 32 :
                            tile_COUNT = 0

                    display_MODE = ""

                    while display_MODE == "":
                        display_MODE = str(input("Is the picture displayed vertically or horizontally? v/h")).lower()
                        if display_MODE != "v" and display_MODE != "h":
                            display_MODE = ""

                    BIN_len = len(BIN_file) + (len(BIN_file) % (tile_COUNT * 32))

                    if display_MODE == "v":
                        w = 8 * tile_COUNT
                        h = BIN_len // (tile_COUNT * 32) * 8

                    else:
                        h = 8 * tile_COUNT
                        w = BIN_len // (tile_COUNT * 32) * 8
                        
                    OUTCOME= Image.new('RGB', (w , h))

                    Pointer = 0
                    n1, n2 = 0 ,0
                    if display_MODE == "v":
                        for y in range(0, h, 8):
                            for x in range (0, w, 8):
                                for iz in range(0, 8):
                                    for ix in range(0, 8, 2):
                                        if Pointer < len(BIN_file):
                                            Hex_Data = struct.pack("B", BIN_file[Pointer])[0]
                                            n1 = Hex_Data // 16
                                            n2 = Hex_Data - (n1 * 16)
                                            OUTCOME.putpixel((x+ix,y+iz), PAL_List[n1])
                                            OUTCOME.putpixel((x+ix+1,y+iz), PAL_List[n2])
                                            Pointer += 1
                    else:
                        for x in range(0, w, 8):
                            for y in range (0, h, 8):
                                for iz in range(0, 8):
                                    for ix in range(0, 8, 2):
                                        if Pointer < len(BIN_file):
                                            Hex_Data = struct.pack("B", BIN_file[Pointer])[0]
                                            n1 = Hex_Data // 16
                                            n2 = Hex_Data - (n1 * 16)
                                            OUTCOME.putpixel((x+ix,y+iz), PAL_List[n1])
                                            OUTCOME.putpixel((x+ix+1,y+iz), PAL_List[n2])
                                            Pointer += 1

                    OUTCOME.save(SHORT_name + " - " + str(tile_COUNT) + " Tiles.png")

                    PAL_OUTCOME= Image.new('RGB', (8 , 2))

                    np = 0
                    for y in range(2):
                        for x in range(8):
                            PAL_OUTCOME.putpixel((x,y), PAL_List[np])
                            np += 1

                    PAL_OUTCOME.save(SHORT_name + " Pal.png")

                    print("Image and Pal Datas Files Done!")
                            
                else:
                    print("The Sprite Bin File isn't a divisible of 32")

            else:
                print("No Sprite File Selected")

        else:
            print("Palette File Empty")

    else:

        print("The Palette Bin file has to be 32 long")

else:
    print("No Palette File Selected")
