#!/usr/bin/python3

from discordwebhook import Discord

def send_notif(target_name, target_platform, change):
    discord = Discord(url="https://discordapp.com/api/webhooks/1172444478540353647/ERGLO7YCDtGb_ZWV8VuD1qCZyB4hLgT7YN-mbtjSQ2IXSOoKmkrirlhcC6ZHRUZVZsqd")
    
    msg = f'***{target_name}*** (New on {target_platform}) added some new domains:\n ` {change} \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t` \n\n'
    
    discord.post(content=msg)