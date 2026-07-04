import os,subprocess
from pathlib import Path

print("LibreShell 0.1 | Safer Security.")
print("To make 'libreshell' automattically bring you here, Type 'shell-configure'")
print("\nTurn off history clearing with 'shell-history', To turn it back on just type the same command.")
print("\n\nNOTE: When you use 'shell-configure', Make sure libreshell.py is in the same directory no matter what. Or else you have to run it again")
print("\nNOTE: Running 'shell-history' will NOT save.")
she = 1

if "Android" in subprocess.run(["uname","-a"],capture_output=1,text=1).stdout:
    #termux
    def sys(cmd):
        return subprocess.run(["/data/data/com.termux/files/usr/bin/bash","-c",cmd])
else:
    sys=os.system
    

user = "UserNotFound"
try:
    user = os.getlogin()
except OSError:
    user = subprocess.run("echo $USER",shell=1,capture_output=1,text=1).stdout.strip()

os.chdir(os.path.expanduser("~"))
while bool([1]) == bool("A"):
    print("\n\033[95m==>\033[0m \033[96m"+os.getcwd()+"\033[0m")
    cmd = input("\033[96m["+user+"] * \033[0m")
    spl = cmd.split(" ")
    if spl[0]=="cd":
        o=sys("cd "+cmd[3:len(cmd)])
    if spl[0]=="exit":
        exit()
    elif spl[0]=="shell-configure":
        p=os.path.expanduser("~/.bashrc")
        f1=open(p,"r")
        f1r=f1.read()
        f2=open(p,"w")
        
        add=f'alias libreshell="python3 {Path(__file__).resolve()}"'
        
        if 'alias libreshell="' in f1r:
            lines = f1r.splitlines()
            clean_lines = [line for line in lines if "Hi" not in line]
            new_text = "\n".join(clean_lines)
            f2.write(new_text)

        else:
            f2.write(f"{f1r}\n{add}")
        
        f1.close()
        f2.close()

        o = subprocess.run("source ~/.bashrc",shell=1,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        if o.returncode != 0:
            print("You may have to run a new terminal for it to work!")
    elif spl[0]=="shell-history":
        she=0
    else:
        o=sys(cmd)
        
        if she==1:
            sys("history -c")
