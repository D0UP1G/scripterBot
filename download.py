import subprocess

for i in ['aiogram', 'requests','lxml','pyautogui','opencv-python']:
    process = subprocess.Popen(['pip','install',i])
    process.wait()
