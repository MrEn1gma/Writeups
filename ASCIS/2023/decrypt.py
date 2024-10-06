import subprocess

p = subprocess.run("challenge1.exe %s", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)