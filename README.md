# microbit-serial-to-processing
control software (processing in python mode) using the micro:bit (over USB)

## steps:

1. Get firmware onto microbit:

* To upload the microbit firmware drag microbit-serial-out.hex into the micro:bit flash drive

* Alternatively create the hex file from block code [here](https://makecode.microbit.org/_MeEiY9aPHA47)

* Alternatively use the javascript to create the hex file:

```javascript
let diff = 0
let yOld = 0
let yNew = 0
let averaging = 0
let counter = 0
counter = 0
averaging = 3
yOld = input.acceleration(Dimension.Z)
basic.forever(() => {
    counter += 1
    yNew = input.acceleration(Dimension.Z)
    diff += yNew - yOld
    if (counter == averaging) {
        serial.writeNumber(diff / averaging)
        counter = 0
        diff = 0
    }
})
```
2. Make sure the microbit is plugged in via usb and all serial monitors are closed 

3. Run mBitSerial.pyde in the processing environment

4. Hold the microbit upright and press reset. Change the orientation of the microbit and the line in the processing app should change to mirror the state of the microbit
