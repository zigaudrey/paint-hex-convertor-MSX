![Paint-Bin Convetor - Sega Genesis BANNER](https://github.com/zigaudrey/paint-hex-convertor-MSX/assets/129554573/44e32b22-2809-4761-8027-f73d21a9ebd8)

# Paint - Hex Convertor Scripts (Sega Genesis / Megadrive)
Python Scripts that convert Picture into Bin file and vice-versa for Sega Genesis / MegaDrive Sprite Editing.

## Setup
1. If you don't have PIL, **open the command prompt and install it with PIP**
2. Open one of the scripts in **command prompt for PIL lib to work**

## Paint-to-hex Steps
3. Create a separate file for the palette. **Be sure the colors match with the picture you will using**
3. Choose a palette (image). **It have to have a total of 16 pixels**
3. Choose a sprite sheet (image). **Its dimensions both should be a divisible of 8**
3. Mention if **the picture is displayed vertically or horizontally.**
3. **Two bin files will be created**, ready to replace data in the ROM

## Hex-to-paint Steps
3. Get the Palette and Sprites data from the ROM. **Use the [GSavestate](https://www.romhacking.net/utilities/344/) and [CHR-YY](https://www.romhacking.net/utilities/119/) repectivily to locate them and create new files with an Hex editor. _Don't forget to mention the offset_**
3. Choose a palette (bin file). **Its lenght has to be 32**
3. Choose a sprite sheet (bin file). **Its lenght has to be a divisble of 32 (one tile)**
3. Choose **the number of tiles for the width**
3. Choose if **you want to display the tiles vertically or horizontally.**
3. **Two images files will be created**, ready to be edited in drawing tools

## Result
![Fusion_VvzzC6zCaj-Toejam-and-Earl---Logo-Edit](https://github.com/zigaudrey/paint-hex-convertor-MSX/assets/129554573/c34f6f9e-147c-44a5-9d26-45d70f90f204) Toejam & Earl

## Update
**1st Febuary of 2024**: Added the option to display verticallly/horizontally.

## History
Previously know as paint-to-bin-MSX, the repository is upgraded into a both-way convertor. Now, you need two files (Palette and Sprite Sheet) for paint-to-hex script.
Turning a Bin data into Image is an ambitious idea. I am glad to turn this dream come true. For someone visual, Sprite Editing become easier (and better than YY-CHR).

## Similar Tool
+ [Paint-Hex Convertor (Gameboy Advance / DS 16-Colors)](https://github.com/zigaudrey/paint-hex-convertor-GBA-DS)
+ [Paint - Hex Convertor DS-256 colors](https://github.com/zigaudrey/paint-hex-convertor-DS-256/tree/main)
