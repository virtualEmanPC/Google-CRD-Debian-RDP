import os
import subprocess
import shutil

CRD_SSH_Code = "" #@param {type:"string"}
Username = "user" #@param {type:"string"}
Password = "root" #@param {type:"string"}
os.system(f"useradd -m {Username}")
os.system(f"adduser {Username} sudo")
os.system(f"echo '{Username}:{Password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 123456 #@param {type: "integer"}
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
        os.system("systemctl disable lightdm.service")
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
        os.system(f"curl -s -L -k -o xfce-verticals.png https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6S-m4OLmvtcZS8ZTVV6URDle3ElT3wy4mi2Zp1CPZ4B5k8JBHsxfQHoc6X9H0TNI0Mx-vS-Nvedg3Eu9lDkz7vZ0X3vo0xO1OjHLzmVkKMviP52PjB1fkveE51FmfgP-QQv0JGXM-ZnFJMTGU-gfFCQbbQ9DVchPVJ_xUMR5Dx-5hffAxAoCioOST9_0/s892/Wallpaper.png")
        current_directory = os.getcwd()
        custom_wallpaper_path = os.path.join(current_directory, "xfce-verticals.png")
        destination_path = '/usr/share/backgrounds/xfce/'
        shutil.copy(custom_wallpaper_path, destination_path)
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
            link = "https://github.com/virtualEmanPC/Google-CRD-Debian-RDP"
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

        print(".............................................................................................................................")
        print(".....Created By The Disala...................................................................................................")
        print(".....Modified By Virtual Eman PC.............................................................................................")
        print(".............................................................................................................................")
        print(".##.......##..######..######..######..##....##...####...##........######..####...####...####...####....##....######..######..")
        print("..##.....##.....##....##..##....##....##....##..##..##..##........##......##.##.##.##..##..##..##.##...##....##..##..##......")
        print("...##...##......##....######....##....##....##..######..##........####....##..###..##..######..##..##..##....######..##......")
        print("....##.##.......##....##.##.....##....##....##..##..##..##........##......##.......##..##..##..##...##.##....##......##......")
        print(".....###......######..##..##....##....########..##..##..######....######..##.......##..##..##..##....####....##......######..")
        print(".............................................................................................................................")
        print(" ")
        print("User Info :")
        print(" ")
        print("Log in PIN : " + str(Pin)) 
        print("User Name  : " + Username) 
        print("User Pass  : " + Password) 
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("Please Enter Authcode From The Given Link")
    elif len(str(Pin)) < 6:
        print("Enter A Pin More Or Equal To 6 Digits")
    else:
        CRDSetup(Username)
except NameError as e:
    print("'Username' Variable Not Found, Create A User First")
