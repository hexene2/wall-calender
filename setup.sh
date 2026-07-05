#!/bin/sh

mkdir -p "$HOME/.config/wall-calender"
cp "config.config" "$HOME/.config/wall-calender/config.config"
cp "background.png" "$HOME/.config/wall-calender/background.png"
sudo cp "wall-update" "/bin/wall-update"