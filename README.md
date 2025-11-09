# badApple-esp8266
This is a project for ESP8266 with a 0.96-inch OLED screen, or rather, a project with Bad Apple animation at 16 fps. Feel free to use it, as there is no license required.

> ⚠️ **Note**: Due to memory limitations, this version is **not recommended for direct upload to ESP8266**. The full 47-second animation (~752 frames @ 16 FPS) exceeds the available flash memory (`irom0` segment). Use only for reference or adapt it for **ESP32** or **shorter clips**.

# How to use
Download the .bin firmware, use ESPWEBTOOL from Spacehuhn, and set 0x00000. when sending the firmware.
If you want to view the code, modify it, or do something else, download the Source Code, view it, and open the Arduino IDE to compile it.

# What's next?
Write in the comments if you want me to port DOOM to ESP32 or Arduino.
