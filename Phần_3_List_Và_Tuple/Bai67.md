# MẢNG CỘNG DỒN (PREFIX SUM)

- Thiết lập công thức tính tổng các phần tử từ vị trí `left` đến vị trí `right`.

- F[i] = F[i - 1] + a[i]

- Chày cối nhưng độ phức tạp là O(N):

    ```python
    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        l, r = map(int, input().split())
        print(sum(arr[l : r + 1])) # O(N)
    ```

- Thuật toán có thể thực hiện nhiều truy vấn với độ phức tạp mỗi truy vấn là O(1).

    ```python
    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        l, r = map(int, input().split())
        F = [0] * n
        F[0] = arr[0]
        for i in range(1, n):
            F[i] = F[i - 1] + arr[i]
        print(F[r] - F[l - 1])
    ```

- Nếu `l = 0` thì là `F(r)`