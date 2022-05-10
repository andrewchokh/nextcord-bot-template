from dotenv import load_dotenv
from src.bot import Bot
import json
import os


def load_json(filename):
    with open(filename) as infile:
        return json.load(infile)


def main():
    load_dotenv()

    bot = Bot(
        cfg=load_json('.src/cfgs/bot.json')
    )
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()