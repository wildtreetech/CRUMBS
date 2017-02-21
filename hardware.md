# Hardware

The hardware should be as simple as possible and able to function for
weeks at a time while attached to a motorbike being driven in hot, dusty,
wet, off-road conditions.

During the trip it should record data, reading is not required. It should
operate without requiring a human to remember that it is there. It is the
backup system so trading features for robustness is a good trade off.

## Electronics
The current design is based on combining a ESP8266 and a GPS module.

Hardware in hand for prototyping:
* [Adafruit Feather ESP8266](https://www.adafruit.com/product/2821)
* [Adafruit Ultimate GPS](https://www.adafruit.com/product/746)

These are expensive but easy to obtain and of known quality.

Undecided components:
* battery ([LiPo from Adafruit](https://www.adafruit.com/product/258), capacity?)
* SD card reader ([Adafruit](https://www.adafruit.com/product/254), or [RobotShop](http://www.robotshop.com/eu/en/micro-sd-breakout-board.html?gclid=Cj0KEQiA56_FBRDYpqGa2p_e1MgBEiQAVEZ6-2htR87RpM-ml2_4WOqBBEv1aE29_P1kFiN2ci4KYP4aAsGi8P8HAQ)
* interface to motorbike 12V and recharging of internal battery


## Case
There is no design yet. It needs to safely house all the components, and
safely (re)attach to a motorbike of unknown brand. See [#4](https://github.com/wildtreetech/CRUMBS/issues/4) for ideas.
