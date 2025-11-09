#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "frames.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const uint32_t FRAME_TIME_MS = 1000 / FPS; // FPS it must be declared in frames.h
uint32_t currentFrame = 0;
unsigned long lastFrameTime = 0;

void setup() {
  Serial.begin(115200);
  
  Wire.begin(4, 5);           // SDA = D2 (GPIO4), SCL = D1 (GPIO5)
  Wire.setClock(400000);      // Fast-mode I2C (400 kHz)

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED not found!");
    for (;;);
  }

  display.ssd1306_command(SSD1306_COMSCANDEC);

  display.clearDisplay();
  display.display();
  delay(100);

  Serial.println("Bad Apple OLED Started");
}

void loop() {
  if (currentFrame >= frameCount) {
    // currentFrame = 0; // if you want an infinite animation loop, uncomment this code
    return;
  }

  unsigned long now = millis();
  if (now - lastFrameTime >= FRAME_TIME_MS) {
    lastFrameTime = now;

    display.clearDisplay();
    display.drawBitmap(
      0, 0,
      (const uint8_t*)pgm_read_ptr(&frames[currentFrame]),
      SCREEN_WIDTH, SCREEN_HEIGHT,
      SSD1306_WHITE
    );
    display.display();

    currentFrame++;
  }
}