#!/usr/bin/python3
"""ASCII alphabet lowercase except q and e"""
for i in range(ord('a'), ord('z') + 1):
    if i == ord('e') or i == ord('q'):
        continue
    else:
        print('{:c}'.format(i), end='')
