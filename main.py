import discord
from discord.ext import commands, tasks
import datetime as dt
from pray_times_calculator import PrayerTimesCalculator

allowed_mentions = discord.AllowedMentions(everyone = True)
channel_id = ID
bot = commands.Bot("$", intents=discord.Intents.default())
token = "TOKEN"

@bot.event
async def on_ready():
    await salah.start()

@tasks.loop(seconds=30)
async def salah():
    calc = PrayerTimesCalculator(
        latitude=27.9506,
        longitude=-82.4572,
        calculation_method='isna',
        date=str(dt.date.today()),
        school='shafi',
        midnightMode='jafari',
        latitudeAdjustmentMethod='one seventh',
        tune=False,
        imsak_tune=0,
        fajr_tune=0,
        sunrise_tune=0,
        dhuhr_tune=0,
        asr_tune=0,
        maghrib_tune=0,
        sunset_tune=0,
        isha_tune=0,
        midnight_tune=0,
        fajr_angle=15,
        maghrib_angle=None,
        isha_angle=15,
    )
    times = calc.fetch_prayer_times()
    time = dt.datetime.now().time().strftime("%H:%M")
    if time == times['Fajr']:
        message_channel = bot.get_channel(channel_id)
        await message_channel.send("<@&ID> It is Fajr time! Be sure to Pray Fajr!", allowed_mentions = allowed_mentions)
    elif time == times['Dhuhr']:
        message_channel = bot.get_channel(channel_id)
        await message_channel.send("<@&ID> It is Dhuhr time! Be sure to Pray Dhuhr!", allowed_mentions = allowed_mentions)
    elif time == times['Asr']:
        message_channel = bot.get_channel(channel_id)
        await message_channel.send("<@&ID> It is Asr time! Be sure to Pray Asr!", allowed_mentions = allowed_mentions)
    elif time == times['Maghrib']:
        message_channel = bot.get_channel(channel_id)
        await message_channel.send("<@&ID> It is Maghrib time! Be sure to Pray Maghrib!", allowed_mentions = allowed_mentions)
    elif time == times['Isha']:
        message_channel = bot.get_channel(channel_id)
        await message_channel.send("<@&ID> It is Ishaa time! Be sure to Pray Ishaa!", allowed_mentions = allowed_mentions)

if __name__ == "__main__":
    bot.run(token)
