echo "Cloning Repo...."
git clone https://github.com/PlayerX/Player-X-bot.git /Player-X-bot
cd /Player-X-bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
