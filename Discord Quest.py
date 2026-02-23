import subprocess, sys, time
try: import pyautogui, pyperclip, win32gui, win32process; from bs4 import BeautifulSoup; import requests, psutil
except: subprocess.check_call([sys.executable,"-m","pip","install","pyautogui","pyperclip","pywin32","requests","beautifulsoup4","psutil"]); import pyautogui, pyperclip, win32gui, win32process; from bs4 import BeautifulSoup; import requests, psutil

r=requests.get("https://gist.githubusercontent.com/aamiaa/204cd9d42013ded9faf646fae7f89fbb/raw/e284335c95dec448a2ba751853d122b210bb195a/CompleteDiscordQuest.md"); s=r.text if r.status_code==200 else ""; a=s.find("```js"); texte=s[a+5:s.find("```",a+5)].strip() if a!=-1 else ""

def find_window_by_process(name):
    name=name.lower(); t=[]
    for p in psutil.process_iter(['pid','name']):
        if p.info['name'] and p.info['name'].lower()==name:
            pid=p.info['pid']
            def cb(hwnd,e):
                if win32gui.IsWindowVisible(hwnd) and win32process.GetWindowThreadProcessId(hwnd)[1]==pid: t.append(hwnd)
                return True
            win32gui.EnumWindows(cb,None)
    return t[0] if t else None

hwnd=find_window_by_process("Discord.exe"); exit() if not hwnd else win32gui.ShowWindow(hwnd,5); win32gui.SetForegroundWindow(hwnd); time.sleep(1)
pyautogui.hotkey("ctrl","shift","i"); time.sleep(2); pyperclip.copy(texte); pyautogui.hotkey("ctrl","v"); pyautogui.press("enter")