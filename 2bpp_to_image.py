import sys
from PIL import Image

def draw(data_buf):
    colors = [(0xff, 0xff, 0xff),
        (0xaa, 0xaa, 0xaa),
        (0x55, 0x55, 0x55),
        (0x00, 0x00, 0x00)]

    chunks = [data_buf[i:i+16] for i in range(0, len(data_buf), 16)]
    bitlen = len(data_buf)*8
    height = (bitlen//2)//160

    img = Image.new('RGB', (160, height), "white")
    pixels = img.load()

    for c in range(len(chunks)):
        chunk_x = c%20
        chunk_y = c//20
        for i in range(0, 16, 2):
            (a, b) = (chunks[c][i], chunks[c][i+1])
            a_bits = list(map(lambda x: int(x), list(bin(a)[2:].zfill(8))))
            b_bits = list(map(lambda x: int(x), list(bin(b)[2:].zfill(8))))
            for j in range(len(a_bits)):
                color = colors[((a_bits[j] << 1) | b_bits[j])]
                pixels[chunk_x*8+j, chunk_y*8+i//2] = color
    return img

if len(sys.argv) < 2:
    print("Please provide hex file name.")
    sys.exit(1)

with open(sys.argv[1], "r") as hex_dump:
    byte_data = bytes.fromhex(hex_dump.read()[:-1])
    image = draw(byte_data)

    image.show()

    format_suffix = "bmp"
    if len(sys.argv) > 2 and sys.argv[2] in ["jpg", "png", "bmp"]:
        format_suffix = sys.argv[2]

    image.save(sys.argv[1].split(".")[0] + "." + format_suffix)

