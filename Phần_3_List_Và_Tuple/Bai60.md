# BÀI 60: KỸ THUẬT MẢNG ĐÁNH DẤU

- Giá trị khác nhau trong mảng: Tìm số lượng phần tử khác nhau, liệt kê.

- Những bài toán liên quan đến tần suất.

- Ví dụ: cho mảnh A có N phần tử, đếm tần suất mỗi giá trị trong mảng.

    ```python
    #input
    1 2 3 4 1 3 2
    #output
    1: 2
    2: 2 
    3: 2
    3: 1 
    ```

- Ý tưởng: Sử dụng chỉ số của mảng để đánh dấu 1 giá trị tương ứng.

- Chỉ áp dụng với những bài số dương từ `0` đến `10^7` và là số nguyên.

    ```python
    import math

    def nt(x):
        for i in range(2, math.isqrt(x) + 1):
            if x % i == 0: return False
        return x > 1

    if __name__ == "__main__":
        n = int(input())
        a = list(map(int, input().split()))
        count = [0] * 1000001
        for i in a:
            count[i] += 1
        for i in a:
            print(i, ": ", count[i], sep = '')
        print("In theo thu tu.")
        for i in a:
            if count[i] != 0:
                print(i, ": ", count[i], sep = '')
                count[i] = 0
    ```

- Với bài toán tìm số phần tử khác nhau thì cx có thể sử dụng mảng đánh dấu.

    ```python
    
    ```