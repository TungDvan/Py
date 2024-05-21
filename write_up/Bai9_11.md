# VÒNG LẶP FOR TRONG PYTHON | HÀM RANGE TRONG PYTHON

## Vòng lặp for và hàm range():

### Vòng lặp for:

- Trong ngôn ngữ lập trình Python có chút khác so với các ngôn ngữ lập trình như `C`/`C++`, `Java`, ect.

- Thay vì duyệt qua các giá trị số thì python sẽ lặp trên csac `iterable` (list, tuple, string, set...). Thứ tự duyệt sẽ theo thứ tự xuất hiện trong `iterable`. Để thực hiện vòng lặp for ta sử dụng `built-in function` là `range()`.

- Cú pháp:

    ```python
    for var in iterable:
        statement
        statement
        ...
    else:
        statement
        ...
    # var: it takes items from iterable one by one
    # iterable: It's a collection ò objects (like a list, tuple etc.)
    ```

### Hàm range()

- Hàm range() sẽ sinh ra một dãy số và bạn có thể sử dụng vòng for để duyệt qua từng số trong dãy được sinh ra.

- Cú pháp:

    ```python
    range(start, stop, step)
    # start: giá trị bắt đầu của dãy số (mặc định là 0).
    # stop: giá trị cuối cùng của dãy số (cận này không được lấy).
    # step: bước nhảy của dãy số (mặc định là 1).
    ```

- Ví dụ:
    
    ```python
    a = range(1, 10, 1)
    for i in a:
        print(i, end = ' ')
    ```

    ```python
    # ket qua
    1 2 3 4 5 6 7 8 9
    ```

- Ví dụ: Duyệt từ 1 đến 50:

    ```python
    for i in range(1, 51):
        print(i, end = ' ')
    ```

    ```python
    # ket qua
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
    ```

- Ví dụ: duyệt từ 0 đến 51:

    ```python
    for i in range(51):
        print(i, end = " ")
    ```

    ```python
    # ket qua
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
    ```

- Giải thích vòng for sau:

    ```python
    for i in range(5):
        print(i)
        i += 5
        print(i, "Ket thuc vong lap")
    ```

    ```python
    # ket qua
    0
    5 Ket thuc vong lap
    1
    6 Ket thuc vong lap
    2
    7 Ket thuc vong lap
    3
    8 Ket thuc vong lap
    4
    9 Ket thuc vong lap
    ```

    - Ban đầu chương trình sẽ tạo ra một range là `[0, 1, 2, 3, 4]`.

    - Tiếp theo chương trình sẽ gán phần tử đầu tiên của `range` cho `i` = 0. Xong rùi in ra, xong rùi `i` = 0 + 5 = 5. Ở vòng lặp thứ 2 lại gán lại phần tử thứ 2 của `range` cho `i`, lúc này `i` = 2 (không còn là 5 như trước). Tiếp tục như thế cho đến cuối vòng lặp.

    - Vậy tức là dù bạn có thay đổi giá trị của i trong vòng for như thế nào đi chăng nữa thì bắt đầu vòng lặp mới thì giá trị i đó sẽ được tạo lại.

### Câu lệnh break và continue

#### Câu lệnh break

- Câu lệnh `break` được sử dụng để kết thúc vòng lặp ngay lập tức, vòng lặp `for` sẽ kết thúc ngay tại thời điểm gặp câu lệnh `break` và tiếp tục các câu lệnh bên dưới vòng `for`. Thông thường thì câu lệnh `break` sẽ đi kèm theo một điều kiện kích hoạt.

- Ví dụ:

    ```python
    for i in range(5):
        print(i, end = ' ')
        if i == 3: break
        print('hello dchi')
    print("ket thuc")
    ```

    ```python
    # ket qua
    0 hello dchi
    1 hello dchi
    2 hello dchi
    3 ket thuc  
    ```

#### Câu lệnh continue

- Câu lệnh continue được dùng để bỏ qua lần lặp hiện tại và quay trở lại lun vòng lặp tiếp theo. Các câu lệnh bên dưới continue ở trong vòng lặp sẽ được bỏ qua.

- Ví dụ:

    ```python
    for i in range(5):
        print('tung dep trai')
        continue
        print('tung xau trai')
    ```

    ```python
    # ket qua
    tung dep trai
    tung dep trai
    tung dep trai
    tung dep trai
    tung dep trai
    ```

### Vòng for lồng nhau

- Vòng for lồng nhau (nested loop) xuất hiện khi một câu lệnh bên trong vòng for này lại là một còng for khác. Để hiểu được cách hoạt động của vòng for các bạn chỉ cần nhớ rằng mỗi vòng lặp của vòng for bên ngoài thì toàn bộ vòng for con bên trong sẽ được thực hiện.

- Ví dụ:

    ```python
    for i in range(3):
        print('Vong for ben ngoai')
        for j in range(2):
            print('Vong for ben trong', end = ' ')
            print(i, j)
    ```

    ```python
    # ket qua
    Vong for ben ngoai
    Vong for ben trong 0 0
    Vong for ben trong 0 1
    Vong for ben ngoai
    Vong for ben trong 1 0
    Vong for ben trong 1 1
    Vong for ben ngoai
    Vong for ben trong 2 0
    Vong for ben trong 2 1
    ```