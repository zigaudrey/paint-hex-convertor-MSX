![Paint-Bin Convetor - Sega Genesis BANNER](https://github.com/zigaudrey/paint-hex-convertor-MSX/assets/129554573/44e32b22-2809-4761-8027-f73d21a9ebd8)

# Paint - Hex Convertor Script (Sega Genesis / Megadrive)
Python Scripts that convert Picture into Bin file and vice-versa for Sega Genesis / MegaDrive.

## Setup
1. If you don't have PIL, **open the command prompt and install it with PIP**
2. Open one of the scripts in **command prompt for PIL lib to work**

## Paint-to-hex Steps
3. Create a separate file for the palette. **Be sure the colors match with the picture you will using**
3. Choose a palette (image). **It have to have a total of 16 pixels**
3. Choose a sprite sheet (image). **Its dimensions both should be a divisible of 8**
3. **Two bin files will be created**, ready to replace data in the ROM

## Hex-to-paint Steps
3. Get the Palette and Sprites data from the ROM. **Use the [GSavestate](https://www.romhacking.net/utilities/344/) and [CHR-YY](https://www.romhacking.net/utilities/119/) repectivily to locate them and create new files with an Hex editor. _Don't forget to mention the offset_**
3. Choose a palette (bin file). **Its lenght has to be 32**
3. Choose a sprite sheet (bin file). **Its lenght has to be a divisble of 32 (one tile)**
3. Choose **the number of tiles for the width**
3. **Two images files will be created**, ready to be edited in drawing tools

## Result
![Toejam and Earl - HUM Logo Mod](https://github.com/zigaudrey/paint-to-bin-MSX/assets/129554573/daaf9907-d925-4e45-83cf-df9ec2a5ee8d) Toejam & Earl Screenshot

## History
Previously know as paint-to-bin-MSX, the repository is upgraded into a both-way convertor. Now, you need two files (Palette and Sprite Sheet) for paint-to-hex script.
Turning a Bin data into Image is an ambitious idea. I am glad to turn this dream come true. For someone visual, Sprite Editing become easier (and better than YY-CHR).
