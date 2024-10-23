<p align="center">
  <h1>⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️</h1>
</p>

<p align="center">
<b>Symbiote</b> is a powerful social engineering tool designed to create phishing pages and capture images from a webcam. By requesting camera permissions from the victim's device, this script can covertly take photos. If you'd like to contribute to the project, we would love to have you on board! 💻🤝
</p>

---

## 🌐 Available Tunneling Options
Choose one of the following tunneling options to facilitate your usage:
1. **NGROK** [🔗 Requires Account](https://ngrok.com)
2. **Localhost.run** [🌐 Free & Easy](http://localhost.run)
3. **LOCALXPOSE** [🔗 Requires Account](https://localxpose.io)

---

## 🛠️ Installation (Kali Linux/Termux)

### Step 1: Install Prerequisites
Run the following commands to ensure all necessary packages are installed:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 wget php openssh-client jq -y
sudo ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y >/dev/null 2>&1
```

### Step 2: Clone the Repository and Run
Execute the following commands to clone the repository and start the tool:
```bash
git clone https://github.com/hasanfirnas/symbiote
cd symbiote
python3 symbiote.py
```

### Step 3: Access Captured Data
Once you have captured a cam file, you can view it using:
```bash
cd symbiote/CapturedData
ls
termux-open <file_name>
```

---

## 📋 Prerequisites
Ensure you have the following installed:
- **Python 3** 🐍
- **PHP** 🛠️
- **wget** 🌐

---

## 📸 Screenshot (Kali Linux)
![Symbiote Screenshot](https://i.imgur.com/PP51q6i.jpeg)

---

## 📽️ Video Tutorial (Step-by-step commands)
[![Watch the video](https://i.imgur.com/PP51q6i.jpeg)](https://youtu.be/j8rTc3CI7UA)

---

<p align="center">
  <b>Disclaimer:</b> This tool is intended for ethical hacking and educational purposes only. Misuse of this tool is strictly prohibited and the developer is not responsible for any illegal actions taken with it.
</p>
