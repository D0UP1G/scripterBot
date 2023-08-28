import subprocess
import getpass

for i in ['aiogram', 'requests','lxml','pyautogui','opencv-python']:
    process = subprocess.Popen(['pip','install',i])
    process.wait()
os.mkdir(F'C:\Users\{getpass.getuser()}\Documents\critp')
os.mkdir(F'C:\Users\{getpass.getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
