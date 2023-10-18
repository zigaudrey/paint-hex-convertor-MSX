![image](https://github.com/zigaudrey/paint-to-bin-MSX/assets/129554573/101d3c2f-7eda-4955-98cd-6f1fec28a692)

# Paint to Bin Script (Sega Genesis / Megadrive)
A Python Script that convert a picture into a binary file for editing Sega Genesis/Megadrive sprites. Ready to be used in [YY-CHR tool](https://www.romhacking.net/utilities/119/).

## Step
1. After downloading the script, create an Virtual Environment and add the PIL Lib. [Check tutorial here](https://www.youtube.com/watch?v=IAvAlS0CuxI)
2. Run the script. The picture you will choose have to be **128 width long and the height has to be a multiple of 8**
3. To make the color picking easier, **add the palette at the top left of the picture** as seen below.
![image](https://github.com/zigaudrey/paint-to-bin-MSX/assets/129554573/e827bb99-cf82-4426-8c7e-3f8dc141fb4a)

To verify if this has 16 colors, open the picture in a software using palette (eg. GIMP)

4. A new BIN file will be created, ready to be used for the YY-CHR tool.

## Result
![Toejam and Earl - HUM Logo Mod](https://github.com/zigaudrey/paint-to-bin-MSX/assets/129554573/daaf9907-d925-4e45-83cf-df9ec2a5ee8d) Toejam & Earl Screenshot

## Personal Thought
YY-CHR is obsolete for Sega Genesis/Megadrive graphic, especially for someone visual. You can't shrink the window to have better sprite display and knowing what you are doing.
Instead, YY-CHR is more fitted to see which offset the sprite is and replace the data throught an Hex Editor, which what I did above. It seen YY-CHR is made for 2-bit graphic like NES/Virtual Boy.
I hope to find a tool that center on Sega graphics but the MOD scene for this console is too narrowed (too much Sonic MOD).
