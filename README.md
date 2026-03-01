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

## Wiring quick reference (BOARD pins)

| Example | Required signal pins |
|---|---|
| `01_hall_1.py` | Hall DO: 11, LED: 12 |
| `01_hall_2.py` | ADC0832 (11/12/13) + Hall AO to ADC channel |
| `01_hall_3.py` | Hall DO: 16 + ADC0832 (11/12/13) |
| `02_rgb.py` | RGB LED: R=11, G=12, B=13 |
| `03_doubleColorLed.py` | 2-color LED: R=11, G=12 |
| `04_shockSwitch.py` | Shock sensor DO: 11, LED: 12 |
| `05_knock.py` | Knock sensor DO: 11, LED: 12 |
| `06_Ir.py` | IR transmitter/LED module: 11 |
| `07_laser.py` | Laser module control: 11 |
| `08_reedSwitch.py` | Reed DO: 11, LED: 12 |
| `09_IR_receive.py` | IR receiver DO: 11, LED: 12 |
| `10_analogTemp.py` | ADC0832 (11/12/13) + temp sensor AO to ADC channel |
| `11_buzzer.py` | Active buzzer: 11 |
| `11_buzzer_passive.py` | Passive buzzer: 11 |
| `12_button.py` | Button: 11, LED: 12 |
| `13_photo_interrput.py` | Photo interrupter DO: 11, LED: 12 |
| `14_tiltSwitch.py` | Tilt switch DO: 11, LED: 12 |
| `15_mercurySwitch.py` | Mercury switch DO: 11, LED: 12 |
| `16_magicCup.py` | Mercury DO: 11, LED1: 12, LED2: 15 |
| `16_raindetection.py` | ADC0832 (11/12/13) + rain AO to ADC channel |
| `17_ds18b20.py` | Uses Linux 1-Wire device path (no direct GPIO set in script) |
| `18_rotaryEncoder.py` | Encoder A: 11, B: 12, Button: 13 |
| `19_autoFlashLed.py` | LED: 11 |
| `20_photoRes.py` | ADC0832 (11/12/13) + photoresistor AO to ADC channel |
| `21_Humiture.py` | DHT data: 11 |
| `22_obstacleAvoidance.py` | Obstacle sensor DO: 11 |
| `23_Tracking.py` | Tracking sensor DO: 11, LED: 12 |
| `24_microphone.py` | Microphone DO: 15 + ADC0832 (11/12/13) for analog read |
| `25_metalTouch.py` | Touch sensor DO: 11, LED: 12 |
| `26_flame.py` | Flame sensor DO: 11 |
| `27_relay.py` | Relay IN: 11 |
| `29_expand01.py` | RGB LED: 11/12/13, buzzer: 15, DS18B20 via 1-Wire |
| `30_expand02.py` | RGB LED: 15/16/18, joystick button: 22, buzzer: 3, ADC0832 (11/12/13), DS18B20 |
| `joystickPS2.py` | Joystick button: 15 + ADC0832 (11/12/13) |
| `mq-2.py` | Buzzer: 16 + ADC0832 (11/12/13) |

> Note: `BOARD` pins are physical header pin numbers, not BCM GPIO numbers.
