import board
from i2cperipheral import I2CPeripheral

address1 = 0x29
address2 = 0x30

regs = [0] * 16
index = 0

with I2CPeripheral(board.SCL, board.SDA, (address1, address2)) as slave:
    while True:
        r = slave.request()
        if not r:
            # Maybe do some housekeeping
            continue
        with r:  # Closes the transfer if necessary by sending a NACK or feeding the master dummy bytes
            if r.address == address1:
                if not r.is_read:  # Master write which is Slave read
                    b = r.read(1)
                    if not b or b[0] > 15:
                        break
                    index = b[0]
                    b = r.read(1)
                    if b:
                        regs[index] = b[0]
                elif r.is_restart:  # Combined transfer: This is the Master read message
                    n = r.write(bytes([regs[index]]))
                #else:
                    # A read transfer is not supported in this example
                    # If the Master tries, it will get 0xff byte(s) by the ctx manager (r.close())
