import subprocess

cmd = ["bash", "--version"]
sp = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
rc = sp.wait()
o,e = sp.communicate()

# The code is to print the bash version of the OS
if rc == 0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line)
else:
    print(f"Command was failed and error is: {e}")