#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    st1 = input()
    st2 = input()
    l1 = ""
    l2 = ""
    for i in st1:
        if i not in st2:
            l1 += i
    for i in st2:
        if i not in st1:
            l2 += i
    print(l1, l2)






