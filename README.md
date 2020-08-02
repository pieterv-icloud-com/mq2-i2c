# mq2-i2c

Will act as a mq2 i2c slave device.

Basing a lot of the work on these:

[Step by Step Guide on Making an I2C Slave Device with an Arduino](http://dsscircuits.com/articles/arduino-i2c-slave-guide)

[micropython-MQ](https://github.com/kartun83/micropython-MQ)

[i2cslave — Two wire serial protocol slave](https://circuitpython.readthedocs.io/en/5.0.x/shared-bindings/i2cslave/__init__.html)

[Trinket M0 Pinouts](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino)

[How MQ2 Gas/Smoke Sensor Works? & Interface it with Arduino](https://lastminuteengineers.com/mq2-gas-senser-arduino-tutorial/)

I have an Arduino Trinket M0 for this project, so I will be implementing this in CircuitPython as a first try.

## Device Details

|||
| ---| ---|
| **Device Address:** | 0x29 |

## Register Map

| Address | Register Description |
| --------| ---------------------|
| 0x00    | Status               |
| 0x01    | Smoke                |
| 0x02    | LPG                  |
| 0x03    | Methane              |
| 0x04    | Hydrogen             |

## Wiring

| Qwiiq Connector | Trinket M0 | MQ2 |
| --------------- | ---------- | --- |
| Black (GND)     | Gnd        | GND |
| Red (3.3V)      | Bat        |     |
| Blue (SDA)      | 0          |     |
| Yellow (SCL)    | 2          |     |
|                 | 3V         | VCC |
|                 | 3 (A3)     | A0  |


 