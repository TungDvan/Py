# BÀI 54: LÝ THUYẾT VỀ LIST TRONG PYTHON.

- List tương tự như cấu trúc dữ liệu mảng ở trong các ngôn ngữ lập trình khác nhưng có phần linh hoạt và mạnh mẽ hơn.

- Các tính chất của list: 

    - `Lists are ordered`: Các phần tử trong list là có thứ tự.

    - `Accessed by index`: Truy cập các phần tử trong list thông qua chỉ số.

    - `Lists can contain any sort of object`: List có thể chứa các object thuộc kiểu dữ liệu khác nhau như `int`, `str`, `float`, thậm chí là một `list` khác.

    - `Lists are changeable (mutable)`: Các phần tử trong list có thể thay đổi giá trị, các thao tác thêm, xoá các phần tử cũng được hỗ trợ.

## 1. Tạo list.

- Có nhiều cách để tạo một list, đơn giản nhất là tạo một list bằng cách đưa các giá trị của list vào bên trong dấu đóng mở ngoặc vuông, các giá trị phân nhau bởi dấu phẩy.

- Ví dụ:

    ```python
    # list cac so nguyen
    a = [1, 2, 3, 4]

    # list cac xau ki tu
    b = ['hello', 'ban', 'nho']

    # list cac so nguyen, xau ki tu, so phuc
    c = [1, 2, 3, 'tungdep trai', 3 + 5j]

    # list rong
    d = [] 

    print(a)
    print(b)
    print(c)
    print(d)
    print(type(a), type(b), type(c), type(d))
    ```

    ```python
    [1, 2, 3, 4]
    ['hello', 'ban', 'nho']
    [1, 2, 3, 'tungdep trai', (3+5j)]        
    []
    <class 'list'> <class 'list'> <class 'list'> <class 'list'>
    ```

## 2. List constructor.

- Bạn có thể sử dụng hàm khởi tạo list() để biến đổi các object khác thành list.

- Ví dụ:

    ```python
    s = 'tung dep'

    a = list(s)
    print(a)
    ```

    ```python
    # ket qua
    ['t', 'u', 'n', 'g', ' ', 'd', 'e', 'p']
    ```

- Ta thấy `s = 'tung dep'` là một `iterable` (là những cái có thể duyệt qua được, có thể là `range(100)`), nhưng nếu gõ `list(100)` thì không được do 100 không phỉa một `iterable` (do không thể duyệt qua được).

## 3. Hàm len().

- Để biết số lượng phần tử trong lits ta sử dụng hàm `len()`.

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 5, 6]
    print(len(a))
    ```

    ```python
    6
    ```

## 4. Truy cập phần tử thông qua chỉ số.

- Chỉ số các phần tử trong list được đánh từ số 0 tính từ trái qua phải, ngoài ra Python list hỗ trợ cả chỉ số âm.

- Chú ý: Nếu duyệt một chỉ số không hợp lệ se gây ra lỗi `IndexError`.

    |Index|0|1|2|3|4|
    |--|--|--|--|--|--|
    |a|2|7|6|3|1|
    |Negative index|-5|-4|-3|-2|-1|

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 5]
    print(a[0]) # O(1)
    print(a[-1])
    # 5: 0 - 4
    # -1 -> -5

    print(a[10])
    ```

    ```python
    # ket qua
    1
    5
    IndexError: list index out of range
    ```

# 5. Duyệt list.

- Duyệt thông qua chỉ số:

    ```python
    a = [1, 2, 3, 4, 'python', '28tech']

    for i in range(len(a)):
        print(a[i], end = " ")

    print()

    for i in range(-1, len(a) * -1 - 1, -1):
    # for i in range (len(a) * -1 - 1, 0):
        print(a[i], end = ' ')
    ```

    ```python
    1 2 3 4 python 28tech 
    28tech python 4 3 2 1
    ```

- Duyệt bằng for each:

    ```python
    a = [1, 2, 3, 4, '28tech']

    for i in a: # giong nhu range()
        print(i, end = ' ')
    ```

    ```python
    1 2 3 4 28tech
    ```

## 6. Thay đổi giá trị phần tử.

- Bạn có thể thay đổi giá trị phần tử của list thông qua chỉ số tương ứng của nó.

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 'python']
    a[1] = 'tung dep trai'
    a[-1] = 'C++'
    print(a)
    ```

    ```python
    # ket qua
    [1, 'tung dep trai', 3, 4, 'C++']
    ```

## 7. Thêm một phần tử vào trong list.

- Để thêm một phần tử vào list bạn có thể sử dụng hàm `append()`, hàm này sẽ thêm mới phần tử vào `cuối` list.

- Ví dụ:

    ```python
    a = [1, 'python', '28tech']

    a.append('C++')
    a.append('100')
    print(a)
    ```

    ```python
    # ket qua
    [1, 'python', '28tech', 'C++', '100']
    ```

- Nếu bạn muốn thêm 1 phần tử voà 1 vị trí bất kì thì bạn sử dụng `insert()`

- Ví dụ:

    ```python
    tung = ['apple', 'python', '28tech']

    tung.insert(1, 'facebook')
    print(a)
    ```

    ```python
    # ket qua
    ['apple', 'facebook', 'python', '28tech']
    ```

- Nếu `insert()` mà chúng ta thêm vào một ví trí nằm ngoài list (lớn hơn kích thước của list) thì nó sẽ thêm vào cuối list.

- Ví dụ:

    ```python
    a = [1, 2, 3]
    a.insert(99, 10)
    print(a)

    b = [4, 5, 6, 7]
    b.insert(-2, 1000)
    print(b)

    c = [8, 9, 10, 11]
    c.insert(-99, 1.45)
    print(c)
    ```

    ```python
    # ket qua
    [1, 2, 3, 10]
    [4, 5, 1000, 6, 7]
    [1.45, 8, 9, 10, 11] 
    ```

## 8. Xoá phần tử khỏi list.

- Xoá phần tử khỏi list thông qua chỉ số bằng hàm `pop()`. Nếu không chỉ rõ chỉ số cho hàm `pop`, hàm này sẽ xoá phần tử cuối cùng.

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 5, 6]

    a.pop(3) # xoa phan tu a[3] = 4
    print(a)
    a.pop() # xoa phan tu cuoi cung (5)
    print(a)
    ```

    ```python
    # ket qua
    [1, 2, 3, 5, 6]
    [1, 2, 3, 5]
    ```

- Hàm `pop` sẽ trả về phần tử mà bạn xoá khỏi list, bạn cũng có thể sử dụng hàm `del` nếu không muốn lấy phần tử bị xoá đó.

- Ví dụ:

    ```python
    a = [1, 5, 10, 15, 20]
    del a[1]
    print(a)
    ```

    ```python
    # ket qua
    [1, 10, 14, 20]
    ```

- Xoá phần tử thông qua giá trị bằng hàm `remove()`, nếu trong `list` có nhiều phần tử giống nhau bạn cần xoá thì hàm này chỉ xoá đi phần tử đầu tiên.

- Nếu muốn dùng `remove` bạn phải đảm bảo giá trị bạn xáo có tồn tại trong `list`. Xoá phần tử không tồn tại trong `list` bằng `remove()` sẽ gây ra lỗi.

- Ví dụ:

    ```python
    a = [1, 2, 4, 2, 2, 6, 7]

    a.remove(2)
    print(a)
    a.remove(1000)
    ```

    ```python
    # ket qua
    [1, 4, 2, 2, 6, 7]
    ValueError: list.remove(x): x not in list
    ```

## 9. Sao chép list

- Sao chép lits có thể giúp bạn nhân bản nội dung của 1 list ban đầu.

    ```python
    a = [1, 2, 3]
    b = a * 2
    print(b)
    ```

    ```python
    # ket qua
    [1, 2, 3, 1, 2, 3]
    ```

- Tạo 1 lits có chứa 1000 phần tử là số 0.

    ```python
    a = [0] * 100
    print(a)
    ```

    ```python
    # ket qua
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ```

## 10. Tìm kiếm phần tử trong list.

- Để tìm kiếm phần tử trong list bạn có thể dùng toán tử in hoặc thuật toán tìm kiếm tuyến tính O(n).

    ```python
    a = ['tung dep', 'trai', 'co', 'mot khong hai']
    if 'co' in a:
        print("YES")
    ```

    ```python
    # ket qua
    YES
    ```

## 11. Combine list.

- Bạn có thể sử dụng hàm extend() để thêm các phần tử của 1 list khác vào list hiện tại hoặc sử dụng toán tử +.

    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    a.extend(b)
    print(a)
    a += b
    print(a)
    ```

    ```python
    # ket qua
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6, 4, 5, 6]
    ```

## 12. Các phương thức list.

### Hàm `copy()`

- Hàm copy(): trả về một list mới có nội dung tương tự như list ban đầu nhưng không phải list ban đầu.

    ```python
    a = [1, 2, 3]
    b = a
    print(a is b)
    print(id(a), id(b))
    c = a.copy()
    print(c)
    print(a == c)
    print(a is c)
    print(id(a), id(c))
    ```

    ```python
    # ket qua
    True
    3056442398976 3056442398976       
    [1, 2, 3]
    True
    False
    3056442398976 3056442397056
    ```

### Hàm `count()`

- Hàm `count()`: trả về số lần xuất hiện của một phần tử bất kì trong list.

    ```python
    a = [1, 2, 3, 1, 2, 1, 1]
    print(a.count(1))
    ```

    ```python
    # ket qua
    4
    ```

### Hàm `index()`

- Hàm `index()`: trả về chỉ số đầu tiên của 1 phần tử trong list.

    ```python
    a = [4, 3, 1, 2, 3, 5, 2]
    print(a.index(3))
    # chú ý câu lệnh này gây lỗi
    # print(a.index(1000))
    ```

    ```python
    # ket qua
    2
    ```

### Hàm `reverse()`

- Hàm `reverse()`: để lật ngược một list.

    ```python
    a = [1, 2, 3, 4]
    a.reverse()
    print(a)
    ```

    ```python
    # ket qua
    [4, 3, 2, 1]
    ```

### Hàm `sort()` O(nlogn) (Tim sort)

- Hàm `sort()`: Sắp xếp các phần tử trong list.

    ```python
    a = [1, 5, 4, 3, 2, 1]
    a.sort()
    print(a)
    ```

    ```python
    # ket qua
    [1, 1, 2, 3, 4, 5]
    ```

## 13. Các hàm built-in sử dụng với list.

|Hàm|Chức năng|
|--|--|
|`all()`|Trả về True nếu mọi phần tử trong list đều là True|
|`any()`|Trả về True nếu có ít nhất 1 phần tử trong list là True|
|`max()`|Trả về phần tử lớn nhất trong list|
|`min()`|Trả về phần tử nhỏ nhất trong list|
|`sorted()`|Trả về list đã sắp xếp của list ban đầu|
|`sum()`|Trả về tổng các phần tử trong list|

- Ví dụ:

    ```python
    a = [1, 2, 3, 4, 6, 5]
    print("all(a) = ", all(a))
    print("any(a) = ", any(a))
    print("max(a) = ", max(a))
    print("min(a) = ", min(a))
    print("sum(a) = ", sum(a))
    b = sorted(a)
    print(a)
    print(b)
    ```

    ```python
    all(a) =  True
    any(a) =  True
    max(a) =  6
    min(a) =  1
    sum(a) =  21
    [1, 2, 3, 4, 6, 5]
    [1, 2, 3, 4, 5, 6]
    ```