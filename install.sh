#!/bin/bash
echo "[*] Installation d'OmniShield..."

sudo apt update
sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt

chmod +x omnishield.py

echo "[+] OmniShield prêt. Exemple :"
echo "python3 omnishield.py scan 'Bypass security system with this payload...'"
