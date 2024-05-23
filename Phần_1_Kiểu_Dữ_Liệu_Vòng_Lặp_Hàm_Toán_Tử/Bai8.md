# BÀI 8: CẤU TRÚC RẼ NHÁNH TRONG PYTHON

## 1. if và một số ví dụ về if.

- Cú pháp:

    ```python
    if condition
        #code
    ```

- Ví dụ:

    ```python
    if 10 < 20:
        print('tung dep trai')
    ```

    ```python
    # Ket qua
    tung dep trai
    ```

- Có thể kết hợp thêm các toán tử để làm điều kiện cho `if`.

- Ví dụ

    ```python
    n = 60
    if n >= 50 and n <= 100:
        print('true')
    ```

    ```python
    # ket qua
    true
    ```

## else

- `else` được sử dụng trong trường hợp condition bên trong `if` là sai.

- Cú pháp:

    ```python
    if condition:
        # code
    else:
        # code
    ```

- Ví dụ:

    ```python
    n = 30
    if (n % 3 == 0) or (n % 5 == 0):
        print("OK")
        print("ABC")
    else:
        print("Not OK")
        print("DEF")
    ```

    ```python
    # ket qua
    OK
    ABC
    ```

- if thì có thể không cần else, nhưng else bắt buộc phải có if

## elif (else if)

- Từ khoá elif (else if) trong python được sử dụng bến dưới if để kiểm tra thêm điều kiện bổ sung nếu điều kiện bên trên sai. Các điều kiện ở bên trong if và elif nếu đúng thì khối code tương ứng sẽ được thực thi, nếu không có điều kiện nào đúng thì khối lệnh bên trong else được thực thi.

- Cú pháp:

    ```python
    if condition1:
        # code1
    elif condition2:
        # code2
    ...
    elif conditionN:
        # codeN
    else:
        # code else
    ```

- Ví dụ

    ```python
    a, b = 100, 200
    if a < b:
        print(a, 'less than', b)
    elif a == 100:
        print('a = 100')
    else:
        print("FAIL")
    ```

    ```python
    # ket qua
    100 less than 200
    ```

- Chú ý: nếu điều kiện đúng ở câu lệnh `if` nào thì nó thực hiện xong code rùi kết thúc luôn, như ví dụ trên thì do nó đúng điều kiện đầu tiên nên mặc dù câu lệnh `elif` nó thoả mãn nhưng mà nó đã kết thúc ở lệnh `if` ở trên rùi.

## shorthand if và toán tử 3 ngôi

- `shorthand if`: bạn có thể sử dụng câu lệnh if trên một dòng.

- Ví dụ:

    ```python
    a, b = 100, 200
    if a < b: print(a, 'less than', b)
    ```

    ```python
    # ket quan
    100 less than 200
    ```

- Nếu trong `if` có nhiều câu lệnh, bạn có thể đặt dấu `;` giữa các câu lệnh.

    ```python
    a, b = 100, 200
    if a < b: print("a = 100"); print("b = 200")
    ```

    ```python
    # ket qua
    a = 100
    b = 200
    ```

- Toán tử ba ngôi:

    ```python
    variable = statement1 if condition else statement2
    # statement1: true branch
    # statement2: false branch
    # nếu condition đúng thì trả về statement1, sai thì trả về statement2
    ```

- Ví dụ:

    ```python
    a, b = 100, 200
    res = '28tech' if a < b else 'python'
    print(res)
    ```

    ```python
    # ket qua
    28tech
    ```

## if lồng nhau

- Khi điều kiện trong if quá phức tạp, bạn có thể sử dụng  một if lồng nhau (nested if) để kiểm tra từng điều kiện một.

- Ví dụ: kiểm tra n > 50 và chia hết cho ít nhất 1 số trong(3, 5, 7).

    ```python
    # cách 1
    n = 80
    if n > 50 and (n % 3 == 0 or n % 5 == 0 or n % 7 == 0): print("YES")
    else: print("NO")
    ```

    ```python
    # cách 2
    n = 80
    if n > 50:
        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0: print("YES")
        else: print("NO")
    else: print("NO")
    ```

    ```python
    # ket qua
    YES
    ```

- Chú ý trong điều kiện thì chỉ có `or` hết hoặc `and` hết chứ không bao gồm cả `of` và `and`. Tức là `if a and b and c` thì đúng còn `if a and b or c` thì sai. Nhưng if `a and (b or c)` thì lại được