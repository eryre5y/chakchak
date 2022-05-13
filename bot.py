import hikari
import lightbulb
import random
import dstk

# konnichiwa

bot = lightbulb.BotApp(token=dstk.token, help_class=None)

HELP_MESSAGE = """
Команды:
`add` - прибавление числа (тест библиотеки)
`casino` - ебаное казино попробуй что-то выиграть
`chance` - шанс чего-то
`connect` - присоединение к войсу
`disconnect` - обратное к connect
`friends` - они реальны?
`fuck` - яой ирл
`japan` - фотка японии
`japangif` - аним фотка японии
`mention` - упоминание юзера
`ping` - понг
`rand` - рандом от какого-то числа до какого-то числа
`roll` - бросить кость
`terms` - условия пользования
`text` - текст от лица бота
"""

@bot.command
@lightbulb.command("help", "описание команд")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:
    await ctx.respond(HELP_MESSAGE)

"""
тут типа мем, но он не работает

@bot.command
@lightbulb.command("meme", "мем прямиком из пиндостана")
@lightbulb.implements(lightbulb.SlashCommand)
async def meme_subcommand(ctx: lightbulb.Context) -> None:
    async with ctx.bot.d.aio_session.get(
        "https://meme-api.herokuapp.com/gimme"
    ) as response:
        res = await response.json()
        if response.ok and res["nsfw"] != True:
            link = res["postLink"]
            title = res["title"]
            img_url = res["url"]
            embed = hikari.Embed(colour=0x3B9DFF)
            embed.set_author(name=title, url=link)
            embed.set_image(img_url)
            await ctx.respond(embed)
        else:
            await ctx.respond(
                "Could not fetch a meme :c", flags=hikari.MessageFlag.EPHEMERAL
            )
"""

@bot.command
@lightbulb.command('ping', 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('pong')

@bot.command
@lightbulb.command('japan', 'фотка японии')
@lightbulb.implements(lightbulb.SlashCommand)   
async def imgsnd(ctx):
    f = hikari.File('japan.jpg')
    await ctx.respond(f)

@bot.command
@lightbulb.command('japangif', 'фотка японии gif')
@lightbulb.implements(lightbulb.SlashCommand)   
async def imgsnd(ctx):
    f = hikari.File('japan.gif')
    await ctx.respond(f)

@bot.command
@lightbulb.command('friends', 'are they real?')
@lightbulb.implements(lightbulb.SlashCommand)   
async def imgsnd(ctx):
    f = hikari.File('friends.gif')
    await ctx.respond(f)

@bot.command
@lightbulb.command('casino', 'крути крути мы же миллионеры')
@lightbulb.implements(lightbulb.SlashCommand)
async def casino(context):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    if num1 == num2 == num3:
        win=":diamond_shape_with_a_dot_inside: Win :sparkler::sparkler::sparkler:"
    else:
        win=":diamond_shape_with_a_dot_inside: Loss"
    await context.respond(':gem: ' + str(num1) + ' | ' + str(num2) + ' | ' + str(num3) + ' :gem:\n' + str(win))

@bot.command
@lightbulb.command('roll', 'dice')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(context):
    await context.respond(':game_die: ' + str(random.randint(1, 6)) + ' :game_die:')

@bot.command
@lightbulb.option('text', 'текст', type=str)
@lightbulb.command('text', 'текст')
@lightbulb.implements(lightbulb.SlashCommand)
async def text(context):
    await context.respond(context.options.text)

@bot.command
@lightbulb.option('guildid', 'guild id')
@lightbulb.option('voiceid', 'voice id')
@lightbulb.command('connect', 'текст')
@lightbulb.implements(lightbulb.SlashCommand)
async def join(context):
    await bot.update_voice_state(context.options.guildid, context.options.voiceid)
    pass

@bot.command
@lightbulb.option('guildid', 'guild id')
@lightbulb.command('disconnect', 'текст')
@lightbulb.implements(lightbulb.SlashCommand)
async def disconnect(context):
    await bot.update_voice_state(context.options.guildid, None)
    pass

@bot.command
@lightbulb.option('user2', 'юзер2', hikari.User)
@lightbulb.option('user1', 'юзер1', hikari.User)
@lightbulb.command('fuck', 'трахнуть')
@lightbulb.implements(lightbulb.SlashCommand)
async def fuck(context):
    await context.respond(f"{context.options.user1.mention} смачно трахнул {context.options.user2.mention} :sweat_drops:")

@bot.command
@lightbulb.option('text', 'текст', str)
@lightbulb.option('user', 'юзер', hikari.User)
@lightbulb.command('mention', 'упомянуть юзера')
@lightbulb.implements(lightbulb.SlashCommand)
async def mention(context):
    await context.respond(f"мне кажется, что {context.options.user.mention} {context.options.text}")

@bot.command
@lightbulb.command('terms', 'условия пользования (terms of conditions)')
@lightbulb.implements(lightbulb.SlashCommand)
async def chance(context):
    await context.respond("ВНИМАНИЕ! Пользуясь этим ботом вы даете право, что у вас нет прав, матери, денег, телок, тачек, админок и вообще идите нахуй\n\n warning! using this bot you agree that ur a hopeless soul and ur life is already fucked so fuck you cunt")

@bot.command
@lightbulb.option('text', 'текст', type=str)
@lightbulb.command('chance', 'шанс чего-то')
@lightbulb.implements(lightbulb.SlashCommand)
async def chance(context):
    await context.respond(str(random.randint(1,100)) + "% шанс " + context.options.text)

@bot.command
@lightbulb.option('num2', 'цифра до', type=int)
@lightbulb.option('num1', 'цифра от', type=int)
@lightbulb.command('rand', 'рандом от чего-то до чего-то')
@lightbulb.implements(lightbulb.SlashCommand)
async def rand(ctx):
    await ctx.respond(random.randint(ctx.options.num1, ctx.options.num2))


"""
@bot.command
@lightbulb.command('group','group command')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(context):
    pass

@my_group.child
@lightbulb.command('subcommand', 'subcommand command')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(context):
    await context.respond('im a subcommand')
"""

@bot.command
@lightbulb.option('num1', 'first number', type=int)
@lightbulb.option('num2', 'the second number', type=int)
@lightbulb.command('add', 'add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

# ---------------------------

"""
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)
"""

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('bot started chak chak')

bot.run()
