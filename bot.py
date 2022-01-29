import webbrowser
import time
import pandas as pd
from datetime import datetime
import os
import sys

cwd = os.getcwd()


def makeCall(now):
    url = "https://cvrcoe.zoom.us/j/7968129860?pwd=S0VkZzRPdnNtMlRpQzZjcW10M2JIZz09";
    sign_in(url)
    print('signed in ' + now)


def sign_in(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


def find(now):
    i = 0
    j = 4
    ans = 0
    while i <= j:
        k = (i + j) // 2
        if (now < df0[k]):
            j = k - 1
        elif (now > df0[k]):
            ans = k
            i = k + 1
        else:
            ans = k
            break
    return ans


df = pd.read_csv(cwd + '/ctimings.csv')
df0 = df['timingss']
df1 = df['timingse']
while True:
    # checking if the current time exists in our csv file

    now = datetime.now().strftime("%H:%M")
    if (now >= '15:00'):
        sys.exit()
    j = find(now);
    if now < df1[j]:
        makeCall(now)
        time.sleep(4200)
    print('checked at' + now)
    time.sleep(58)
