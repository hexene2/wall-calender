# Wall-Calender

> A simple open source application that modifies your desktop wallpaper by adding a github style calender on wallpaper.

## 📖 About

Project Name is a Wall-Calender written in Python that performs wallpaper modifications using the Pillow library. It is designed to be simple, fast, and easy to use while remaining completely open source.

## ✨ Features

- Lightweight and fast
- Easy to install
- Simple configuration

## 📸 Screenshots



## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hexene2/wall-calen
```

Move into the project directory:

```bash
cd project-name
```

run setup.sh file
```bash
chmod x+ setup.sh
./setup.sh
```
this will add wall-update into /bin . which you can run
```bash
wall-update
```

and make /.congif/well-celender directry. and add config.config and background.png

## config
to config you can do
```bash
nano ~/.config/project-name/config.conf
```
Feel free to change background.png file as you like

## ▶️ Usage

Run the application:
```bash
wall-update
```
this will change the wallpaper

Example configuration:

```ini
# Example settings
Github Style
{
    "scale":3,
    "color":"#0FBF3E",
    "color2":"#24292E",
    "color3":"#91008D",
    "whichMonitor":"HDMI-1",
    "fileName":"wallpaper.png",
    "filepath":"/home/hexene/Pictures",
    "backgroundPNG":"background.png",
    "isBlackBackground":1
}
```

Modify these values to customize the application's behavior.

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project, feel free to fork the repository, make your changes, and submit a pull request.

If you discover a bug or have a feature request, please open an issue.

## 🛣️ Roadmap

- [ ] Add more customization options
- [ ] Improve performance
- [ ] Add GUI
- [ ] Add support for additional operating systems
- [ ] More features...

## 📜 License

This project is licensed under the GNU General Public License (GPL).

See the `LICENSE` file for more information.

## 🙏 Acknowledgements

- Python
- Pillow
- Everyone who contributes to the project

---

If you find this project useful, consider giving it a ⭐ on GitHub!
