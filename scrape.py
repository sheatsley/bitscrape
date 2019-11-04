"""
Code for scraping gifs from 8bitdash
Author: Ryan Sheatsley
Mon Nov 4 2019
"""


def scrape(root="http://8bitdash.com/", interval=5, out="gifs/"):
    """
    This is the main scraping function. To keep code as minimial as
    possible, the pathnames cannot be dynamically determined (as it
    would require a library that supports resolving javascript). 
    Thus, simply copy and paste the gif paths from the source 
    through your browser (lines 8600-8604 from main.c97e3faf.js). 
    No other modifications are necessary.
    url - webpage to scrape from
    interval - wait time (in seconds) inbetween requests
    out - directory to write to
    """

    # global imports
    import time
    import urllib.request

    # this only requires you to copy and paste
    valenberg = "valenberg"
    landscapes = "landscapes"
    kirokaze = "kirokaze"

    # last copied Mon Nov 4 2019
    h = {
        landscapes: [
            "bridge.gif",
            "bridge_raining.gif",
            "coast.gif",
            "falls.gif",
            "forrest.gif",
            "lake.gif",
            "nature.gif",
            "northlights.gif",
            "sea.gif",
        ],
        valenberg: [
            "streets.gif",
            "shop.gif",
            "highlands.gif",
            "virtuaverse.gif",
            "sushi.gif",
            "girlinrain.gif",
            "exodus.gif",
            "drift.gif",
            "daftpunk.gif",
            "blade.gif",
            "highfloor.gif",
            "lowlands.gif",
            "moon.png",
        ],
        kirokaze: [
            "spaceport.gif",
            "bad_landing.gif",
            "bluebalcony.gif",
            "coffeeinrain.gif",
            "dark_pillar.gif",
            "familydinner.gif",
            "cemetry.gif",
            "sandcastle.gif",
            "horse.gif",
            "nightlytraining.gif",
            "attack.gif",
            "zombies.gif",
            "citymirror.gif",
            "droidcrime.gif",
            "elderorc.gif",
            "factory5.gif",
            "iplayoldgames.gif",
            "metro_final.gif",
            "pilot.gif",
            "player2.gif",
            "robot_alley.gif",
            "shootingstars.gif",
            "thieves.gif",
            "train_city.gif",
            "troll_cave.gif",
            "youngatnight.gif",
        ],
    }

    # main scraping portion
    found, scraped, attempts = 0, 0, 0
    for author in h:
        for gif in h[author]:

            # be nice, only scrape what's new
            try:
                open(out + gif, "rb")
                found += 1
                print("[  ]", gif, "exists! Skipping...")
            except IOError as e:

                # apparently not everything is a gif
                if "gif" in gif:
                    try:
                        print("[>>>] Scraping", gif, "...")
                        with urllib.request.urlopen(
                            root + author + "/" + gif
                        ) as req, open(out + gif, "wb") as fp:
                            size = fp.write(req.read())
                        scraped += 1
                        print(
                            "[<<<]",
                            gif,
                            "successful! Wrote ",
                            str(size / 1024 ** 2)[:4] + "MB",
                        )
                    except:
                        print("[//<]", gif, "unsuccessful.")
                    attempts += 1
                    time.sleep(5)

    # everyone likes closure
    print(
        "Script complete.",
        found + attempts,
        "total gifs:",
        found,
        "already found, ",
        attempts,
        "attempted,",
        scraped,
        "successful.",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(scrape())
