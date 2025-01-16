#!/usr/bin/python3
"""ASCII alphabet lowercase except q and e"""
for i in range(ord('a'), ord('z') + 1):
    if i == 'e' or i == 'q':
        continue
    else:
        print('{:c}'.format(i), end='')
