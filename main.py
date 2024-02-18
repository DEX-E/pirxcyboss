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
