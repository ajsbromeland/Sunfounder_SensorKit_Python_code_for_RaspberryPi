## SunFounder SensorKit Python code for Raspberry Pi

This README is intentionally simplified for **Raspberry Pi 4** wiring.

## What to use on the Pi 4 header

All scripts use:

```python
GPIO.setmode(GPIO.BOARD)
```

So use **physical pin numbers** on the 40-pin header.

### GPIO pins used by this repo

- `3`
- `11`
- `12`
- `13`
- `15`
- `16`
- `18`
- `22`

### Power pins (3.3V)

- `1`
- `17`

### Power pins (5V / "5v5")

- `2`
- `4`

### Ground pins

- `6`
- `9`
- `14`
- `20`
- `25`
- `30`
- `34`
- `39`

## Per-example pin quick reference (BOARD pin numbers only)

| Example | Pins used |
|---|---|
| `01_hall_1.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `01_hall_2.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `01_hall_3.py` | GPIO: `11`, `12`, `13`, `16`; power: `3.3V`, `GND` |
| `02_rgb.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `03_doubleColorLed.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `04_shockSwitch.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `05_knock.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `06_Ir.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `07_laser.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `08_reedSwitch.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `09_IR_receive.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `10_analogTemp.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `11_buzzer.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `11_buzzer_passive.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `12_button.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `13_photo_interrput.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `14_tiltSwitch.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `15_mercurySwitch.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `16_magicCup.py` | GPIO: `11`, `12`, `15`; power: `3.3V`, `GND` |
| `16_raindetection.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `17_ds18b20.py` | DS18B20 through Linux 1-Wire interface; use `3.3V` + `GND` |
| `18_rotaryEncoder.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `19_autoFlashLed.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `20_photoRes.py` | GPIO: `11`, `12`, `13`; power: `3.3V`, `GND` |
| `21_Humiture.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `22_obstacleAvoidance.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `23_Tracking.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `24_microphone.py` | GPIO: `11`, `12`, `13`, `15`; power: `3.3V`, `GND` |
| `25_metalTouch.py` | GPIO: `11`, `12`; power: `3.3V`, `GND` |
| `26_flame.py` | GPIO: `11`; power: `3.3V`, `GND` |
| `27_relay.py` | GPIO: `11`; power: `5V` (typical relay module), `GND` |
| `29_expand01.py` | GPIO: `11`, `12`, `13`, `15`; power: `3.3V`, `GND` |
| `30_expand02.py` | GPIO: `3`, `11`, `12`, `13`, `15`, `16`, `18`, `22`; power: `3.3V`, `GND` |
| `joystickPS2.py` | GPIO: `11`, `12`, `13`, `15`; power: `3.3V`, `GND` |
| `mq-2.py` | GPIO: `11`, `12`, `13`, `16`; power: `3.3V`, `GND` |

