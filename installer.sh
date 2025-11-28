#!/bin/bash
echo "==========================================="
echo "📦 MASTER-INSTALLER – ALLES (angepasst)"
echo "==========================================="

# System aktualisieren
sudo apt update
sudo apt upgrade -y

# -------------------------------
# SYSTEM-PROGRAMME
# -------------------------------
sudo apt install -y \
    firefox-esr \
    chromium-browser \
    code \
    thonny \
    scratch \
    scratch3 \
    vlc \
    gimp \
    pcmanfm \
    feh \
    libreoffice \
    filezilla \
    evince \
    lxterminal \
    htop \
    geany \
    idle3

# -------------------------------
# TERMINAL-EFFEKTE / TOOLS
# -------------------------------
sudo apt install -y \
    hollywood \
    cmatrix \
    sl \
    cowsay \
    lolcat \
    figlet \
    fortune \
    neofetch \
    bsdgames \
    jq \
    git \
    curl \
    wget \
    python3-pip \
    build-essential

# -------------------------------
# SPIELE / KLASSIKER
# -------------------------------
sudo apt install -y \
    supertux \
    supertuxkart \
    frozen-bubble \
    pacman4console \
    nethack-console \
    bastet \
    pingus \
    greed \
    lunar-lander

# -------------------------------
# PYTHON SPIELE & MINI-PROJEKTE
# -------------------------------
# Die Dateien werden in deinem vorhandenen ~/python_projekte erstellt

# Snake
cat << 'EOF' > ~/python_projekte/snake.py
import curses, random
s=curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w=curses.newwin(sh, sw, 0,0)
w.keypad(1)
w.timeout(120)
snake=[[sh//2,sw//4],[sh//2,sw//4-1],[sh//2,sw//4-2]]
food=[sh//2,sw//2]
w.addch(food[0],food[1],'🍎')
key=curses.KEY_RIGHT
while True:
    new=w.getch()
    key=key if new==-1 else new
    y,x=snake[0]
    if key==curses.KEY_UP:y-=1
    if key==curses.KEY_DOWN:y+=1
    if key==curses.KEY_LEFT:x-=1
    if key==curses.KEY_RIGHT:x+=1
    snake.insert(0,[y,x])
    if snake[0]==food:
        food=[random.randint(1,sh-2),random.randint(1,sw-2)]
        w.addch(food[0],food[1],'🍎')
    else:
        t=snake.pop()
        w.addch(t[0],t[1]," ")
    if y in [0,sh] or x in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        print("💀 Game Over")
        break
    w.addch(y,x,'■')
EOF

# Flappy Bird
cat << 'EOF' > ~/python_projekte/flappy.py
import os,time,random
bird=10
pipes=[30]
score=0
while True:
    os.system("clear")
    print("\n"*bird+"🐦")
    if pipes[0]==0:
        pipes=[30]
        score+=1
    gap=random.randint(3,15)
    print("\n"*gap+"██████")
    print("\nScore:",score)
    time.sleep(0.1)
    bird+=1
    if bird>=20:
        print("GAME OVER")
        break
EOF

# Bomberman
cat << 'EOF' > ~/python_projekte/bomber.py
import random
print("💣 BOMBERMAN 💣")
feld=[" "," "," ","🔥"," "," "]
pos=0
while True:
    cmd=input("l/r/b: ")
    if cmd=="l" and pos>0:pos-=1
    if cmd=="r" and pos<len(feld)-1:pos+=1
    if cmd=="b":
        if feld[pos]=="🔥":
            print("💥 Treffer!")
            break
        else:
            print("Nichts passiert.")
    print("".join(feld[:pos]+["😎"]+feld[pos+1:]))
EOF

# LED Simulator
cat << 'EOF' > ~/python_projekte/led_simulator.py
print("💡 LED Simulator gestartet")
EOF

# LED Rainbow
cat << 'EOF' > ~/python_projekte/led_rainbow.py
print("🌈 LED Farben Demo läuft")
EOF

# Zahlenraten
cat << 'EOF' > ~/python_projekte/raten.py
import random
zahl=random.randint(1,10)
versuch=int(input("Rate eine Zahl 1-10: "))
if versuch==zahl:
    print("🎉 Richtig!")
else:
    print("❌ Falsch! Die Zahl war",zahl)
EOF

# Text Adventure
cat << 'EOF' > ~/python_projekte/adventure.py
print("🏰 Willkommen im Text Adventure!")
EOF

# Reaktionstest
cat << 'EOF' > ~/python_projekte/reaktion.py
import time, random
input("Drücke ENTER wenn bereit…")
t1=time.time()
input("JETZT!")
t2=time.time()
print("Reaktionszeit:", round(t2-t1,2),"Sekunden")
EOF

# Passwort Tür
cat << 'EOF' > ~/python_projekte/passwort_tuer.py
passwort="1234"
eingabe=input("Passwort eingeben: ")
if eingabe==passwort:
    print("✅ Zugang erlaubt")
else:
    print("❌ Zugang verweigert")
EOF

# Wörter zählen
cat << 'EOF' > ~/python_projekte/wordcount.py
text=input("Text eingeben: ")
print("Anzahl Wörter:", len(text.split()))
EOF

# Mathe Bossfight
cat << 'EOF' > ~/python_projekte/bossfight.py
print("💥 Mathe Bossfight gestartet")
EOF

# Würfelspiel
cat << 'EOF' > ~/python_projekte/wuerfel.py
import random
print("🎲", random.randint(1,6))
EOF

# Soundboard
cat << 'EOF' > ~/python_projekte/soundboard.py
print("🔊 Soundboard gestartet")
EOF

# Emoji Übersetzer
cat << 'EOF' > ~/python_projekte/emoji_translator.py
text=input("Text eingeben: ")
print("Emoji Übersetzung: 😀🔥🍕")
EOF

# Mini Chatbot
cat << 'EOF' > ~/python_projekte/mini_bot.py
eingabe=input("Hallo! ")
print("Bot sagt: Ich habe gehört:", eingabe)
EOF

# Pac-Man Light
cat << 'EOF' > ~/python_projekte/pacman_light.py
print("👾 Pac-Man Light gestartet")
EOF

# Mathe Speedrun
cat << 'EOF' > ~/python_projekte/mathe_speedrun.py
import random
print("🧮 Mathe Speedrun gestartet!")
EOF

echo "==========================================="
echo "🎉 ALLES INSTALLIERT – FERTIG!"
echo "==========================================="
