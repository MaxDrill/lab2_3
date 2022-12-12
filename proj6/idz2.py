#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = input()
    if "," in a:
        print(a[:a.find(',')].count('н'))
    else:
        print("в предложении нет ,")


