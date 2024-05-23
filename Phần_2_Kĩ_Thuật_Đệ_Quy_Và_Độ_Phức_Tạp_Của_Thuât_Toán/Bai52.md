# BÀI 52: ĐỘ PHỨC TẠP CỦA THUẬT TOÁN

## Đánh giá một thuật toán

- Độ phức tạp về thời gian (time complexity) và độ phức tạp về không gina( space complexity) là 2 yếu tố quyết định một thuật toán có thích hợp để giải quyết một bài toán nào đó hay không.

- Trong đó độ phức tạp về thời gian được quan tâm nhiều hơn khi bạn tham gia vào các contest về lập trình.

- Độ phức tạp thời gian là thời gian mà thuật toán của bạn có thể thực thi, nó là một hàm của input, tức là dựa vào đầu vào ta sẽ tính toán số lượng thao tác mà thuật toán cần thực thi từ đó tính ra được thời gian thực thi của thuật toán.

- Trên các trang chấm online

    - Giới hạn thời gina của bài toán là `1 - 2s` đối với: C/C++.

    - Giới hạn thời gina của bài toán là `4s` đối với: Java/Python.

    - Thông thường 1s các bạn có thể thực hiện được từ 10<sup>8</sup> - 5.10<sup>8</sup> phép toán.

## 1. Tính toán độ phức tạp và kí hiệu là Big O

- BIG O NOTION:

    - Tính toán số lượng phép toán được thực hiện trong mỗi lần thuật toán được khỏi chạy dựa trên input đầu vào của bài toán.

    - Kí hiệu BIG O mô tả trường hợp tệ nhất của thuật toán thông qua một hàm của input đầu vào n.

    - Độ phức tạp của thuật toán càng nhỏ thì thuật toán chạy càng nhanh.

    - Thông qua kí hiệu của BIG O ta có thể mô tả độ phức tạp của thuật toán là O(f(n)).

- Ví dụ mô tả độ phức tạp của thuật toán là O(f(n)): O(n), O(1), O(logn), O(nlogn), O(n^2), O(n!),...

- Chú ý: Trong TH hàm f(n) có chứa hằng só và các bậc khác nhau của n thì ta chọn bậc cao nhất để đại diện cho hàm f(n).

- Ví dụ: O(n^2 + 2n + 3) thay bằng O(n^2)

## Một số ví dụ về phân tích độ phức tạp của thuật toán.

### a) Độ phức tạp của các phép toán và nhập xuất.

- Code sau có độ phức tạp là `O(1)` vì nó thực thi một số phép toán có định.

    ```python
    a, b, c = 100, 200, 300
    sum = a + b + c
    print(sum)
    tich = a * b * c
    print(tich)
    ```

- Chú ý các phép toán như `+`, `-`, `*`, `/`, `%` hay các phép toán gán, so sánh và nhập xuất đều được coi là `O(1)`.

### b) Độ phức tạp của vòng lặp

-  Độ phức tạp của vòng lặp lồng nhau chính là số lượng của vòng lặp nhân với độ phức tạp của code bên trong vòng lặp.

- Code sau đều có độ phức tạp là O(n).

    ```python
    n = 1000
    for i in range(n):
        # O(1) code
    ```

    ```python
    n = 1000
    i = 1
    while i <= n:
        #O(1) code
    ```

    ```python
    n = 1000
    for i in range(3 * n + 2024):
        #O(1) code
    ```

- Code sau sẽ có độ phức tạp là O(n.$\sqrt{n}$).

    ```python
    import math

    def nt(n):
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0: return False
        return n > 1

    for i in range(1, 100):
        if nt(i): print("Nguyen to")
    ```

### c) Độ phức tạp của vòng for lồng nhau

- Trong trường hợp thuật toán của bạn sử dụng vòng lặp lồng nhau, độ phức tạp của thuật toán được tính bằng cách nhân số lần lặp của từng vòng lặp với nhau.

- Code sau có độ phức tạp là O(n*m) hay O(n^2).

    ```python
    n = 10
    m = 100

    for i in range(n):
        for j in range(m):
            # code O(1)
    ```

- Chú ý: bạn càng sử dụng nhiều vòng lặp lồng nhay thì thuật toán sẽ càng lớn và thời gian chạy càng lâu.

## Một vài độ phức tạp thường găp

|Thao tác, thuật toán|Độ phức tạp|
|--|--|
|Sử dụng công thức toán học để tìm ra ngay lời giải|O(1)|
|Tìm kiếm nhị phân|O(logn)|
|Các thao tác của set, map, hàng đợi ưu tiên|O(logn)|
|Kiểm tra số nguyên tố, phân tích thừa số nguyên tố|O(sqrt(n))|
|Đọc n ssoo từ input|O(n)|
|Duyệt qua mảng|O(n)|
|Hàm sort trong thư viện|O(nlogn)|
|Sàng số nguyên tố|O(nloglogn)|
|Duyệt các tập con cỡ k của tập có n phần tử|O(n^k)|
|Duyệt mọi tập con|O(2^n)|
|Duyệt mọi hoán vị|O(n!)|