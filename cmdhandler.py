import subprocess 
import os
# pkexec
def upgrade_cmd():
    subprocess.run(['pkexec','pacman','-Syu', '--noconfirm'])

def del_packets_cmd():
    os.system("pacman -Qdtq | pkexec pacman -Rns --noconfirm -")