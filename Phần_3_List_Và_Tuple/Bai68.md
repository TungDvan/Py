# BÀI 68: KỸ THUẬT CỬA SỔ TRƯỢT (SLIDING WINDOW)

- Chày cối `O(n)`:

    ```python
    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        for i in range(0, n - k + 1):
            # chi so bat dau cua day con
            tong = 0
            for j in range(i, i + k): tong += arr[j]
            print(tong)
    ```

- Tối ưu `O(1)`:

    ```python
    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        tong = sum(arr[:k])
        print(tong, end = ' ')
        for i in range(0, n - k + 1):
            tong = tong - arr[i - 1] + arr[i + k - 1]
            print(tong, end = ' ')
    ```