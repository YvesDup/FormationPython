import io
import time

begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
print(f'{len(buffer) = }')
seconds = end - begin
print("Concat:", seconds)

begin = time.time()
byte = io.BytesIO(b"")
for i in range(0, 50000):
   byte.write(b"Hello World")
end = time.time()
print(f'{len(byte.getbuffer()) = }')
seconds = end - begin
print("BytesIO:", seconds)

with open("test.dat", "wb") as f:
    f.write(byte.getvalue())