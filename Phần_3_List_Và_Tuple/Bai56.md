# BÀI 56: LIST SCLICING

- `Python list slicing`: là một kĩ thuật giúp các bạn có thể truy cập vào 1 khoảng các phần tử trong list thông qua toán tử.

- Sử dụng `list slicing`:

    - Với toán tử: Bạn có thể xác định chỉ số ban đầu, chỉ số kết thúc, bước nhảy của các phần tử trong list mà bạn muốn cắt ra.

    - Cú pháp: `list[start, end, step]`.

    - Giá trị trả về: Một list chứa các phần tử trong list bắt đầu từ chỉ số `start`, kết thúc ở `stop - 1` với bước nhảy là step. Nếu không chỉ rõ step thì giá trị step mặc định là `1`.

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    b = a[2 : 7 : 1] 
    # cắt từ chỉ số 2 đến chỉ số 6 với bước nhảy 1
    c = a[2 : 7 : 2]
    # cắt từ chỉ số 2 đến chỉ số 6 với bước nhảy 2 
    d = a[ : 7]
    # cắ từ chỉ số 0 đến chỉ số 6, bước nhảy 1
    e = a[6 : ]
    # cắt từ chỉ số 6 đến hết, bước nhảy 1
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    ```

    ```python
    # ket qua
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [3, 4, 5, 6, 7]
    [3, 5, 7]
    [1, 2, 3, 4, 5, 6, 7]
    [7, 8, 9]
    ```

## 1. Slicing với chỉ số không âm

- Nếu không có tham số stop thì mặc định giá trị của stop sẽ là chỉ số cuối cùng trong mảng, nếu không có tham số start thì giá trị mặc định của start sẽ là 0.

## 2. Slicing với chỉ số âm

- Ví dụ:

|`a`|2|3|1|5|7|4|3|
|--|--|--|--|--|--|--|--|
|`Negative index`|-7|-6|-5|-4|-3|-2|-1|

```python
a = [2, 3, 1, 5, 7, 4, 3]
b = a[-4 : -1]
c = a[1: -2]
print(b)
print(c)
```

```python
# ket qua
[5, 7, 4]
[3, 1, 5, 7]
```

## 3. Lật ngược list.

- Để lật ngược list các bạn chỉ cần bỏ trống phần `start` và `stop`, phần `step` có giá trị là `-1`.

    ```python
    a = [2, 3, 1, 'python', '28tech']
    b = a[::-1]
    print(b)
    ```

    ```python
    # ket qua
    ['28tech', 'python', 1, 3, 2]
    ```

## 4. Thay đổi giá trị của nhiều phần tử trong một đoạn.

- Bạn có thể thay đổi hoặc xoá một loạt các phần tử trong một đoạn xác định bằng list slicing. Chú ý bạn chỉ có thể gán cho một iterable cho slice mà bạn cắt ra.

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 5, 6]
    a[2 : 5] = ["28tech"]
    # từ phần tử chỉ số 2 đến chỉ số 4 thay bằng "28tech"
    # nếu cho xâu rỗng [] thì sẽ xoá
    print(a)
    ```

    ```python
    # ket qua 
    ```


## 5. Chèn vào xoá với list slicing.

- Thêm vào đầu list.

    ```python
    a = ['x', 'y', 'z']
    a[:0] = [10, 20, 30]
    print(a)
    ```

    ```python
    # ket qua
    [10, 20, 30, 'x', 'y', 'z']
    ```

- Thêm vào cuối list.

    ```python
    a = ['x', 'y', 'z']
    a[len(a):] = [10, 20, 30]
    print(a)
    ```

    ```python
    # ket qua
    ['x', 'y', 'z', 10, 20, 30]
    ```

- Thêm vào giữa list:

    ```python
    # ví dụ 1
    a = [0, 1, 2, 3, 4, 5, 6, 7]

    a[2 : 2] = ['a', 'a', 'a']
    # Thêm vào vị trí thứ 2 của list a a a 
    print(a)
    ```

    ```python
    # ket qua
    [0, 1, 'a', 'a', 'a', 2, 3, 4, 5, 6, 7]
    ```

    ```python
    # ví dụ 2
    a = [0, 1, 2, 3, 4, 5, 6, 7]

    a[2 : 3] = ['a', 'a', 'a']
    # Xoá phần tử thứ 2 và thay vào là a a a
    print(a)
    ```

    ```python
    # ket qua
    [0, 1, 'a', 'a', 'a', 3, 4, 5, 6, 7]
    ```

## 6. Copy một list (deep copy)

```python
a = [1, 2, 3, 4, 5]
b = a[:]
print(b)
print(a)
print(b == a)
print(a is b)
```

```python
# kết quả
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
True
False
```