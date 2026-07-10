#!/bin/sh

sudo rm -rf "$HOME/.config/wall-calender"

sudo rm "$HOME/.config/autostart/wall-calendar.desktop"

echo "Autostart disabled!"

sudo systemctl disable --now wall-update.service
sudo rm -f /etc/systemd/system/wall-update.service
sudo rm -f /usr/local/bin/wall-update
sudo systemctl daemon-reload