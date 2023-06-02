echo "Cloning Repository"
git clone https://github.com/TechGiron/Guardian-All-Shortner-BOT.git /Guardian-All-Shortner-BOT
cd /Guardian-All-Shortner-BOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
