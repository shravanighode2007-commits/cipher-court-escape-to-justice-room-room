import subprocess

try:
    p = subprocess.Popen(['powershell', '-Command', 'Get-Process Unity | Select-Object Id, ProcessName, MainWindowTitle'], stdout=subprocess.PIPE, text=True)
    out, _ = p.communicate()
    print(out)
except Exception as e:
    print(e)
