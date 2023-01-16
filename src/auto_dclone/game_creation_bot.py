import os
import time
import pyautogui

from region import Region

class GameCreationBot:
    def __init__(self, launcher_path):
        self.launcher_path = launcher_path
        self.img_path = "../../assets/img"

    def run_diablo_2_automation(self, region):
        # Open bnet launcher
        os.startfile(self.launcher_path)

        # Choose the region where dclone is going to spawn
        region_icon = self.wait_for_image(f"{self.img_path}/region.png")
        pyautogui.click(region_icon)

        # Handle region select
        region_path = None
        if region == Region.AMERICA:
            region_path = f"{self.img_path}/america.png"
        elif region == Region.EUROPE:
            region_path = f"{self.img_path}/europe.png"
        else:
            region_path = f"{self.img_path}/asia.png"
        region_button = self.wait_for_image(region_path, confidence=0.7)
        pyautogui.click(region_button)

        # Start the game
        start_button = self.wait_for_image(f"{self.img_path}/start.png")
        pyautogui.click(start_button)

        # Skip for first intro
        self.wait_for_image(f"{self.img_path}/intro.png", realtime=True, confidence=0.5)
        pyautogui.press("space")

        # Skip for second intro
        self.wait_for_image(f"{self.img_path}/intro_2.png", realtime=True, confidence=0.5)
        pyautogui.press("space")

        # Skip any key screen
        self.wait_for_image(f"{self.img_path}/d2_any_key.png")
        pyautogui.press("space")

        # Click on the character name
        character_name = self.wait_for_image(f"{self.img_path}/character_name.png")
        pyautogui.click(character_name)

        # Press "Play" button
        play_button = self.wait_for_image(f"{self.img_path}/play.png")
        pyautogui.click(play_button)

        # Press "Hell" button
        hell_button = self.wait_for_image(f"{self.img_path}/hell.png")
        pyautogui.click(hell_button)


    def wait_for_image(
        self, image_path, timeout=120, realtime=False, grayscale=True, confidence=0.9
    ):
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Timed out waiting for image: {image_path}")
            image = pyautogui.locateOnScreen(
                image_path, grayscale=grayscale, confidence=confidence
            )
            if image:
                return image
            print(f"Waiting for image: {image_path}")
            if not realtime:
                time.sleep(5)