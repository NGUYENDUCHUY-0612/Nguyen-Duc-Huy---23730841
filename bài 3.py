# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:01:59 2024

@author: Nguyễn Đức Huy
"""

n = int(input("Nhập vào số nguyên n: "))
a = n // 10
b = n % 10
if n > 9 and n < 100:
    print("Tổng các chữ số của {n} là: ",a +b )   
else:
    print ("Số bạn vừa nhập không hợp lệ")
    
