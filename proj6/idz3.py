#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    strn = input()
    print(''.join(sorted(set(strn), key=strn.index)))


