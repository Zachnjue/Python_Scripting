import subprocess

cmd = ["java", "--version"]
sp = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
rc = sp.wait()
o,e = sp.communicate()

if rc == 0:
    for each_line in o.splitlines():
        print (each_line)
            