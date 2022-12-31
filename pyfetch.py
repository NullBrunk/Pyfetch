
Skip to content
Pull requests
Issues
Codespaces
Marketplace
Explore
@NullBrunk
NullBrunk /
Pyfetch
Public

Code
Issues 1
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

Pyfetch/pyfetch.py /
@NullBrunk
NullBrunk Update and rename exploit.sh to pyfetch.py
Latest commit c094a95 Dec 31, 2022
History
1 contributor
76 lines (52 sloc) 1.76 KB
from termcolor import colored
from platform import release
from os import popen, environ
from sys import platform


def getde():

	if platform in ["win32", "cygwin"]:
		return "windows"
	
	elif platform == "darwin":
		return "mac"

	else: 
		
		common_de = [
			"Gnome",
			"Cinnamon", 
			"Mate", 
			"Xfce4", 
			"Fluxbox", 
	 		"Openbox", 
		]
		desktop_session = environ.get("DESKTOP_SESSION").lower()

		if desktop_session in common_de:
			return desktop_session.capitalize()

		elif "xfce" in desktop_session or desktop_session.startswith("xubuntu"):
			return "Xfce4"

		elif "kde" in desktop_session or desktop_session.startswith('ubuntustudio'):
			return 'KDE'
		
		elif desktop_session.startswith('ubuntu'):
			return 'Gnome'     
		
		elif desktop_session.startswith("lubuntu"):
			return "LXDE" 
		
		elif desktop_session.startswith("kubuntu"): 
			return "KDE" 

	return desktop_session


def getkernel() -> str:
	return release()

def getuptime() -> str:
	return popen("uptime -p").read().strip().split("up")[1].replace("minute", "min")[1:]

def getram() -> str:
	mem = popen("free -m").readlines()[1].split()
	return f"{mem[2]}MiB / {mem[1]}MiB"

def getshell() -> str:
	return environ["SHELL"]



def main():

	banner = f"""
     {colored(" ▄       ▄ ", "blue")}      {colored("", "green")}  • {getkernel()}   
     {colored("▄ ▀▄   ▄▀ ▄", "blue")}      {colored("", "yellow")}  • {getuptime()}
     {colored("█▄█▀███▀█▄█", "blue")}      {colored("", "blue")}  • {getram()}
     {colored("▀█████████▀", "blue")}      {colored("", "magenta")}  • {getde()}
     {colored(" ▄▀     ▀▄ ", "blue")}      {colored("", "cyan")}  • {getshell()}
	"""

	print(banner)

if __name__ == "__main__":
	main()
Footer
© 2022 GitHub, Inc.
Footer navigation

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

