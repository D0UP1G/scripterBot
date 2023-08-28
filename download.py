import subprocess
import getpass


user = getpass.getuser()
for i in ['aiogram', 'requests','lxml','pyautogui','opencv-python']:
    process = subprocess.Popen(['pip','install',i])
    process.wait()
os.mkdir(r'C:\Users\'+ user +r'\Documents\critp')
os.mkdir(r'C:\Users\'+ user +r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
