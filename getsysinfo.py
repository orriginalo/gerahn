import platform,socket,psutil,logging,distro
import gpustat

plat = platform.system()
gpu_stats = gpustat.GPUStatCollection.new_query()
gpuname:str
for gpu in gpu_stats.gpus:
    gpuname = gpu.name

def getSystemInfo():
    try:
        if plat == "Linux":

            info = {
                'OS' : distro.name(),
                'Platform' : platform.system(),
                'Platform release' : platform.release(),
                'Distro release' : distro.version(),
                'GPU' : gpuname,
                'Hostname' : socket.gethostname(),
                'IP address' : socket.gethostbyname(socket.gethostname()),
                'Architecture' : platform.machine(),
                'Ram' : str(round(psutil.virtual_memory().total / (1024.0 **3)) + 1)+" GB"
            }
        else:
            info = {
                'Platform' : platform.system(),
                'Platform release' : platform.release(),
                'Platform version' : platform.version(),
                'Architecture' : platform.machine(),
                'Hostname' : socket.gethostname(),
                'IP address' : socket.gethostbyname(socket.gethostname()),
                'Ram' : str( round(psutil.virtual_memory().total + 1 / (1024.0 **3) ) + 1) + " GB"
            }
        return info
    except Exception as e:
        logging.exception(e)

dic = getSystemInfo()
for key, value in dic.items():
    print(f"{key} >>> {value}")
    