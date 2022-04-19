# Samsung-MDC

Serial control for Samsung MDC (Multiple Display Control).

## Why?

I got my hands on a Samsung 400DXn-2 screen. It was "key-locked", so was not able to use the menus. I was not able to
find a download of the official Samsung MDC software. I did find the protocol
specification: https://vgavro.github.io/samsung-mdc/MDC-Protocol.pdf

My program allows you to easily unlock the key-lock using the serial port. Do make sure you have the right kind of
serial cable, I tried a few out of my old serial box and after testing a few, I found one with the correct pin layout.

The code ignores the ID of the screen and sends the command to any screen (0xFE).

Enjoy!