import os
import subprocess
import shutil

CRD_SSH_Code = input("Google CRD SSH Code :")
username = "user" #@param {type:"string"}
password = "user" #@param {type:"string"}
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 1234 #@param {type: "integer"}
Autostart = True #@param {type: "boolean"}

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.changewall()
        self.installGoogleChrome()
        self.installTelegram()
        self.installQbit()
        self.finish(user)

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Chrome Remoted Desktop Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("sudo service lightdm stop")
        os.system("sudo apt-get install dbus-x11 -y")
        os.system("service dbus start")
        print("Installed XFCE4 Desktop Environment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    @staticmethod
    def installTelegram():
        subprocess.run(["apt", "install", "--assume-yes", "telegram-desktop"])
        print("Telegram Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def changewall():
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/1280x1024.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/1280x1024.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/1280x800.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/1280x800.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/1600x1200.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/1600x1200.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/1920x1080.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/1920x1080.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/1920x1200.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/1920x1200.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/2560x1440.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/2560x1440.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/2560x1600.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/2560x1600.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/3200x1800.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/3200x1800.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/3200x2000.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/3200x2000.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/3840x2160.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/3840x2160.svg")
        os.system(f"sudo curl -s -L -o /etc/alternatives/desktop-theme/wallpaper/contents/images/5120x2880.svg https://gitlab.com/chamod12/gcrd_deb_codesandbox.io_rdp/-/raw/main/walls/5120x2880.svg")
        print("Wallpaper Changed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
   
    @staticmethod
    def installQbit():
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "qbittorrent"])
        print("Qbittorrent Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def finish(user):
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "www.youtube.com/@The_Disala"
            colab_autostart = """[Desktop Entry]
            print("Finalizing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")
            
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        
        print(" ..........................................................")
        print(" .....Brought By The Disala................................")
        print(" ..........................................................")
        print(" ......#####...######...####....####...##.......####.......")
        print(" ......##..##....##....##......##..##..##......##..##......")
        print(" ......##..##....##.....####...######..##......######......")
        print(" ......##..##....##........##..##..##..##......##..##......")
        print(" ......#####...######...####...##..##..######..##..##......")
        print(" ..........................................................")
        print(" ......... Telegram Channel - https://t.me/TheDisala4U ....")
        print(" ..........................................................")
        print(" ..Youtube Channel - https://www.youtube.com/@The_Disala ..")
        print(" ..........................................................")
        print("Log in PIN : 123456") 
        print("User Name : user") 
        print("User Pass : root") 
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
