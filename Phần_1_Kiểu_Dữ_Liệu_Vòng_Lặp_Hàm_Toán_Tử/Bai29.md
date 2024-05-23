# KIỂM TRA SỐ NGUYÊN TỐ

- Số nguyên tố: là một số nguyên dương, và chỉ có 2 ước là 1 và chính nó: 2, 3, ...

- Chày cối:

    ```python
    def prime(n):
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0: cnt += 1
        if cnt == 2: return True
        else: return False
    ```

- Smart:

    ```python
    import math

    def prime(n):
        cnt = 0
        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                cnt += 1
                if i != n // i: cnt += 1
        if cnt == 2: return True
        else: return False
    ```

- ***Smart pro vip***:

    ```python
    import math

    def prime(n):
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0: return False
        return n > 1
    ```