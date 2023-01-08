from enum import Enum
from twilio.rest import Client
import requests
import time
import os
import pyautogui

from config import (
    URL,
    REGION,
    LADDER,
    HARDCORE,
    LAUNCHER_PATH,
    NOTIFICATION_ENABLED,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    SMS_FROM_NUMBER,
    SMS_TO_NUMBER,
    SMS_BODY,
)


class Region(Enum):
    AMERICA = "America"
    EUROPE = "Europe"
    ASIA = "Asia"


def main():
    print("Welcome to auto dclone bot!")
    print("This bot will:")
    print("1. Poll the api for dclone spawn")
    print("2. Send you a notification when dclone spawns")
    print("3. Start diablo 2 and create a game\n")
    print("Data courtesy of diablo2.io")
    print("https://diablo2.io/dclonetracker.php\n")
    print("Press any key to start polling")
    input()

    while True:
        region = poll_api()
        if region:
            print("Dclone is spawning! Go get him!")
            if NOTIFICATION_ENABLED:
                print("Sending email notification...")
                send_sms()
            print("Running diablo 2 automation...")
            run_diablo_2_automation(region)
            print("Bot initialized and waiting")
            print("Press any key to continue polling")
            input()
        print("Waiting 2 minutes before polling again...\n")
        time.sleep(120)


def poll_api():
    print("Polling api...")
    response = requests.get(
        URL, params={"ladder": LADDER, "hc": HARDCORE, "region": REGION}
    )
    data = response.json()
    for realm in data:
        region = (
            Region.AMERICA
            if realm["region"] == "1"
            else Region.EUROPE
            if realm["region"] == "2"
            else Region.ASIA
        )
        progress = realm["progress"]
        print(f"Dclone is on step: {progress} in {region.name}")
        if progress == "5" or progress == "6":
            return realm["region"]
    return None


def send_sms():
    print("Sending sms notification...")
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=SMS_FROM_NUMBER, body=SMS_BODY, to=SMS_TO_NUMBER
    )
    print("SMS sent!")
    print(message.sid)


def run_diablo_2_automation(region):
    # Open bnet launcher
    os.startfile(LAUNCHER_PATH)

    # Choose the region where dclone is going to spawn
    region_icon = wait_for_image("./assets/img/region.png")
    pyautogui.click(region_icon)

    # Handle region select
    region_path = None
    if region == Region.AMERICA:
        region_path = "./assets/img/america.png"
    elif region == Region.EUROPE:
        region_path = "./assets/img/europe.png"
    else:
        region_path = "./assets/img/asia.png"
    region_button = wait_for_image(region_path, confidence=0.7)
    pyautogui.click(region_button)

    # Start the game
    start_button = wait_for_image("./assets/img/start.png")
    pyautogui.click(start_button)

    # Skip for first intro
    wait_for_image("./assets/img/intro.png", realtime=True, confidence=0.5)
    pyautogui.press("space")

    # Skip for second intro
    wait_for_image("./assets/img/intro_2.png", realtime=True, confidence=0.5)
    pyautogui.press("space")

    # Skip any key screen
    wait_for_image("./assets/img/d2_any_key.png")
    pyautogui.press("space")

    # Click on the character name
    character_name = wait_for_image("./assets/img/character_name.png")
    pyautogui.click(character_name)

    # Press "Play" button
    play_button = wait_for_image("./assets/img/play.png")
    pyautogui.click(play_button)

    # Press "Hell" button
    hell_button = wait_for_image("./assets/img/hell.png")
    pyautogui.click(hell_button)


def wait_for_image(
    image_path, timeout=120, realtime=False, grayscale=True, confidence=0.9
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


if __name__ == "__main__":
    main()
