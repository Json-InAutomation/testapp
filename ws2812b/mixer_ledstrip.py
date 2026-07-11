from rpi_ws281x import PixelStrip, Color
import time

LED_COUNT = 36
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    LED_FREQ_HZ,
    LED_DMA,
    LED_INVERT,
    LED_BRIGHTNESS,
    LED_CHANNEL
)

strip.begin()


def mixerLED():

    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(252, 252, 250))

    brightness = 255
    target = 85

    while brightness >= target:
        strip.setBrightness(brightness)
        strip.show()

        brightness -= 2      
        time.sleep(0.03)    


if __name__ == "__main__":
    mixerLED()
