# BÀI 59: 3 DẠNG TOÁN CƠ BẢN TRÊN MẢNG 1 CHIỀU

## Kiểm tra trong list đâu là những số nguyên tố

```python
import math

def nt(x):
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0: return False
    return x > 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for x in a:
        if nt(x): print(x, end = ' ')
```

## Tìm max, min

```python
import math

def nt(x):
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0: return False
    return x > 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    min_value = 1e18
    max_value = -1e18
    for x in a:
        if min_value > x: min_value = x
        if max_value < x: max_value = x
    print("min_value:", min_value)
    print("max_value:", max_value)
```

## Kiểm tra các cặp phần tử trong list thoả mãn điều kiện gì đó.