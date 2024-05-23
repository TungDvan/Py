# BÀI 55: COPY LIST VÀ LIST LÀM THAM SỐ CHO HÀM

```python
a = [1, 2, 3, 4]
b = a
print(a is b)
```

```python
# ket qua
True
```

- Giải thích: Câu lệnh b = a tức là câu lệnh gán địa chỉ của a cho b, vậy nên lúc này b và a có cùng địa chỉ hay chính là b là a. Vậy nếu thay đổi giá trị trên a thì nó cũng thay đổi trên b (a và b cùng một đối tượng).

    ```python
    a = [1, 2, 3]
    b = a

    print(id(a), id(b))
    a[1] = 1000
    print(a, b, sep = '\n')
    ```

    ```python
    # ket qua
    2795475818752 2795475818752       
    [1, 1000, 3]
    [1, 1000, 3]
    ```

- Vậy nếu ta muốn copy một list để thay đổi một số giá trị của list a không làm ảnh hưởng đến list b thì ta phải dử dụng câu lệnh `b = a.copy()`.

    ```python
    a = [1, 2, 3, 4]
    b = a.copy()
    print(id(a), id(b))
    b[2] = 1000
    print(a)
    print(b)
    ```

    ```python
    # ket qua
    2345033783552 2345033781632
    [1, 2, 3, 4]
    [1, 2, 1000, 4]
    ```

- Nếu hàm có truyền tham số là một list.

    ```python
    def change(arr):
        arr[0] = 1.234

    a = [1, 2, 3, 4, 5]
    change(a)
    print(a)
    ```

    ```python
    # ket qua
    [1.234, 2, 3, 4, 5]
    ```