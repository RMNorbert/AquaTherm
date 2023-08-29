[<img src="https://github.com/RMNorbert/AquaTherm/blob/main/AquaDark.png" alt="AquaTherm" width="300">](README.md)

[![Python](https://img.shields.io/badge/Python-00264D.svg?logo=python&logoColor=gold&labelColor=black&style=for-the-badge)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-472DEC.svg?logo=pandas&logoColor=black&labelColor=gold&style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-darkred.svg?label=SQLA&logoColor=white&labelColor=222222&style=for-the-badge)](https://www.sqlalchemy.org/)
[![Flask](https://img.shields.io/badge/Flask-008080.svg?logo=flask&logoColor=white&labelColor=008080&style=for-the-badge)](https://flask.palletsprojects.com/en/2.3.x/)
[![Prometheus](https://img.shields.io/badge/Prometheus-242526.svg?logo=prometheus&logoColor=white&labelColor=C0362C&style=for-the-badge)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-242526.svg?logo=Grafana&logoColor=DD4F00&labelColor=black&style=for-the-badge)](https://grafana.com/)

[![jQuery](https://img.shields.io/badge/-jQuery-222222.svg?logo=jquery&logoColor=lightblue&labelColor=darkblue&style=for-the-badge)](https://jquery.com/)
[![SQLite](https://img.shields.io/badge/-SQLite-222222.svg?logo=SQLite&logoColor=0052A2&labelColor=222222&style=for-the-badge)](https://www.sqlite.org/index.html)
[![Docker](https://img.shields.io/badge/-docker-blue.svg?logo=docker&logoColor=0197f6&labelColor=222222&style=for-the-badge)](https://www.docker.com/)
[![Arduino](https://img.shields.io/badge/-Arduino-14A3C7.svg?logo=Arduino&logoColor=14A3C7&labelColor=222222&style=for-the-badge)](https://www.arduino.cc/)
[![Raspberry Pi](https://img.shields.io/badge/-Raspberry%20Pi-222222.svg?logo=Raspberrypi&logoColor=black&labelColor=E20B2D&style=for-the-badge)](https://www.raspberrypi.com/)
![Digi](https://img.shields.io/badge/-Digi-blue.svg?label=XCTU-XBEE&logo=Digi&logoColor=white&labelColor=242526&style=for-the-badge)

[<img src="https://github.com/RMNorbert/AquaTherm/blob/main/images/connection.png" alt="usb" width="350">](#getting-started)

[![License: MIT](https://img.shields.io/badge/-MIT-blue.svg?label=license&logoColor=white&labelColor=242526&style=for-the-badge)](LICENSE "License")
[![Last Commit](https://img.shields.io/github/last-commit/RMNorbert/AquaTherm?logo=github&label=Last%20Commit&style=for-the-badge&display_timestamp=committer&labelColor=242526)](https://github.com/RMNorbert/AquaTherm/commits "Commit History")

</div>

# AquaTherm

[Table of content:](#description)
- [Used Technologies And Packages](#used-technologies-and-packages)
- [Features](#features)
- [Used Sensors](#used-sensors)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [License](#license)
  
## Description

AquaTherm is a project that designed to revolutionize aquarium management by ensuring precise control over temperature and water levels. While offering both Desktop and Web GUIs, involves sensor readings, collecting sensor reading data, performing analysis, taking appropriate actions according to collected data and communicating with other systems for further processing, by utilizing and connecting multiple Arduino and Raspberry-related products to multiple devices through USB, Wi-Fi or Radio communication.

## Used Technologies And Packages

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
- [cAdvisor](https://github.com/google/cadvisor)
- [Node exporter](https://github.com/prometheus/node_exporter)
- [Arduino](https://www.arduino.cc/)
- [Raspberry Pi](https://www.raspberrypi.com/)
- [Digi](https://www.digi.com/)
- [jQuery](https://jquery.com/)

## Features

**AquaTherm offers a range of features that make it a powerful tool for managing sensor data and automating actions:**

 **Temperature and Humidity Reading, Displaying, and Management**

 **Automated Actions for Specific Scenarios:**
  **Decreasing Temperature, Increasing Aquarium Water Level**

## Used Sensors
  
  - DHT22
  - SR04
     
## Getting Started

**- The Arduino Software (IDE) was used during the creation of the sensor controlling releated codes.**

**To upload the codes to the board('s) :**
  1. [Download](https://www.arduino.cc/en/software) and install the Arduino Software IDE.
  2. Connect your Arduino board to your device.
  3. Open the Arduino Software (IDE).

The Arduino Integrated Development Environment - or Arduino Software (IDE) - connects to the Arduino boards to upload programs and communicate with them. Programs written using Arduino Software (IDE) are called sketches. These sketches are written in the text editor and are saved with the file extension .ino.

  4. Select the right board & port. This is done from the toolbar. Make sure you select the board that you are using. If you cannot find your board, you can add it from the board manager in the sidebar.
  5. To upload the code to your board, simply click on the arrow in the top left corner. This process takes a few seconds, and it is important to not disconnect the board during this process. If the upload is successful, the message "Done uploading" will appear in the bottom output area.
  6. Once the upload is complete, you can use the board with the sensors specified in the **Used Sensor** section.
 
**- For Raspberry Pi:**
**To upload the codes to the board('s) :**
  1. [Download](https://www.raspberrypi.com/software/) and install the Raspberry Pi Imager and follow the [instructions](https://www.raspberrypi.com/documentation/computers/getting-started.html) provided on the official page.
  2. After the installation you can use the board with the sensors specified in the **Used Sensor** section.

In either cases both the pin in the sensor controller files and baud rate can be customized in both the sensor controller files and the python files in ./sensor/arduino directory and the ./sensor/raspberry directory if the values i used are not adequate. The pins(2 - temperature and humidity, 13 - distance, 3 - fan , 5 - tap) the baud rate 115200

**- For Radio Communication :**
  1. 2 Xbee Radios modell, to program the radios, a SparkFun USB Explorer needed and finally an Xbee Shield. The shield allows you to plug the Xbee radio into the Arduino.
  2. [Download](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu) and install the XCTU software to program the radios. AES encryption can be created during the configuration of the connected radio.
  3. Set the port and the baud rate . 


**- To get started with AquaTherm, make sure you meet the following prerequisites:**

- Python installed on your machine. [Download Python](https://www.python.org/) from the official website and follow the installation instructions.

If you plan to deploy AquaTherm using Docker containers, follow these steps:

 Install Docker:
   - For Linux: Follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/).
   - For Windows or macOS: Install [Docker Desktop](https://www.docker.com/products/docker-desktop) for an easy-to-use Docker environment.

   After installing Docker, ensure it's running by opening a terminal or command prompt and running the command `docker --version`.

   **Note:** Docker is optional and recommended for deployment scenarios. If you're using Docker, it can help manage dependencies and ensure consistent environments.
   
   
### Installation
**1. Clone the repository:**

   Start by cloning the AquaTherm repository to your local machine. Open a terminal or command prompt and run the following command:

   ```
   git clone https://github.com/RMNorbert/AquaTherm.git
   ```
   install the required packages with the following command:
   ```
   pip install -r requirements.txt
   ```
   if raspberry sensors used install the the required package with the following command:
   bash
   ```
   pip install adafruit-circuitpython-dht
   ```
   C library for interacting with Linux GPIO device:
   ```
   sudo apt-get install libgpiod2
   ```
**2. A, Run the Desktop app with:**

   bash
   ```
   python3 main.py
   ```
**2. B, Run the Web app with:**
   bash
   ```
   python3 web_app.py
   ```
 Access the application:
 Once the Web app is running, you can access it in your web browser at http://localhost:5000.

 **2. C, Run the dockerized version with:**
   - Navigate to the project directory containing the ```docker-deploy.yml``` file.
   - Run the command ```docker-compose up --build``` to build and start the project.

   The `docker-deploy.yml` file defines the services and configurations needed for running your application in a Docker container. It simplifies deployment and ensures consistent setups across environments.

 Access the application:
 
 Once the Web app is running, you can access it in your web browser at http://localhost:5000.
 
 Access Prometheus at http://localhost:9090
 
 Grafana at http://localhost:3000
 
## License

This project is licensed under the MIT License - see the [License](License) file for details.

##
Then sensor controller files can be simulated on https://wokwi.com/ or
with the VS code extension named : Wokwi Simulator
