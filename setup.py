 
import os, time

username = os.getenv('USER') or os.getenv('LOGNAME')

path = f'/home/{username}/.config/BetterDiscord/themes/'

os.system('curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl')
os.system('chmod +x betterdiscordctl')
os.system('sudo mv betterdiscordctl /usr/local/bin')
os.system('betterdiscordctl install')
time.sleep(1)
if os.path.exists(path):
    os.system(f'mv dedsec.theme.css "{path}"')
else:
    try:
        os.makedirs(path)
        os.system(f'mv dedsec.theme.css "{path}"')
    except OSError as e:
        print(f"Failed to create directory: {e}")
