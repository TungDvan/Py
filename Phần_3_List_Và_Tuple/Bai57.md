# BÀI 57: HÀM LAMBDA

- Lambda là một trong những tính năng cực kì mạnh mẽ, quan trọng và thú vị trong ngôn ngữ lập trình Python, tuy nhiên kiến thức này thường bị hiểu sai hoặc hiểu thiếu.

## 1. Lambda là gì?

- Lambda là một cách đơn giản để định nghĩa hàm trong Python. Lambda thường được gọi dưới cái tên toán tử lambda hoặc hàm lambda.

- `Lambda` là một cách để định nghĩa hàm vô danh (`anonymous`), một hàm mà không cần tên hàm. Nó được sử dụng khi bạn cần xây dựng những hàm chỉ **bao gồm 1 câu lệnh**, khi đó việc sử dụng `keyword def` để định nghĩa hàm là quá thừa thãi và dài dòng.

- Cú pháp: `lambda parameters : expression`.

- Ví dụ:

    ```python
    def func(n):
        return 2 * n

    print(func(10))
    print(func(20))
    ```

    ```python
    # ket qua
    20
    40
    ```

- Khi sử dụng lambda:

    ```python
    func = lambda x: x * 2

    print(func(90))
    print(func(19))
    ```

    ```python
    # ket qua
    180
    38
    ```

    ```python
    xinchao = lambda: print("hello ban nho")

    xinchao()
    xinchao()
    ```

    ```python
    # ket qua
    hello ban nho
    hello ban nho
    ```

## 2. Các tính chất của lambda.

- Lambda không thể chứa các câu lệnh: ví dụ như `return`, `assest`, `pass`,...

- Lambda chỉ chứa một biểu thức duy nhất.

- `IIEF`: Inmediately Invoked Fuction Expression: Biểu thức lambda có thể được gọi ngay lập tức.

    ```python
    res = (lambda x: x ** 2)(10)
    print(res)
    ```

    ```python
    # ket qua
    100
    ```

## 3. Lambda với nhiều tham số.

- Bạn có thể gửi bao nhiêu tham số tuỳ ý, chỉ cần phân cách giữa các tham số bằng dấu phẩy.

    ```python
    sum = lambda x, y, z: x + y + z

    print(sum(10, 20, 30))

    print((lambda x, y, x: x + y - z)(10, 20, 30))
    ```

    ```python
    # ket qua
    60
    0
    ```

## 4. Truyền đối số cho Lambda.

- `Positional argument`:

    ```python
    sum = lambda x, y, z: x + y + z
    print(sum(10, 20, 30))
    ```

    ```python
    # ket qua
    60
    ```

- `Keyword argument`:

    ```python
    sum = lambda x, y, z: x + y + z
    print(sum(10, z = 20, y = 30))
    ```

    ```python
    # ket qua
    60
    ```

- `Default argument`:

    ```python
    sum = lambda x, y = 20, z = 30: x + y + z
    print(sum(10))
    ```

    ```python
    # ket qua
    60
    ```

## 5. Lambda và map()

- Hàm map() trong python có 2 đối số là một hàm và một list, map áp dụng hàm này với các phần tử trong list.

    ```python
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x: x**2, a))
    print(b)
    ```

    ```python
    # ket qua
    [1, 4, 9, 16, 25]
    ```

## 6. Lambda và filter()

- Hmaf filter() tương tự như hàm map, khi apply các hàm trong filter với từng phần tử trong list mà gái trị của hàm trả về true thì filter lọc ra các phần tử này

    ```python
    a = [1, 2, -3, -4, 5]
    b = list(filter(lambda x: x > 0, a))
    print(b)
    ```

    ```python
    # ket qua
    [1, 2, 5]
    ```

## 7. if else và lambda

- Bạn có thể kết hợp if else trong lambda.

    ```python
    findMax = lambda x, y: x if x > y else y
    print(findMax(100, 200))
    ```

    ```python
    # python
    200
    ```