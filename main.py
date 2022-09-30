from dis import disco
import discord
from discord.ext import commands, tasks
import datetime as dt
from pray_times_calculator import PrayerTimesCalculator
bot = commands.Bot("$", intents=discord.Intents.default())
token = ""
channel_id = 965808322768941129
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



@bot.event
async def on_ready():
    await salah.start()

@tasks.loop(seconds=30)
async def salah():
    print('est')
    message_channel = bot.get_channel(channel_id)
    times = calc.fetch_prayer_times()
    time = dt.datetime.now().time().strftime("%H:%M")
    if time == times['Fajr']:
        await message_channel.send("It is Fajr time! Be sure to Pray Fajr!")
    elif time == times['Dhuhr']:
        await message_channel.send("It is Dhuhr time! Be sure to Pray Dhuhr!")
    elif time == times['Asr']:
        await message_channel.send("It is Asr time! Be sure to Pray Asr!")
    elif time == times['Maghrib']:
        await message_channel.send("It is Maghrib time! Be sure to Pray Maghrib!")
    elif time == times['Isha']:
        await message_channel.send("It is Ishaa time! Be sure to Pray Ishaa!")

if __name__ == "__main__":
    bot.run(token)

