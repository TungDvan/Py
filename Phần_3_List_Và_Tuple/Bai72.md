# BÀI 72: TUPLE

## Giới thiệu về Tuple

- Tuple: là một collection có thứ tự trong Python.

    - Tuple are ordered: Các phần tử lưu trong Tuple có thứ tự.

    - Accessed by index: Truy cập các phần tử trong tuple thông qua chỉ số.

    - Tuple can contain any sort of object: Tuple có thể chứa các phần tử ở mọi loại object như int, float, string, tuple, list,...

    - Tuple are immutable: Tuple không thể thay đổi, tức là không thể chèn, sửa, xoá.

## 1. Tạo Tuple.

- Để tạo một tuple ta đưa các phần tử của tuple vào trong đóng mở ngoặc trong.

    ```python
    a = (1, 2, 3)
    b = (2804, ) # nếu ta để (2804) thì c nó hiểu là số 2804 chứ không phải một tuple
    print(type(a))
    ```

    ```python
    # ket qua
    <class 'tuple'>
    ```

- Tạo tuple thông qua constructor tuple():

    ```python
    s = 'sting'
    b = tuple(s)
    c = tuple([2, 4, 5])
    print(b, c, sep = '\n')
    ```

    ```python
    ('s', 't', 'i', 'n', 'g')
    (2, 4, 5)
    ```

## 2. Nested tuple.

- Tuple có thể chứa mọi object trong Python vì thế nó cũng có thể chứa một tuple khác:

    ```python
    a = ("tuple", (1, 2, 3), 23)
    print(type(a))
    ```

    ```python
    <class 'tuple'>
    ```

## 3. Tuple unpacking.

## 4. Truy cập các phần tử trong Tuple.

- Tương tự như list các bạn có thể truy cập vào các item trong tuple thông qua chỉ số tính tử 0, tuple cũng hỗ trợ chỉ số âm.

    ```python
    a = (1, 2, 3, 4, 5)
    for i in range(len(a)):
        print(a[i], end = ' ')
    ```

## 5. Thay đổi tuple.

- Tuple không thể thay đổi giá trị nhưng nếu item trong tuple là object có thể thay đổi được thì bạn vẫn có thể thay đổi các item đó.

    ```python
    a = ('tung', 'dep', 'trai')
    a[0] = ['Dvan']
    print(a[0])
    ```

    ```python
    # ket qua
    TypeError: 'tuple' object does not support item assignment
    ```

    ```python
    a = ('tung', 'de', [1, 2, 3], 'trai')
    a[2][0] = 1000
    print(a)
    ```

    ```python
    # ket qua
    ('tung', 'de', [1000, 2, 3], 'trai')
    ```

- Dù tuple không thể thay đổi nhưng bạn có thể xoá luôn cả tuple.

## 6. Tuple concatenation và Repetition.

- Các bạn có thể nói tuple hoặc lặp lại tuple.

    ```python
    a = ('tung', 'dep', 'trai')
    b = ('co', 'mot', '02')
    c = a + b
    print(c)
    ```

    ```python
    # ket qua
    ('tung', 'dep', 'trai', 'co', 'mot', '02')
    ```

    ```python
    a = ('tung', 'dep', 'trai')
    b = a * 3
    print(b)
    ```

    ```python
    # ket qua
    ('tung', 'dep', 'trai', 'tung', 'dep', 'trai','tung', 'dep', 'trai')
    ```

## 7. Sắp xếp tuple

- Cách 1: Sử dụng hàm built-in sorted sau đó convert ngược lại tuple.

    ```python
    a = (5, 1, 2, 4, 3)
    a = tuple(sort(a))
    print(a)
    ```

    ```python
    # ket qua
    (1, 2, 3, 4, 5)
    ```

- Cách 2: Convert tuple sang list rồi sử dụng hàm sort của list.

    ```python
    a = (1, 5, 4, 3, 2)
    b = list(a)
    b.sort()
    a = tuple(b)
    print(a)
    ```

    ```python
    (1, 2, 3, 4, 5)
    ```

- Hàm `sort` là một hàm trả về một list, nên ta mới phải ép kiểu sang tuple.

## 8. count() và index()

- Tuple hỗ trợ 2 hàm là count() để đến số lần xuất hiện của một phần tử trong một tuple và index() để trả về chỉ số đầu tiên của một phần tử trong tuple.

- Chú ý: Khi sử dụng hàm index hãy đảm bảo giá trị bạn cần kiểm tra chỉ số xuất hiện trong tuple, không sẽ xảy ra lỗi ValueError.