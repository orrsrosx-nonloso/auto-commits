#!/usr/bin/env bash
#
# Commit Bot by Steven Kneiser
#
# > https://github.com/theshteves/commit-bot
#
# Deploy locally by adding the following line to your crontab:
# 0 22 * * * /bin/bash /<full-path-to-your-folder>/code/commit-bot/bot.sh
#
# Edit your crontab in vim w/ the simple command:
# crontab -e
#
# Deploying just on your computer is better than a server if you want
# your commits to more realistically mirror your computer usage.
#
# ...c'mon, nobody commits EVERY day ;)
#

#提前执行pyhton文件
python getWeiboHotData.py
python indexcreate.py
info="Commit: $(date)"
os="$(uname -s)"

echo "auto-commit detects OS: $os"

case $os in

    Darwin)
        cd "`dirname $0`" || exit 1
        ;;

    Linux)
        cd "$(dirname "$(readlink -f "$0")")" || exit 1
        ;;

    CYGWIN*|MINGW32*|MSYS*|MINGW*)
        echo "OS unsupported (submit an issue on GitHub!)"
        ;;

    *)
        echo "OS unsupported (submit an issue on GitHub!)"
        ;;
esac

echo "$info" >> output.txt
echo "$info"
echo

# Ship it
git add output.txt
git add hot.json
git add index.html
git commit -m "#docs&style: weibo hot mes get$info"
git push origin main # or "master" on old setups

cd -
