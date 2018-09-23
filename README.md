# Screen Time
Track and view how much you use your computer. Records up to two weeks' usage (Up to 13MB).

Designed for Linux.

![Screen Time - Today](screenshots/today%20-%201.1.png)


![Screen Time - 7 Days](screenshots/7%20days%20-%201.1.png)

## Features
* Logs time spent on the computer.
* View time spent on the computer with a detailed today view, or a 7 day view.
* Also used with [Screen Time GUI](https://github.com/kylecorry31/ScreenTimeGUI) for Windows users (not officially supported)

## Dependencies
* python3
* python3-matplotlib
* python3-numpy
* python3-pip
* python3-toml
* libgtk-3-dev
* libgranite-dev

## Installation
Download this project and run the following commands to install.

```shell
sudo make install
```

*Reboot your computer after installing to start logging screen time.*

## Uninstall
Use the following command to uninstall.

```
sudo make uninstall
```

## Update
Use the following command to update your application from new sources (must download new sources).

```
sudo make update
```

## Usage
To view your screen time, you should use the following command to open the Screen Time application:

```shell
screen_time
```

By default it writes to files in the /screen-time/ directory (week.txt and last-week.txt).

## License
This project is licensed under the [MIT License](LICENSE).

## Credits
Just me for now, but help is always welcome!

## Contribute
Please feel free to contribute to this project, or if you find an issue be sure to report it under issues.
