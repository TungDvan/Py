# LÀM QUEN

## Bài 1. Print Hello World !

Nhiệm vụ của bạn ở bài tập này rất đơn giản, bạn hãy nhập vào 1 số nguyên x và in ra 3 dòng :

Dòng 1 là số **x** bạn vừa nhập từ bàn phím

Dòng 2 in ra dòng chữ "**Hello World !**"

Dòng 3 in ra "**Python programming !**"

### Đầu vào.

1 dòng duy nhất chứa số nguyên **x**

### Giới hạn

1<=x<=10^9

### Đầu ra

In ra 3 dòng theo yêu cầu

### Sample Input 01

```
5
```

### Sample Output 01

```
5
Hello World !
28tech C++ programming !
```

### Tham khảo

```python
s = input()
print(s)
print("Hello World !")
print("Python programming !")
```

## Bài 2. Print Number

Đề bài yêu cầu bạn nhập :

Dòng 1 là số nguyên **X**

Dòng 2 là số nguyên **Y**

Dòng 3 là kí tự **C**

Dòng 4 là số thực float **F**

Dòng 5 là số thực double **D**.

Nhiệm vụ của bạn là in ra 5 dòng. Dòng 1 in **X**, dòng 2 in **Y**, dòng 3 in **C**, dòng 4 in **F** với 2 số đằng sau dấu phẩy, dòng 5 in **D** với 9 số sau dấu phẩy.

**Chú ý** : Lựa chọn kiểu dữ liệu cho phù hợp

### Đầu vào.

5 dòng lần lượt là **X**, **Y**, **C**, **F**, **D**

### Giới hạn

-10^9<=X<=10^9;

-10^18<=Y<=10^18;

C là kí tự in hoa hoặc in thường;

-10^6<=F<=10^6;

-10^9<=D<=10^9;

### Đầu ra

In ra 5 dòng theo yêu cầu

### Sample Input 01

```
614
999999999999990528
G
19.088
2.9648
```

### Sample Output 01

```
614
999999999999990528
G
19.09
2.964800000
```

### Tham khảo

```python
x = input()
y = input()
c = input()
f = float(input())
d = float(input())
print(x, y, c, '{:.2f}'.format(f), '{:.9f}'.format(d), sep = '\n')
```

## Bài 3. Print Expression

Cho 4 số **X, Y, Z, T** là số nguyên được nhập từ bàn phím.

Bạn hãy in ra 3 dòng

Dòng 1 lần lượt 4 số **Y, Z, X, T** mỗi số cách nhau một dấu phẩy

Dòng 2 in ra **tổng 4 số**

Dòng 3 in ra giá trị của biểu thử **X - Y + Z * T**.

(Chú ý giá trị của tích Z * T và giá trị của tổng 4 số có thể tràn kiểu dữ liệu int)

### Đầu vào.

1 dòng chứa 4 số **X,Y,Z,T**

### Giới hạn

1<=X, Y, Z, T <= 10^9

### Đầu ra

In ra theo yêu cầu đầu bài

### Sample Input 01

```
93 9 93 98
```

### Sample Output 01

```
9,93,93,98
293
9198
```

### Tham khảo

```python
x, y, z, t = map(int, input().split())
print(y, z, x, t, sep = ",")
print(x + y + z + t)
print(x - y + z * t)
```

## Bài 4. Hàm Pow

Cho 2 số x, y. Nhiệm vụ của bạn là tính **x ^ y**

### Đầu vào.

1 dòng chứa 2 số nguyên dương **x, y** viết cách nhau một dấu cách

### Giới hạn

1<=x,y<=12

### Đầu ra

In ra x^y, nếu x^y có phần thập phân thì in ra 2 số sau dấu phẩy, **nếu không có phần thập phân thì không cần in.**

### Sample Input 01

```
2 2
```

### Sample Output 01

```
4
```

### Tham khảo

```python
x, y = map(int, input().split())
print(x ** y)
```

## Bài 5. Hàm sqrt và cbrt

Cho số nguyên dương **N**, nhiệm vụ của bạn là tính c**ăn bậc 2 và căn bậc 3** của N.

### Đầu vào.

Dòng duy nhất chứa số nguyên dương **N**

### Giới hạn

1<=N<=10^9

### Đầu ra

Dòng 1 in ra căn bậc 2 của **N** với **2 số sau dấu phẩy**

Dòng 2 in ra căn bậc 3 của **N** với **3 số sau dấu phẩy**

### Sample Input 01

```
65
```

### Sample Output 01

```
8.06
4.021
```

### Tham khảo

```python
x = int(input())
print('{:.2f}'.format(x**(1/2)), '%.3f' % (x**(1/3)), sep = '\n')
```

## Bài 6. Hàm ceil, floor, round

Hàm **ceil** : làm tròn lên số nguyên gần nhất, **floor** : làm tròn xuống số nguyên gần nhất, **round** : làm tròn số nguyên phụ thuộc vào phần thập phân.

Cho số thực **X** nhiệm vụ của bạn là sử dụng 3 hàm trên để tìm số nguyên nhỏ hơn gần X nhất, số nguyên lớn hơn gần X nhất, số nguyên gần X nhất.

### Đầu vào.

Dòng duy nhất chứa số thực X

### Giới hạn

1<=X<=10^6

### Đầu ra

In ra 3 số trên 3 dòng

### Sample Input 01

```
3.59
```

### Sample Output 01

```
3
4
4
```

### Tham khảo

```python
from math import *

x = float(input())
print(floor(x), ceil(x), round(x), sep = '\n')
```