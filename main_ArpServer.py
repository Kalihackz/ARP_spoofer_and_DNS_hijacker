from flask import Flask, render_template
import subprocess,os
from termcolor import cprint

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/jquery.js', methods=['GET'])
def jquery():
    return render_template("jquery.js")
    
@app.route('/http_on', methods=['GET'])
def http_on():
    subprocess.call(['gnome-terminal', '--',"sudo", "nodemon", "server/express_http.js"])
    return ("Activated")
    
@app.route('/http_off', methods=['GET'])
def http_off():
    return ("De-Activated")

@app.route('/https_on', methods=['GET'])
def https_on():
    subprocess.call(['gnome-terminal', '--',"sudo", "nodemon", "server/express_https.js"])
    return ("Activated")
    
@app.route('/https_off', methods=['GET'])
def https_off():
    return ("De-Activated")

@app.route('/arp_on', methods=['GET'])
def arp_on():
    __ = subprocess.check_output("sudo sysctl net.ipv4.ip_forward=0", shell=True)
    subprocess.call(['gnome-terminal', '--',"sudo", "python3", "ARP_Spoofer.py"])
    return ("Activated")
    
@app.route('/arp_off', methods=['GET'])
def arp_off():
    return ("De-Activated")

@app.route('/ipv4_on', methods=['GET'])
def ipv4_on():
    __ = subprocess.check_output("sudo sysctl -w net.ipv4.ip_forward=1", shell=True)
    return ("Activated")
    
@app.route('/ipv4_off', methods=['GET'])
def ipv4_off():
    __ = subprocess.check_output("sudo sysctl -w net.ipv4.ip_forward=0", shell=True)
    return ("De-Activated")

if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
else:
    cprint('''  _   _      _   _                   
 | \ | | ___| |_| |_ _ __ __ _ _ __  
 |  \| |/ _ \ __| __| '__/ _` | '_ \ 
 | |\  |  __/ |_| |_| | | (_| | |_) |
 |_| \_|\___|\__|\__|_|  \__,_| .__/ 
                              |_|    
''',"red")
    cprint("                         By Kalihackz","green")
    cprint("                         Version : Final\n","yellow")
app.run(debug=False)
