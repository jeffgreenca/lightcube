![build](https://travis-ci.org/jeffgreenca/lightcube.svg?branch=master) ![coverage](https://sonarcloud.io/api/project_badges/measure?project=jeffgreenca_lightcube&metric=coverage)
[![CircleCI](https://circleci.com/gh/jeffgreenca/lightcube.svg?style=svg)](https://circleci.com/gh/jeffgreenca/lightcube)
# lightcube

A simple web interface to trigger events on my custom light cube.

![lightcube](cube.jpg)

## Hardware
It's an Arduino-based board with a couple colored LEDs placed behind a translucent plastic screen, and accepts on/off commands over USB serial interface such as:
```
1
1
```

First `1` turns on LED 1, second `1` turns off LED one.
