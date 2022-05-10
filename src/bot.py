from nextcord.ext import commands
import nextcord
from src.utils import logger
import os


class Bot(commands.Bot):
    def __init__(self, cfg, db=None):
        super().__init__(
            command_prefix=cfg.prefixes,
            intents=nextcord.Intents.default()
        )
        self.cfg = cfg
        self.db = db

        self.load_cogs('./src/cogs')   

    def load_cogs(self, path):
        for file in os.listdir(path):
            if not file.startswith('_') and file.endswith('.py'):
                super().load_extension(f'src.cogs.{file[:-3]}')
                logger.info(f'Loaded cog "{ file[:-3]}"')  
                              
    def run(self, token):
        super().run(token)