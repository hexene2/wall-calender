#!/bin/sh

mkdir -p "$HOME/.config/wall-calender"
cp "config.config" "$HOME/.config/wall-calender/config.config"
cp "background.png" "$HOME/.config/wall-calender/background.png"
sudo cp "wall-update" "/bin/wall-update"


mkdir -p "$HOME/.config/autostart"

cat > "$HOME/.config/autostart/wall-calendar.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Wall Calendar
Exec=/usr/local/bin/wall-update
Terminal=false
X-GNOME-Autostart-enabled=true
EOF

echo "Autostart enabled!"



set -e

echo "Installing Wall Calendar service..."

# Copy executable
sudo install -m 755 wall-update /usr/local/bin/wall-update

# Create service
sudo tee /etc/systemd/system/wall-update.service > /dev/null <<EOF
[Unit]
Description=Wall Calendar

[Service]
ExecStart=/usr/local/bin/wall-update
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable service
sudo systemctl daemon-reload
sudo systemctl enable wall-update.service

echo "Done! The service will start automatically on every boot."
echo "To start it now, run:"
echo "sudo systemctl start wall-update.service"