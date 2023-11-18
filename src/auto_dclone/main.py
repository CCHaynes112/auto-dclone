import time
import dotenv
import os

from poller import Poller
from game_creation_bot import GameCreationBot
from region import Region

dotenv.load_dotenv()

def handle_intro():
    print("Welcome to auto dclone bot!")
    print("This bot will:")
    print("1. Poll the api for dclone spawn")
    print("3. Start diablo 2 and create a game\n")
    print("Data courtesy of diablo2.io")
    print("https://diablo2.io/dclonetracker.php\n")
    
    region = input("Enter region (1 = America, 2 = Europe, 3 = Asia) or leave blank for all: ")
    ladder = input("Enter ladder (1 = ladder, 2 = non-ladder) or leave blank for all: ")
    hardcore = input("Enter hardcore (1 = hardcore, 2 = softcore) or leave blank for all: ")

    print("")

    input("Press any key to start polling")
    return region, ladder, hardcore
    
# Example payload:
# {
#     "region": "americas",
#     "hardcore": "softcore",
#     "ladder": "ladder",
#     "progress": 1,
#     "time": "2023-02-05 23:43:22"
# },
def main():
    region, ladder, hardcore = handle_intro()

    game_creation_bot = GameCreationBot(os.getenv("D2_LAUNCHER_PATH"))
    poller = Poller(region, ladder, hardcore)

    while True:
        data = poller.poll_api()
        for realm in data:
            region = (
                Region.AMERICA
                if realm["region"] == "1"
                else Region.EUROPE
                if realm["region"] == "2"
                else Region.ASIA
            )
            ladder = "ladder" if realm["ladder"] == "1" else "non-ladder"
            hardcore = "hardcore" if realm["hc"] == "1" else "softcore"
            progress = realm["progress"]
            progress = "5"
            print(f"{region.name} {ladder} {hardcore} {progress}")
            if progress != "5" and progress != "6":
                continue

            print("Dclone is spawning! Go get him!")
            print("Running diablo 2 automation...")
            game_creation_bot.run_diablo_2_automation(region)
            print("Bot initialized and waiting")
            print("Press any key to continue polling")
            input()
            break
        print("Waiting 2 minutes before polling again...\n")
        time.sleep(120)

if __name__ == "__main__":
    main()