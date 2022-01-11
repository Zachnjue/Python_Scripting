# This is used to execute Operating System commands
import subprocess

# For shell to be True, cmd is listed as a string while False is when the command is in List format
# For example 
# cmd = "ls -lrt" ==> shell = True
# cmd = "ls -lrt".split() or ['ls', '-lrt'] shell = False
cmd = 'ls -lrt'
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True ) # use of universal_newlines=True. Helps list the output
rt = sp.wait()
out, err = sp.communicate()

print(f'The return code is: {rt}')
print(f'The output is: \n{out.splitlines()}') # use of .splitlines() leads the output to be a list
print(f'The error is: \n{err.splitlines()}')
