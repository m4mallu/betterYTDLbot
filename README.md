# BetterYtDLBoT 😉

---
## Easy Installation:

**Deploy in Heroku** (Press the below button)

[Heroku having some problems with youtube-dl, so may not work properly. Try some other VPS if possible.]

<br />

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/m4mallu/betterYTDLbot)

## Legendary way:

Prerequisites are:

  - ffmpeg

Run
<br />

    apt-get install ffmpeg

## install dependencies
    pip3 install -r requirements.txt


## Setup Bot:
<br />

Create a config.py file with required variables

**An example `config.py` file could be:**

[Note: All the variables are mandatory]

```python3
class Development(Config):
  APP_ID = "55315485"
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = "624442654:nhs6sgvhh6776gfnhsbnTGFbb9277nNbb"
  AUTH_USERS = [245588455,246456588,3452256266]
  PRE_FILE_TXT = "@MovieKeralam."
```
**Finally Run:**

    python3 -m bot

---
    
##To run the bot in linux backend

**Create a `script.sh` file with the above command**

**An example `script.sh` file could be:**

    #!/bin/sh
    cd <path to the bot directory>
    python3 -m bot

**Make the script executable**

    cd <directory to the script file>
    chmod 755 <name of the script file.sh>

**Create a crontab entry to run the script in backend after every system reboot:**

    sudo su
    sudo crontab -e
  - Open the file in nano / vim editor . (First time it will ask for the selection)
  - Add the below line to the bottom of the file.
  - Reboot the system.

**An example `crontab` entry could be:**

    @reboot <path to the script file.sh>

---

## Thanks ❤️
* [Spechide](https://telegram.dog/SpEcHIDe) for his [AnyDlBot](https://github.com/SpEcHiDe/AnyDLBot)
* [Aryan Vikash](https://t.me/aryanvikash) for his [YouTube DL Bot](https://github.com/aryanvikash/Youtube-Downloader-Bot)

## Created By
* [Mallu Boy](https://github.com/m4mallu) in Tg as [RENJITH](https://t.me/space4renjith)
