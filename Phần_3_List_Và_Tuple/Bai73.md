# BÀI 73: MAP VÀ FILTER

## 1. Map()

- `Map()` là một hàm trong python có chức năng apply một hàm có sẵn cho mọi phần tử trong iterable (list, tuple, str...)

- Cú pháp: map(fuction, iterable)

    - function: hàm này sẽ được sử dụng để apply với các phần tử trong iterable.

    - iterable: các iterable ví dụ như list, tuple, str,...

    - giá trị trả về: map trả về một đối tượng thuộc lớp map. Các bạn nên ép sang list để sử dụng. 

- Ví dụ:

    ```python
    # binh thuong
    a = [-100, 200, -29, -900]
    a = [abs(x) for x in a]
    print(a)
    ```

    ```python
    # ket qua
    [100, 200, 29, 900]
    ```

    ```python
    # dung map
    a = [-100, 200, -29, -900]
    a = list(map(abs, a))
    print(a)
    ```

    ```python
    # ket qua
    [100, 200, 29, 900]
    ```

- Ví dụ về map:

    ```python
    s = 'tung dep trai'
    b = list(map(ord, s))
    print(b)
    ```

    ```python
    [116, 117, 110, 103, 32, 100, 101, 112, 32, 116, 114, 97, 105]
    ```

- Trong TH hàm apply trong map ngắn gọn thì bạn có thể thay thế bằng lamda.

    ```python
    a = [1, 2, 3, 4]
    c = list(map(lambda x: x * x, a))
    print(c)
    ```


    ```python
    # ket qua
    [1, 4, 9, 16]
    ```

- Áp dụng map với nhiều iterable sử dụng trong lambda:

    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = list(map(lambda x, y: x + y, a, b))
    print(c)
    ```

    ```python
    #ket qua
    [5, 7, 9]
    ```

## 2. Filter()

- Hàm filter() được sử dụng để trích xuất các phần tử trong một iteravble khi apply một hàm nào đó với phần tử đó mà hàm trả về giá trị là True.

- Cú pháp: filter(function, iterable)

    - function: hàm sẽ được sử dụng để apply với các phần tử trong iterable.

    - iterable: các iterable ví dụ như list, tuple, str,...

    - giá trị trả về; filter trả về một đối tượng của lớp filter, bạn nên ép nó sang list hoặc tuple.

- Ví dụ:

    ```python
    def even(n):
        return n % 2 == 0

    a = [1, 2, 3, 4, 5, 6]
    b = list(filter(even, a))
    print(b)
    ```

    ```python
    # ket qua
    [2, 4, 6]
    ```

    ```python
    a = [1, 2, 3, 4, 5]
    b = list(filter(lambda x: x % 2 == 0), a)
    print(b)
    ```

    ```python
    # ket qua
    [2, 4]
    ```