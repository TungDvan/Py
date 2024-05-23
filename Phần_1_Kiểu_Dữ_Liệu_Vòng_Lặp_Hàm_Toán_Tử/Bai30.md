# BÀI 30: PHÂN TÍCH THỪA SỐ NGUYÊN TỐ

- VD: 30 = 2 x 3 x 5

- VD: 60 = 2 x 2 x 3 x 5

    ```python
    def phan_tich(n):
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                while n % i == 0:
                    print(i, end = " ")
                    n //= i
        if n != 1: print(n)
    ```
    
- Từ phân tích thừa số nguyên tố suy ra số ước của nó.

