import subprocess

try:
    p = subprocess.Popen(['powershell', '-Command', 'Get-CimInstance Win32_Process -Filter "Name = \'Unity.exe\'" | Select-Object ProcessId, CommandLine'], stdout=subprocess.PIPE, text=True)
    out, _ = p.communicate()
    print(out)
except Exception as e:
    print(e)
