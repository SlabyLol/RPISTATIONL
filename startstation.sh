#!/bin/bash

while true; do
    clear
    echo "==============================================="
    echo "       WELCOME TO RaspberryPi' STATION!"
    echo "==============================================="
    echo ""
    echo "[!] Alles nur mit Erlaubnis von Tobias Musch!"
    echo ""
    echo "PROGRAMME & TOOLS:"
    echo "------------------------------------------"
    echo "1) Scratch"
    echo "2) Scratch 3"
    echo "3) Terminal (lxterminal)"
    echo "4) Firefox"
    echo "5) Visual Studio Code"
    echo "6) Minecraft Reborn"
    echo "------------------------------------------"
    echo "SPIELE & MINI-PROJEKTE:"
    echo "------------------------------------------"
    echo "7) LED Simulator"
    echo "8) LED Farben Demo"
    echo "9) Zahlenraten"
    echo "10) Text Adventure"
    echo "11) Reaktionstest"
    echo "12) Passwort-Tür"
    echo "13) Wörter zählen"
    echo "14) Snake"
    echo "15) Flappy Bird"
    echo "16) Bomberman"
    echo "17) Mathe Bossfight"
    echo "18) Würfelspiel"
    echo "19) Soundboard"
    echo "20) Emoji Übersetzer"
    echo "21) Mini Chatbot"
    echo "22) Pac-Man Light"
    echo "23) Mathe Speedrun"
    echo "------------------------------------------"
    echo "TERMINAL-EFFEKTE:"
    echo "24) Hollywood Hacker Terminal"
    echo "25) Matrix Effekt (cmatrix)"
    echo "26) Zug Animation (sl)"
    echo "------------------------------------------"
    echo "27) Beenden"
    echo ""

    read -p "Deine Auswahl: " choice

    case $choice in
        1) scratch ;;
        2) scratch3 ;;
        3) lxterminal ;;
        4) firefox ;;
        5) code ;;
        6) mcpi-reborn ;;
        7) python3 ~/python_projekte/led_simulator.py ;;
        8) python3 ~/python_projekte/led_rainbow.py ;;
        9) python3 ~/python_projekte/raten.py ;;
        10) python3 ~/python_projekte/adventure.py ;;
        11) python3 ~/python_projekte/reaktion.py ;;
        12) python3 ~/python_projekte/passwort_tuer.py ;;
        13) python3 ~/python_projekte/wordcount.py ;;
        14) python3 ~/python_projekte/snake.py ;;
        15) python3 ~/python_projekte/flappy.py ;;
        16) python3 ~/python_projekte/bomber.py ;;
        17) python3 ~/python_projekte/bossfight.py ;;
        18) python3 ~/python_projekte/wuerfel.py ;;
        19) python3 ~/python_projekte/soundboard.py ;;
        20) python3 ~/python_projekte/emoji_translator.py ;;
        21) python3 ~/python_projekte/mini_bot.py ;;
        22) python3 ~/python_projekte/pacman_light.py ;;
        23) python3 ~/python_projekte/mathe_speedrun.py ;;
        24) hollywood ;;
        25) cmatrix ;;
        26) sl ;;
        27) echo "Beendet." ; exit 0 ;;
        *) echo "Ungültige Eingabe!" ; sleep 1 ;;
    esac
done
