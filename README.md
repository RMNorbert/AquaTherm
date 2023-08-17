[<img src="https://github.com/RMNorbert/AquaTherm/blob/main/AquaDark.png" alt="AquaTherm" width="300">](README.md)

[![Python](https://img.shields.io/badge/Python-00264D.svg?logo=python&logoColor=gold&labelColor=black&style=for-the-badge)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-472DEC.svg?logo=pandas&logoColor=black&labelColor=gold&style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-darkred.svg?label=SQLA&logoColor=white&labelColor=222222&style=for-the-badge)](https://www.sqlalchemy.org/)
[![Flask](https://img.shields.io/badge/Flask-008080.svg?logo=flask&logoColor=white&labelColor=008080&style=for-the-badge)](https://flask.palletsprojects.com/en/2.3.x/)
[![Prometheus](https://img.shields.io/badge/Prometheus-242526.svg?logo=prometheus&logoColor=white&labelColor=C0362C&style=for-the-badge)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-242526.svg?logo=Grafana&logoColor=DD4F00&labelColor=black&style=for-the-badge)](https://grafana.com/)

[![SQLite](https://img.shields.io/badge/-SQLite-222222.svg?logo=SQLite&logoColor=0052A2&labelColor=222222&style=for-the-badge)](https://www.sqlite.org/index.html)
[![Docker](https://img.shields.io/badge/-docker-blue.svg?logo=docker&logoColor=0197f6&labelColor=222222&style=for-the-badge)](https://www.docker.com/)
[![Arduino](https://img.shields.io/badge/-Arduino-14A3C7.svg?logo=Arduino&logoColor=14A3C7&labelColor=222222&style=for-the-badge)](https://www.arduino.cc/)
[![Raspberry Pi](https://img.shields.io/badge/-Raspberry%20Pi-222222.svg?logo=Raspberrypi&logoColor=black&labelColor=E20B2D&style=for-the-badge)](https://www.raspberrypi.com/)
[![jQuery](https://img.shields.io/badge/-jQuery-222222.svg?logo=jquery&logoColor=lightblue&labelColor=darkblue&style=for-the-badge)](https://jquery.com/)

[![License: MIT](https://img.shields.io/badge/-MIT-blue.svg?label=license&logoColor=white&labelColor=242526&style=for-the-badge)](LICENSE "License")
[![Last Commit](https://img.shields.io/github/last-commit/RMNorbert/ExcelVisualizer?logo=github&label=Last%20Commit&style=for-the-badge&display_timestamp=committer&labelColor=242526)](https://github.com/RMNorbert/ExcelVisualizer/commits "Commit History")
</div>

# AquaTherm

[Table of content:](#description)
- [Used Technologies](#used-technologies)
- [Features](#features)
- [Getting Started](#getting-started)

## Description:

AquaTherm is a project that provides both Desktop and Web GUIs, supporting USB or Wi-Fi connected devices. It involves sensor readings, utilizing Arduino and Raspberry-related products to connect to multiple devices. The project collects sensor data, performs analysis, takes appropriate actions, and communicates with other systems for further processing.

## Used Technologies & Packages:

AquaTherm integrates a range of cutting-edge technologies and packages:

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
- [Arduino](https://www.arduino.cc/)
- [Raspberry Pi](https://www.raspberrypi.com/)
- [jQuery](https://jquery.com/)

## Features

AquaTherm offers a range of features that make it a powerful tool for managing sensor data and automating actions:

- **Temperature and Humidity Reading, Displaying, and Management**
- **Automated Actions for Specific Scenarios:**
  - **Decreasing or Increasing Temperature**
  - **Increasing Aquarium Water Level**

## How Does it Work?

## Getting Started

To get started with AquaTherm, make sure you meet the following prerequisites:

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
