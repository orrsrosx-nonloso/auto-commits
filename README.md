# auto-commits
GitHub Commit Bot
Generate Organic™ GitHub activity
My most insidious idea yet


The Contribution Dream


Once a day (if my laptop is open),
commit-bot adds today's line:

Commit: Wed Sep 25 22:00:00 EDT 2019
This is a Bash script
designed to be run locally
(i.e. on your machine)




But @theshteves,
I want this to run every day

Oh hush

Nobody commits every day
Is that what you want?
🚫 Sorry, not today

We're looking for a more realistic distribution of activity throughout the year




Getting Started
If you're on Windows™,
setup the Windows Subsystem for Linux

If you haven't already,
install git


Open your command-line
& navigate to whatever folder you prefer

Fork this project on GitHub

Download your new copy of this project

git@github.com:orrsrosx-nonloso/auto-commits.git
Don't forget to include your username

Test run the script
in case you need to fix permissions issues
/bin/bash ./commit-bot/bot.sh
Open your crontab to set a trigger
crontab -e
NOTE:
If this makes your screen almost blank
with no toolbar of keys to navigate,
you've probably entered the text editor Vim

Remember, press "i" to start [i]nserting text

When you're finished,
press "Esc" repeatedly until nothing happens

Then type ":wq" to save & quit
or ":q!" to quit without saving

Add this line to schedule every 10pm or whenever
0 22 * * * /bin/bash /<full-path-to-your-folder>/commit-bot/bot.sh
Do not forget to include the correct folder path

NOTE:
Make sure you save your changes
on your way out!
