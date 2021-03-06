import discord
import weather_getter

token = 'NjEyMjYyNTE3MTU4MzEzOTg0.XVfz5w.HciJQO1Y2JvzrGeuBvsZ-UhipQo'
client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready.")

@client.event
async def on_message(message):
    content = message.content

    if content == "날씨":
        code, current_weather = weather_getter.generateRequest()
        embed = discord.Embed(title="안양시의 현재 날씨", description=f"{current_weather['weather'][0]['description']}", color=0xF2F2F1)
        embed.set_thumbnail(url=f"http://openweathermap.org/img/wn/{current_weather['weather'][0]['icon']}@4x.png")
        embed.add_field(name="온도", value=f"{current_weather['main']['temp']}°C", inline=True)
        embed.add_field(name="습도", value=f"{current_weather['main']['humidity']}%", inline=True)
        embed.add_field(name="체감온도", value=f"{current_weather['main']['feels_like']}°C", inline=True)
        embed.add_field(name="바람", value=f"{current_weather['wind']['speed']}km/h@{current_weather['wind']['deg']}", inline=False)
        embed.set_footer(text="와인봇, 동기가 만든")
        await message.channel.send(embed=embed)

client.run(token)