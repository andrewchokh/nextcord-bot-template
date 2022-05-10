# <p align="center">**COGS folder**</p>
In this folder will be stored extentions for bot. <br>
Here's an example of a cog:

```python
from nextcord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Some incrediable code


def setup(bot):
    bot.add_cog(Example(bot))
```
