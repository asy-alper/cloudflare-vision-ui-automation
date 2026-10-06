import pyautogui
import time
import random
import os

print("[INFO] Vision-Based UI Automation Initialized.")
print("[INFO] Searching for target UI element...")
print("[INFO] FAILSAFE ENABLED: Move cursor to any screen corner to abort.")

target_image = "image_365c2f.png"

if not os.path.exists(target_image):
    print(f"[ERROR] Target file '{target_image}' not found in the current directory.")
    exit()

pyautogui.FAILSAFE = True

screen_width, screen_height = pyautogui.size()

left_bound = int(screen_width * 0.30)
top_bound = int(screen_height * 0.10)
scan_width = int(screen_width * 0.40)
scan_height = int(screen_height * 0.80)

roi = (left_bound, top_bound, scan_width, scan_height)

print(f"[INFO] Dynamic ROI established: {roi}")

while True:
    try:
        location = pyautogui.locateCenterOnScreen(
            target_image, 
            confidence=0.8, 
            grayscale=True, 
            region=roi
        )
        
        if location is not None:
            current_time = time.strftime('%H:%M:%S')
            print(f"[{current_time}] [SUCCESS] UI Element detected at coordinates: X:{location.x}, Y:{location.y}")
            
            original_x, original_y = pyautogui.position()
            
            movement_duration = random.uniform(0.3, 0.7)
            pyautogui.moveTo(location.x, location.y, duration=movement_duration, tween=pyautogui.easeInOutQuad)
            
            time.sleep(random.uniform(0.1, 0.3))
            
            pyautogui.click()
            print("[INFO] Interaction event dispatched. Awaiting system response...")
            
            pyautogui.moveTo(location.x, location.y + 200, duration=0.3)
            
            time.sleep(4)
            
    except pyautogui.ImageNotFoundException:
        pass
    except Exception as e:
        pass

    time.sleep(1.5)