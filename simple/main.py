#!/usr/bin/python
from simple_device import SimpleDevice

def main():
    device = SimpleDevice()
    device.on_event('device_locked')
    device.on_event('pin_entered')
    print device.state
    device.on_event('device_locked')
    print device.state
    device.on_event('device_locked')

if __name__ == '__main__':
    main()
