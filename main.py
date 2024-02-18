import os 
items = ["pytz" "setuptools" "aioconsole" "asyncio"]
for item in items:
  os.system(f"pip install {item}")
os.system(f"pip install fortnitepy")
import fortnitepy

bot = fortnitepy.Client(
  auth=fortnitepy.AuthorizationCodeAuth(
    code=input("Code: ")
  )
)

@bot.command()
async def cid(ctx,skin):
  await bot.party.me.set_outfit(cid)
  await ctx.send(skin)

bot.run()
