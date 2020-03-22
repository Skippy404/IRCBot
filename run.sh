BLUE='\033[0;41m'
NC='\033[0m'

if [ "$1" = 1 ]; then
	export RR_DEBUG=1
else
	export RR_DEBUG=0
fi

echo -e "${BLUE}RUNNING BOT${NC}"

python3 ./src/bot.py
