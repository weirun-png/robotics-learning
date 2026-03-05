# -*- coding: utf-8 -*-
"""NumPy 基础测试 - 机器人学数学基础"""
import numpy as np

print("=== NumPy 版本 ===")
print("版本:", np.__version__)

print("\n=== 矩阵乘法（机器人运动学基础）===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A =\n", A)
print("B =\n", B)
print("A × B =\n", A @ B)

print("\n=== 旋转矩阵（绕 Z 轴旋转 90 度）===")
theta = np.pi / 2
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
print("Rz =\n", Rz)

print("\n=== 单位矩阵 ===")
I = np.eye(3)
print("I =\n", I)

print("\n✅ NumPy 测试完成！")
