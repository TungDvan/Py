# BÀI 71: UNPACKING TRONG PYTHON

## Giới thiệu về Unpacking.

- Unpacking là một kĩ thuật giúp tác một tuple, list, iterable,... thành các biến rời rạc.

- Khi unpacking chú ý số lượng phần tử ở bên trái dấu bằng phải bằng số lượng phần tử của iterable bên phải dấu bằng.

    ```python
    # vi du
    a = [1, 2, 3]
    x, y, z = a
    print(x, y, z)
    ```

- Ví dụ unpacking với `list`:

    ```python
    data = ["tung", "mousefuhlen@gmail.com", 2022]
    name, email, birth = data
    print(name, email, birth)
    ```

    ```python
    # ket qua
    tung mousefuhlen@gmail.com 2022
    ```

- Ví dụ unpacking với `tuple`: Trong TH bạn chỉ muốn lấy ra các phần tử cần thiết, có thể dùng biến có thên _ (gạch dưới) để bỏ đi những biến không cần thiết.

    ```python
    data = ("CR7", "ManUTD", 1985, "BDN")
    name, club, _, _ = data
    print(name, club)
    ```

    ```python
    # ket qua
    CR7 ManUTD
    ```

- Unpacking với `string`:

    ```python
    s = "CR7"
    a, b, c = s
    print(a, b, c)
    ```

    ```python
    C R 7
    ```

- Unpacking với `range`:

    ```python
    a, b, c = range(0, 5, 2)
    print(a, b, c)
    ```

    ```python
    # ket qua
    0 2 4
    ```

- Unpacking với `set`: đối với set việc unpacking có thể dẫn tới một thứ tự bất kì vì set vốn không có thứ tự như những interable ở trên

    ```python
    my_set = {'28tech', 'java', 'python'}
    a, b, c = my_set
    print(a, b, c )
    ```

    ```python
    # ket qua
    28tech java python
    ```

- Unpacking với vòng `for`: 

    ```python
    a = [['A', 65], ['B', 66], ['C', 67]]
    for kitu, ma in a:
        print(kitu, '->', ma)
    ```

    ```python
    # ket qua
    A -> 65
    B -> 66
    C -> 67
    ```

- Unpacking với toán tử `*`: Trong Th iterable bên phải dấu bằng có quá nhiều phần tử, trong khi đó bạn chỉ muốn lấy ra một vài phần tử, khi đó bạn có thể sử ụng toán tử `*`:

    ```python
    a = [1, 3, 4, 5, 23, 1, 1, 33]
    x, y, *z = a
    x1, *y1, z1 = a
    print(x, y, z, sep = '\n')
    print(x1, y1, z1, sep = '\n') 
    ```

    ```python
    #ket qua
    1
    3
    [4, 5, 23, 1, 1, 33]
    1
    [3, 4, 5, 23, 1, 1]
    33
    ```