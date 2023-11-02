# GameBoy 2BPP to image converter

Outputs jpg / png / bmp with same filename representing the contents of the hex file in GameBoy 2BPP Graphics Format.

Usage:

```
$ python3 2bpp_to_image.py mew.hex jpg
```

Dependencies: Python Pillow

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install Pillow
```
