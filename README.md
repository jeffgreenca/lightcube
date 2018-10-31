# lightcube
![coverage](https://sonarcloud.io/api/project_badges/measure?project=jeffgreenca_lightcube&metric=coverage) ![build](https://travis-ci.org/jeffgreenca/lightcube.svg?branch=master)

A simple web interface to trigger events on my custom light cube.

## Hardware
It's an Arduino-based board with a couple colored LEDs placed behind a translucent plastic screen, and accepts on/off commands over USB serial interface such as:
```
1
1
```

First `1` turns on LED 1, second `1` turns off LED one.
