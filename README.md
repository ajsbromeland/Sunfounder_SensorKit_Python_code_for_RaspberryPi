## SunFounder SensorKit Python code for Raspberry Pi

This repository has been refreshed for **Python 3 on modern Raspberry Pi boards (including Raspberry Pi 400)**.

### What was fixed
- Converted examples to Python 3 syntax (`print(...)`, etc.).
- Removed mixed tabs/spaces that caused `TabError` and `IndentationError` on newer Python versions.
- Repaired broken indentation and other syntax issues in several scripts (`01_hall_3.py`, `04_shockSwitch.py`, `05_knock.py`, `11_buzzer_passive.py`, and `ADC0832.py`).
- Kept all scripts on **BOARD pin numbering** (`GPIO.setmode(GPIO.BOARD)`).

### Raspberry Pi setup notes
- Enable GPIO access and run scripts with permissions that can access `/dev/gpiomem`.
- For DS18B20 examples (`17_ds18b20.py`, `29_expand01.py`, `30_expand02.py`), enable 1-Wire first.
- Several analog examples use `ADC0832.py`; wire the ADC once and reuse it:
  - `CS -> BOARD pin 11`
  - `CLK -> BOARD pin 12`
  - `DIO -> BOARD pin 13`
  - `VCC -> 3.3V`, `GND -> GND`

## GPIO pin guide for each exercise

The examples use `GPIO.setmode(GPIO.BOARD)`, so the pin numbers in code are **physical header pins**.  
To make wiring easier, this table includes both the BOARD pin and the matching BCM GPIO number.

### Common BOARD → BCM map used in this kit

- BOARD 3  → BCM 2
- BOARD 11 → BCM 17
- BOARD 12 → BCM 18
- BOARD 13 → BCM 27
- BOARD 15 → BCM 22
- BOARD 16 → BCM 23
- BOARD 18 → BCM 24
- BOARD 22 → BCM 25

### Exercise wiring quick reference

| Example | GPIO pin guide |
|---|---|
| `01_hall_1.py` | Hall DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `01_hall_2.py` | Hall AO via ADC0832: CS BOARD 11 (BCM 17), CLK BOARD 12 (BCM 18), DIO BOARD 13 (BCM 27) |
| `01_hall_3.py` | Hall DO: BOARD 16 (BCM 23) + ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `02_rgb.py` | RGB LED: R BOARD 11 (BCM 17), G BOARD 12 (BCM 18), B BOARD 13 (BCM 27) |
| `03_doubleColorLed.py` | 2-color LED: R BOARD 11 (BCM 17), G BOARD 12 (BCM 18) |
| `04_shockSwitch.py` | Shock sensor DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `05_knock.py` | Knock sensor DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `06_Ir.py` | IR transmitter module signal: BOARD 11 (BCM 17) |
| `07_laser.py` | Laser module control: BOARD 11 (BCM 17) |
| `08_reedSwitch.py` | Reed DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `09_IR_receive.py` | IR receiver DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `10_analogTemp.py` | Temp AO via ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `11_buzzer.py` | Active buzzer signal: BOARD 11 (BCM 17) |
| `11_buzzer_passive.py` | Passive buzzer signal: BOARD 11 (BCM 17) |
| `12_button.py` | Button: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `13_photo_interrput.py` | Photo interrupter DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `14_tiltSwitch.py` | Tilt switch DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `15_mercurySwitch.py` | Mercury switch DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `16_magicCup.py` | Mercury DO: BOARD 11 (BCM 17), LED1: BOARD 12 (BCM 18), LED2: BOARD 15 (BCM 22) |
| `16_raindetection.py` | Rain AO via ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `17_ds18b20.py` | 1-Wire sensor read from Linux device path; no direct pin setup in script |
| `18_rotaryEncoder.py` | Encoder CLK: BOARD 11 (BCM 17), DT: BOARD 12 (BCM 18), SW: BOARD 13 (BCM 27) |
| `19_autoFlashLed.py` | LED: BOARD 11 (BCM 17) |
| `20_photoRes.py` | Photoresistor AO via ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `21_Humiture.py` | DHT data: BOARD 11 (BCM 17) |
| `22_obstacleAvoidance.py` | Obstacle sensor DO: BOARD 11 (BCM 17) |
| `23_Tracking.py` | Tracking sensor DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `24_microphone.py` | Microphone DO: BOARD 15 (BCM 22) + analog AO via ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `25_metalTouch.py` | Touch sensor DO: BOARD 11 (BCM 17), LED: BOARD 12 (BCM 18) |
| `26_flame.py` | Flame sensor DO: BOARD 11 (BCM 17) |
| `27_relay.py` | Relay IN: BOARD 11 (BCM 17) |
| `29_expand01.py` | RGB LED: BOARD 11/12/13 (BCM 17/18/27), buzzer: BOARD 15 (BCM 22), DS18B20 via 1-Wire |
| `30_expand02.py` | RGB LED: BOARD 15/16/18 (BCM 22/23/24), joystick SW: BOARD 22 (BCM 25), buzzer: BOARD 3 (BCM 2), ADC0832 on BOARD 11/12/13 (BCM 17/18/27), DS18B20 via 1-Wire |
| `joystickPS2.py` | Joystick SW: BOARD 15 (BCM 22) + ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |
| `mq-2.py` | Buzzer: BOARD 16 (BCM 23) + MQ-2 AO via ADC0832 on BOARD 11/12/13 (BCM 17/18/27) |

> Note: If your module labels pins as `GPIO17`, `GPIO18`, etc., use the BCM value in parentheses.
