import discord
from discord.ext import commands, tasks
import datetime as dt
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pray_times_calculator import PrayerTimesCalculator

allowed_mentions = discord.AllowedMentions(everyone = True)
channel_id = CHANNEL_ID
bot = commands.Bot("$", intents=discord.Intents.default())
token = TOKEN
scheduler = AsyncIOScheduler()

def calculate_times():
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
    return times

async def send_message(salah):    
        message_channel = bot.get_channel(channel_id)
        await message_channel.send(f"<@&ID> It is {salah} time! Be sure to Pray {salah}!", allowed_mentions = allowed_mentions)

async def ayatul_kursi(salah):
    message_channel = bot.get_channel(channel_id)
    await message_channel.send(f"<@&ID> Don't forget to read ayatul kursi after {salah}!\n https://tanzil.net/#2:255", allowed_mentions = allowed_mentions)


@bot.event
async def on_ready():
    await salah.start()

@tasks.loop(hours=24)
async def salah():
    times = calculate_times()
    salahs = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
    for salah in salahs:
        time = dt.date.today().strftime("%m/%d/%y") + ' ' + times[salah]
        date = dt.datetime.strptime(time , "%m/%d/%y %H:%M")
        scheduler.add_job(send_message, 'date', run_date=date, args=[salah])
        scheduler.add_job(ayatul_kursi, 'date', run_date=date, args=[salah])
    scheduler.start()


if __name__ == "__main__":
    bot.run(token)
