import time
import pyautogui
from PIL import ImageGrab  

DETECTION_BOX = (500, 400, 550, 450)

def capture_trigger_area():
    image = ImageGrab.grab(bbox=DETECTION_BOX)
    return image.convert('L')

def start_bot():
    print("Bot starting in 3 seconds... Click onto your game window now!")
    time.sleep(3)
    
    baseline = capture_trigger_area()
    baseline_pixels = list(baseline.getdata())
    
    print("Bot is ACTIVE! Press Ctrl+C in Command Prompt to stop.")
    while True:
        current = capture_trigger_area()
        current_pixels = list(current.getdata())
        
        diff = sum(abs(c - b) for c, b in zip(current_pixels, baseline_pixels))
        
        if diff > 1000:
            pyautogui.press('space')
            time.sleep(0.25)
            
if __name__ == "__main__":
    start_bot()
