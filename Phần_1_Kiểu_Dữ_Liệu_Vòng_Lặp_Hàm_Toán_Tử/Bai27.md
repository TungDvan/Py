# BÀI 27: HÀM TRONG PYTHON

- Hàm giúp các lập trình viên có thể sử dụng lại code của mình (code reuse), chúng cho phép bạn định nghĩa một khối lệnh và có thể thực hiện lại nhiều lần trong một chương trình.

- Python cũng cung cấp các hàm có sẵn (built-in function) như print(), max(), len(), type()... Giờ đây bạn có thể tự xây dựng những hàm của riêng mình.

## Xây dựng hàm

- Để xây dựng hàm ta sử dụng từ khoá `def`, trước khi xây dựng hàm cần xác định tham số (giá trị mà bạn truyền cho hàm), câu lệnh return nếu mong muấn hàm trả về một giá trị nào đó.

- Hàm chỉ được chạy khi nó được goi (function call).

- Cú pháp:

    ```python
    def function_name(parameter):
        #code
        return value
    ```

- Ví dụ:

    ```python
    def tong(a, b):
        res = a + b
        return res

    m, n = 10, 20
    print(tong(10, 20))
    ```

    ```python
    # ket qua
    30
    ```

- Khi gọi hàm `a, b` là `tham số`; còn `10, 20` là `đối số`. Chương trình sẽ gán các tham số chính thức cho các tham số hình thức (tức là a = 10, b = 20). Sau đó chương trình thực thi trên tham số hình thức, sau đó thực hiện tính `res`. 

- Ví dụ:

    ```python
    def xin_chao(name1, name2, name3):
        print("xin chao", name1, name2, name3)

    xin_chao('Tung', 'Phuong', 'Loc')
    ```

    ```python
    # ket qua
    xin chao Tung Phuong Loc
    ```

- Ta thấy hàm trên không có return về giá trị, nhưng nó luôn trả về một giá trị đó là `None`.

    ```python
    def xin_chao(name1, name2, name3):
        print("xin chao", name1, name2, name3)

    xin_chao('Tung', 'Phuong', 'Loc')
    print(xin_chao)
    ```

    ```python
    # ket qua
    xin chao Tung Phuong Loc
    None
    ```

- Ví dụ 2:

    ```python
    def tong(a, b):
        a = a + b 

    if __name__ == '__main__':
        x, y, = map(int, input().split())
        print(tong(x, y))
    ```

    ```python
    # input
    2 3
    # output
    None
    ```

- Thường trong python sẽ sử dựng cú pháp như sau để đánh dấu đâu là hàm main:

    ```python
    if __name__ == '__main__':
        # code
    ```

- Ví dụ:

    ```python
    def tong(a, b):
        res = a + b
        return res

    if __name__ == '__main__':
        x, y, = map(int, input().split())
        print(tong(x, y))
    ```

    ```python
    # input
    2 3
    # output
    5
    ```

- Chú ý: hàm không khiến chúng ta có thể thay đổi giá trị của tham số chính thức.

    ```python
    def change_1(n):
        n *= 2

    def change_2(n):
        return n - 100

    if __name__ == '__main__':
        a = 200
        change_1(a)
        print(a)
        print(change_2(a))
        print(a)
    ```

    ```python
    200
    100
    200
    ```

## Keyword argument

- Bạn có thể sử dụng cú pháp parameter_name = value khi gọi hàm để chỉ định giá trị được gán cho các tham số, khi đó thứ tự bạn gọi hàm không còn quan trọng nữa.

- Ví dụ:

    ```python
    def xin_chao(name1, name2, name3):
        print("Xin chao", name1, name2, name3)

    xin_chao("Bach", "Hai", "Phuong")
    xin_chao(name2 = "Hai", name3 = "Phuong", name1 = "Bach")
    # dòng 5 là keyword argument
    # dòng 4 là positional argument
    ```

    ```python
    Xin chao Bach Hai Phuong
    Xin chao Bach Hai Phuong
    ```

## Default argument

- Bạn có thể chỉ định các giá trị mặc định cho các đối số khi xây dựng một hàm. Giá trị mặc định được sử dụng nếu hàm được gọi mà không có đối số tương ứng.

- Ví dụ:

    ```python
    def infor(name, cha = 'dep trai nhat vu tru'):
        print(name, cha)

    infor("Tung")

    infor("Tung", "DEP TRAI NHAT VIET NAM")
    ```

    ```python
    # ket qua
    Tung dep trai nhat vu tru  
    Tung DEP TRAI NHAT VIET NAM
    ```

- Ta thấy lời gọi hàm đầu tiên ta chỉ có truyền tham số `name` và không có tham số `cha` ở sau thì mặc định sẽ là `dep trai nhat vu tru`.

- Khi xây dựng hàm cần quan tâm

    ```python
    # Hàm có những đối số gì? => Thông tin bạn gửi cho hàm
    # Hàm của bạn trả về giá trị gì, cả kiểu dữ liệu là gì?
    # Kiểm tra đúng sai? Trả về True hoặc False
    ```

- Ngoài ra hàm trong python có thể trả về nhiều giá trị

- Ví dụ:

    ```python
    def tong_hieu(a, b):
        tong = a + b
        hieu = a - b
        return tong, hieu

    if __name__ == "__main__":
        a = 100
        b = 200
        c, d = tong_hieu(a, b)
        print(c, d, sep = '\n')
        print(tong_hieu(a, b))
    ```

    ```python
    # ket qua
    300
    -100
    (300, -100)
    ```

- Hàm mà gặp câu lệnh `return` thì sẽ trả về gay lập tức.