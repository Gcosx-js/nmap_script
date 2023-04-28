import subprocess
try:
    
    target_ip = "192.168.1.104"
    nmap_command = ["nmap", "-sS", "-O", "-T4", target_ip]
    nmap_data = subprocess.check_output(nmap_command)
    print(nmap_data.decode("utf-8"))
except:
    print("IP scan failed!")


