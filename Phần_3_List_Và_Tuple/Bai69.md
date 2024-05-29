# BÀI 69: SÀNG SỐ NGUYÊN TỐ ERATOSTHENES

- Hàm kiểm tra nguyên tố check như bthg: O(`n*căn(n)`).

- Sàng số nguyên tố: O(`n*log(logn)`).

- Sàng từ `0` đến `10^6`.

    ```python
    # B1: Coi tat ca cac so tu 0 den n la so nguyen to
    # B2: Boi cua mot so nguyen to se khong phai so nguyen to
    # duyet tu 2 den can(n)

    import math

    prime = [True] * (10 ** 6 + 1)

    def sieve():
        n = 10 ** 6 + 1
        prime[0], prime[1] = False, False
        for i in range(2, math.isqrt(n) + 1):
            if prime[i]:
                for j in range(i * i, n, i): 
                    prime[j] = False

    if __name__ == "__main__":
        sieve()
        check = int(input())
        if (prime[check]): print("YES")
        else: print("NO")
    ```