# LoRa-microchip-RN2483
Repository for RN2483 project 
### What is it 
This repo is a backup for all the code linked to the LoRa project 
Which is based on RN2483 chip 
### How to use
Insert commands through UART into RN2483
## STM32F103C8T6
To run on Blue Pill STM32F103 microcontroler first download the libraries for Arduino IDE from:

[STM32duino](https://github.com/stm32duino)
 
then install necesarry libraries and set in tools

* Board Generic STM32F103 series 
* Variant STM32F103C8 20kB RAM 64kB flash 
* Clock speed normal 72MHz
* Upload method Serial
* Optimize Smallest


## Server side
To run Raspberry as data receiver/server
set IP as static
download scripts presented below:
* receive2.py
* transform_data.py
* sqlite3.py
* drop_all.py

run script receive2.py

done for 17.12.2018
