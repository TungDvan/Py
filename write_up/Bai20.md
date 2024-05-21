# BÀI 20: VÒNG LẶP WHILE VÀ CÁC BÀI TOÁN ÁP DỤNG

## Vòng lặp while

- `while` được sử dụng khi bạn muốn thực hiện một tác vụ vô thời hạn, cho đến khi một điều kiện cụ thể được đáp ứng. Đây là một vòng lặp được kiểm soát theo điều kiện và thường được sử dụng khi chưa biết một số lượng vòng lặp.

- Cú pháp:

    ```python
    while condition:
        # code when condition is True
    else: 
        # code while condition is False
    ```

- Ví dụ:

    ```python
    n = 1
    while n <= 5:
        print("vong lap tuong ung khi n bang", n)
        n += 1
    else: print("vong lap ket thuc khi n =", n)
    ```

    ```python
    # ket qua
    vong lap tuong ung khi n bang 1
    vong lap tuong ung khi n bang 2
    vong lap tuong ung khi n bang 3
    vong lap tuong ung khi n bang 4
    vong lap tuong ung khi n bang 5
    vong lap ket thuc khi n = 6
    ```

- `continue` và `break` cũng được sử dụng trong `while`, trong đó `continue` là tiếp tục vòng lặp mới, còn `break` là thoát khỏi vòng lặp. 