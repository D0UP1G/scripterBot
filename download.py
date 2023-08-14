import subprocess

for i in ['aiogram', 'requests','lxml',]:
    process = subprocess.Popen(['pip','install',i])
    process.wait()
