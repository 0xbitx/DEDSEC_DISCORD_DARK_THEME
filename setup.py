 
import os, time

username = os.getenv('USER') or os.getenv('LOGNAME')

path = f'/home/{username}/.config/BetterDiscord/themes/'

os.system('curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl')
os.system('chmod +x betterdiscordctl')
os.system('sudo mv betterdiscordctl /usr/local/bin')
os.system('betterdiscordctl install')
os.system('wget https://gist.githubusercontent.com/0xbitx/201fb6e02258271c452731a77dc8bafb/raw/a1ad565c6381437a2e2a5f08bb37655e29c455f5/dedsec.theme.css')
time.sleep(1)
if os.path.exists(path):
    os.system(f'mv dedsec.theme.css "{path}"')
else:
    try:
        os.makedirs(path)
        os.system(f'mv dedsec.theme.css "{path}"')
    except OSError as e:
        print(f"Failed to create directory: {e}")
