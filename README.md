# mq2-i2c

Will act as a mq2 i2c slave device.

Basing a lot of the work on these:

[Step by Step Guide on Making an I2C Slave Device with an Arduino](http://dsscircuits.com/articles/arduino-i2c-slave-guide)

[micropython-MQ](https://github.com/kartun83/micropython-MQ)

[i2cslave — Two wire serial protocol slave](https://circuitpython.readthedocs.io/en/5.0.x/shared-bindings/i2cslave/__init__.html)

[Trinket M0 Pinouts](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino)

[How MQ2 Gas/Smoke Sensor Works? & Interface it with Arduino](https://lastminuteengineers.com/mq2-gas-senser-arduino-tutorial/)

I have an Adafruit Trinket M0 for this project, so I will be implementing this in CircuitPython as a first try.

So i2cslave is not supported on the Trinket due to space constraints, could try and build from source:

[CircuitPython Trinket M0 supports i2c slave? ](https://forums.adafruit.com/viewtopic.php?f=52&t=150431&p=744027&hilit=i2cslave#p744027)

[Build Instructions](https://learn.adafruit.com/building-circuitpython/introduction)

Edit: ports/atmel-samd/boards/trinket_m0/mpconfigboard.mk

```C
CIRCUITPY_I2CPERIPHERAL = 1
CIRCUITPY_AUDIOIO = 0
CIRCUITPY_AUDIOBUSIO = 0
CIRCUITPY_BITBANGIO = 0
CIRCUITPY_PULSEIO = 0
```

This will produce a build small enough so it will fit on the Trinket M0.

**Note:** Building V6 here, so we are now using `I2CPeripheral` instead of `I2CSlave'.

## Device Details

|||
| ---| ---|
| **Device Address:** | 0x29 |
| **Device Address:** | 0x30 |

`I2CPeriperal` constructor requires a tuple of addresses, not sure why.

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


 