# BÀI 6: NHẬP DỮ LIỆU TỪ BÀN PHÍM TRONG PYTHON BẰNG HÀM INPUT VÀ MAP

## Nhập dữ liệu với hàm input   

* Cú pháp: `input(prompt)`

    * Trong đó `prompt` là thứ sẽ hiện ra chương trình trước khi nhập

* Giá trị trả về: input() trả về xâu kí tự ở kiểu str, các bạn cần chú ý ép kiểu dữ liệu tương ứng của biến trong đề bài.

* Ví dụ:
    ```python
    s = input('xin nhap du lieu tu ban phim: ')
    print('xau vua nhap la: ', s)
    ```

    * input: Tung dep trai co mot khong hai
    * output:
        ```
        xin nhap du lieu tu ban phim: Tung dep trai co mot khong hai
        xau vua nhap la:  Tung dep trai co mot khong hai
        ```

* chú ý hàm `input` sẽ đọc toàn bộ 1 dòng nhập vào và lưu ở dưới dạng `str`

* Nếu muốn nhập một số nguyên thì chúng ta cần phải ép kiểu, bơi vì input trả về kiểu dữ liệu str:
    * Ví dụ:
        ```python
        a = input('nhap mot so nguyen: ')
        print(a, type(a))
        a = int(a)
        print(a, type(a))
        ```
        * Input: 23
        * Output:

        ```
        23 <class 'str'>
        23 <class 'int'>
        ```

    * Chúng ta có thể nhập nhanh như sau:
        ```python
        a = int(input('Nhap mot so nguyen: '))
        print(a, type(a))
        ```
        * Input: 23
        * Output:
        ```
        23 <class 'int'>
        ```
* Tương tự như thế nếu ta muốn ép kiểu sang `float` hay `int`

# Nhập nhiều số trên cùng một dòng

* Tư tưởng: tách chuỗi ra, ép kiểu của tùng giá trị trong chuỗi đó thành kiểu mình muốn

* Ví dụ: input `100 200 300`
    * tách chuỗi thành `100` `200` `300` (đang ở dạng string)
    * Ép kiểu sang số nguyên: `100`, `200`, `300`

* Các công đoạn trong python sẽ như sau (nếu muốn hiểu thì đọc qua, còn không thì next luôn đến ý tiếp theo)

    * Bước 1: Nhập

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        ```

    * Bước 2: Tách ra

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        # B2: Tach ca so ra
        b = a.split()
        # In thu ra xem b la gi
        print(b)
        ```
        * Input: `200 100 300`
        * Output:
            ```
            Nhap 3 so: 200 100 300
            ['200', '100', '300']
            ```

    * Bước 3: Sử dụng map để ép các phần tử trong list sang kiểu dữ liệu mong muốn

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        # B2: Tach ca so ra
        b = a.split()
        # B3: Su dung map de ep cac phan tu trong lít => kieu du lieu mong muon
        x, y, z = map(int, b)
        # In thu ra xem x, y, z la gi
        print(x + y + z)
        ```

        * Input: `100 200 300`
        * Output:
            ```
            Nhap 3 so: 100 200 300
            600
            ```

        * Chú ý, nếu ở bước 3 chúng ta không có dòng `x, y, z = map(int, b)` mà thay vào đó là `x, y, z = b` thì lúc này x, y, z vẫn sẽ nhận các giá trị và các `string` lần lượt là `'100'` `'200'` `'300'` và phép cộng x + y + z là phép cộng `string` nên kết quả sẽ là `100200300`

            ```python
            # B1: Nhap
            a = input('Nhap 3 so: ')
            # B2: Tach ca so ra
            b = a.split()
            # B3: 
            x, y, z = b
            # In thu ra xem x, y, z la gi
            print(x + y + z)
            ```
            * Input: `100 200 300`
            * Output:
                ```
                Nhap 3 so: 100 200 300
                10020030
                ```

* Làm gọn lại các bước nhập trên 1 dòng sau 3 bước ở trên:

    ```python
    x, y, z = map(int, input('Nhap 3 so nguyen duong: ').split())
    print(x, type(x), y, type(y), z, type(z))
    ```
    * Input: `100 200 300`
    * Output:
        ```
        Nhap 3 so nguyen duong: 100 200 300
        100 <class 'int'> 200 <class 'int'> 300 <class 'int'> 
        ```
