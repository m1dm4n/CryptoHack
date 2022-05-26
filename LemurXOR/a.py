'''from PIL import Image

lemur = Image.open("D:\code\ctf\cryptohack\LemurXOR\\flag_7ae18c704272532658c10b5faad06d74.png")
flag = Image.open("D:\code\ctf\cryptohack\LemurXOR\lemur_ed66878c338e662d3473f0d98eedbd0d.png")
pixels_lemur = lemur.load() # create the pixel map
pixels_flag = flag.load()

for i in range(lemur.size[0]): # for every pixel:
    for j in range(lemur.size[1]):
        # Gather each pixel
        l = pixels_lemur[i,j]
        f = pixels_flag[i,j]

        # XOR each part of the pixel tuple
        r = l[0] ^ f[0]
        g = l[1] ^ f[1]
        b = l[2] ^ f[2]

        # Store the resulatant tuple back into an image
        pixels_flag[i,j] = (r, g, b)

flag.show()
'''
from PIL import Image
from pwn import xor

lemur = Image.open("D:\code\ctf\cryptohack\LemurXOR\\flag_7ae18c704272532658c10b5faad06d74.png")
flag = Image.open("D:\code\ctf\cryptohack\LemurXOR\lemur_ed66878c338e662d3473f0d98eedbd0d.png")
a = lemur.tobytes()
b = flag.tobytes()

c= xor(a , b)

f = Image.frombytes(flag.mode, flag.size, c)
f.show()