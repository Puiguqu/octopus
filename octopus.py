import cv2
import numpy as np
import pyautogui
import time
from pynput.keyboard import Controller

# --- Setup ---
keyboard = Controller()
pyautogui.FAILSAFE = False  # prevent sudden abort

# Templates (place them in same folder as this script)
TEMPLATE_GATHER = "npc_gather.png"
TEMPLATE_FEED = "feed.png"

npc_template = cv2.imread(TEMPLATE_GATHER, cv2.IMREAD_GRAYSCALE)
feed_template = cv2.imread(TEMPLATE_FEED, cv2.IMREAD_GRAYSCALE)

def find_template(template, threshold=0.8):
    """Return center coordinates of template if found, else None"""
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        return (center_x, center_y)
    return None

def main():
    print("Starting script... Press Ctrl+C to stop.")

    while True:
        # --- Check NPC/Gather ---
        pos_gather = find_template(npc_template, threshold=0.8)
        if pos_gather:
            print("NPC/Gather found → Holding 'R' for 5s")
            keyboard.press('r')
            time.sleep(5)
            keyboard.release('r')
            # Move cursor away after holding R
            pyautogui.moveRel(-100, 0, duration=0.2)  # move left
            print("Released 'R' and moved cursor left")
            time.sleep(1)  # short cooldown

        # --- Check Feed ---
        pos_feed = find_template(feed_template, threshold=0.8)
        if pos_feed:
            print(f"Feed found at {pos_feed} → Click and hold for 5s")
            pyautogui.moveTo(pos_feed[0], pos_feed[1], duration=0.2)
            pyautogui.mouseDown()
            time.sleep(5)   # hold for 5s
            pyautogui.mouseUp()
            # Move cursor away
            pyautogui.moveRel(-100, 0, duration=0.2)  # move left
            print("Released mouse and moved cursor left")
            time.sleep(1)  # small delay

        time.sleep(0.5)  # scan interval

if __name__ == "__main__":
    main()
