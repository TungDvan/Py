# BÀI 53: PHẠM VỊ CỦA BIẾN TRONG PYTHON

- Không phải mọi biến đều có thể truy cập ở mọi vị trí trong chương trình mà tại đó một biến có thể truy cập gọi là "scope", được xác định tị nơi mà biến được khai báo.

- Pyhton có 3 phạm vị:

    - Local scope.

    - Global scope.

    - Enclosing scope.

## 1. Local scope.

- Một biến được khai báo trong phạm vị của một hàm được có phạm vi local scope. Khi đó biến sẽ được truy cập từ vị trí nó được khai báo cho tới hết phạm vi của hàm, chừng nào hàm còn được thực hiện thì nó còn tồn tại.

- Biến local sẽ được xoá khỏi bộ nhớ khi hàm chứa nó kết thưc, vì thế việc cố gắng truy cập vào biến local khi hàm kết thúc sẽ xảy ra lỗi.

- Ví dụ:

    ```python
    def prinT():
        n = 100
        print(n)

    if __name__ == "__main__":
        prinT()
        print(n)
    ```

    ```python
    # ket qua
    100
    NameError: name 'n' is not defined
    ```

- Như vậy ta thấy biến n trong ví dụ trên chỉ là biến trong local scope và nó chỉ có giá trị là 100 trong hàm prinT, còn khi ra khỏi hàm prinT thì nó không có giá trị như thế nữa.

## 2. Global scope.

- Biến được khai báo ngoài hàm có tính phạm vi global, biến này có thể truy cập trong toàn bộ chương trình, tính từ vị trí nó được khai báo cho tới cuối file mã nguồn.

- Ví dụ:

    ```python
    x = 2000

    def printNum():
        print(x)

    if __name__ == "__main__":
        print(x)
        printNum()
    ```

    ```python
    # ket qua
    2000
    2000
    ```

- Ví dụ 2:

    ```python
    x = 1234

    def printNum():
        x = 1000
        print(x)

    if __name__ == "__main__":
        printNum() # n local
        print(x)   # n global
    ```

    ```python
    # ket qua
    1000
    1234
    ```

- Khi trong hàm printNum thì n này được khai báo và nó thuộc về phạm vi của local scope này, để nó hiểu n này là biến trong phạm vị global thì ta thêm từ khoá global trước tên biến.

- Ví dụ:

    ```python
    x = 500 # global scope

    def local_scope():
        global x # thong bao cho biet la day la bien global chu khong phai local
        x = 100 # thay doi bien global trong ham thi gia tri cua no cx thay doi theo
        print(x)

    if __name__ == "__main__":
        print(x)
        local_scope()
        print(x)
    ```

    ```python
    # ket qua
    500
    100
    100
    ```

## 3. Enclosing scope.

- Trong nested function, khi bạn khai báo 2 biến có cùng têntrong 2 hàm này thì 2 biến này có phạm vi khác nhau.

- Ví dụ:

    ```python
    def outer():
        x = 2804
        def inner():
            print(x)
        inner()
        print(x)

    if __name__ == "__main__":
        outer()
    ```

    ```python
    # ket qua
    2804
    2804
    ```

- Ví dụ 2 (python tạo 1 biến x có cùng tên trong phạm vi của hàm inner).

    ```python
    def outer():
        x = 2804
        def inner():
            x = 1000
            print(x)
        inner()
        print(x)

    if __name__ == "__main__":
        outer()
    ```

    ```python
    # ket qua
    1000
    2804
    ```

- Ví dụ 3 (sử dụng keyword nonlocal để tránh Python tạo một biến khác cùng tên trong hàm inner).

    ```python
    def outer():
        x = 2804
        def inner():
            nonlocal x
            x = 1000
            print(x)
        inner()
        print(x)

    if __name__ == "__main__":
        outer()
    ```

    ```python
    # ket qua
    1000
    1000
    ```

- Chú ý: trong python thì các biến trong if, for, while, else thì biến đó sẽ được khai báo và bạn có thể sử dụng nó ở ngoài đó

    ```python
    if __name__ == "__main__":
        if True:
            x = 1000
            print(x)
        print(x)
    ```

    ```python
    # ket qua
    1000
    1000
    ```

- Không phải mọi biến đều có thể truy cập ở mọi ví trí trong chương tình, phạm vi của chương trình mà tạo đó một bién có thể truy cập gọi là `scope`, được xác định tạo nơi mà biến được khai báo.

- Python có 3 phạm vi (LEGB rule)

    - Local scope.

    - Enclosing scope.

    - Global scope.

    - Built_In.


