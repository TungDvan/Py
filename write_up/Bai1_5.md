# BÀI 1 + 2 + 3 + 4 + 5: CÂU LỆNH PRINT, CHÚ THÍCH, CÁC KIỂU DỮ LIỆU, TOÁN TỬ TRONG PYTHON

## 1. Câu lệnh print

* **Cú pháp**

    ```
    print(objec, sep = seperator, end = end)
    ```

    * Object: các đối tượng trong Python
    * sep: phân cách giữa các đối tượng in, nếu không có tham số này thì mặc định sẽ là dấu cách
    * end: Chỉ ra kí tự được in cuối cùng của dòng, nếu không có tham số này thì mặc đính sẽ là dấu xuống dòng

* Ví dụ:
    * Ví dụ 1:
        ```python
        print('tung dep trai')
        ```
        Kết quả: 
        
        ```
        tung dep trai
        ```
    * Ví dụ 2:
        ```python
        a = 100
        b = 200
        c = 300
        print(a, b, c)
        print('tung dep trai')
        ```
        Kết quả:

        ```
        100 200 300
        tung dep trai
        ``` 
        Như ta thấy thì nếu mà không truyền `sep` vào thì 3 biến (`object` a, b, c) sẽ phân cách nhau bỏi dấu `_` và không truyền `end` thì in xong dòng đó tự động xuống dòng 

* In chuỗi trong python thì để trong dấu ngoặc đơn `''` hay dấu ngoặc kép `""` đều được
    * ví dụ
        ```python
        print('tung dep trai')
        print("co 102")
        ```
        Kết quả:

        ```
        tung dep trai
        co 102
        ```

* In có tham số `sep`
    * ví dụ
        ```python
        print('tung', 'dep', 'trai', sep = '_')
        print('co', '102', sep = '#')
        ```
        kết quả:

        ```
        tung_dep_trai
        co#102  
        ```
        như vậy nếu ta truyền `sep` vào thì giữa các object sẽ là thứ ta đưa vào `sep`, trong TH trên là `_` và `#`

* In có tham số `end`
    * ví dụ 1:
        ```python
        print('C', 'Python', 'java', end = '!')
        ```
        kết quả:

        ```
        C Python java!
        ```

    * ví dụ 2:
        ```python
        print('C', 'Python', 'java', end = '!')
        print('tung dep trai')
        ```
        kết quả:

        ```
        C Python java!tung dep trai
        ```
        ở ví dụ 2 ta thấy mặc dù in 2 dòng nhưng mà hiện chỉ ở trên 1 dòng, co dòng thứ nhất kết thúc chỉ là `!` chứ không có xuống dòng, nên nó sẽ in luôn nội dung thứ 2, nếu muốn xuống dòng in dòng 2 thì thêm `\n` (`!\n`)

        ```python
        print('C', 'Python', 'java', end = '!\n')
        print('tung dep trai')
        ```
        kết quả:

        ```
        C Python java!
        tung dep trai
        ```

## 2. Python syntax và chú thích:

* Các câu lệnh trong python không có kết thúc bằng dấu chấm phẩy, trong các ngôn ngữ khác thì thụt lề khi code giúp cho code trở nên dễ đọc hơn, điều đó cũng cần khi code python

* Python sử dụng thụt lề để chỉ ra một khối lệnh mới

* Chú thích trên 1 dòng: sử dụng dấu `#`

    * ví dụ:
        ```python
        # đây là chú thich
        print('hello')
        ```  
        kết quả:

        ```
        hello
        ```

* Chú thích trên nhiều dòng: sử dụng `"""(chú thích)"""`

    * ví dụ:
        ```python
        """
        đây là chú thích
        trên nhiều dòng
        """
        print('Mrs.Bat_Hop_Phap')
        ```
        kết quả:

        ```
        Mrs.Bat_Hop_Phap
        ```
        mình có thể sử dụng dấu nháy đơn cho nháy kép trong chú thích đều được

    * ví dụ:
        ```python
        '''
        đây là chú thích
        trên nhiều dòng
        '''
        print('Mr.Gnut')
        ```
        kết quả:

        ```
        Mr.Gnut
        ``` 

## 3. Biến và kiểu dữ liệu

### 3.1 Biến

* biến là vùng chứa lưu dữ liệu phục vụ bài toán

* trong python các bạn không cần phải khai báo biến cũng như chỉ rõ kiểu dữ liệu của biến đó, biến sẽ được tạo và xác định kiểu tự động (dynamic typing) khi bạn gán giá trị cho nó.

* để biết kiểu dữ liệu của biến các bạn có thể sử dụng hàm `type()`

    * ví dụ
        ```python
        a = 100
        print(type(a))
        s = 'hello'
        print(type(s))
        ```
        kết quả:

        ```
        <class 'int'>
        <class 'str'>
        ```

* chú ý đặt tên biến:

    * không được đặt tên biến có chứa dấu cách, kí tự đặc biệt, bắt đầu bằng chữ số

        * ví dụ `dien tich`, `di@nTich`, `4ienTic&` đều khồn được

    * tên biến trong python có phân biệt chữ hoa và chữ thường

        * ví dụ: `dientich` khác `dienTich`

### 3.2 Kiểu dữ liệu

* ***Kiểu dữ liệu số***

    * trong python có 3 kiểu dữ liệu số: *số nguyên* (`int`), *số thực dấu phẩy động* (`floating-point numbers`), và *số phức* (`complex numbers`)

        * ví dụ:
            ```python
            a = 8
            b = 0.6
            c = 8 + 10j
            print(type(a), type(b), type(c), sep = '\n')
            ```
            kết quả:

            ```
            <class 'int'>
            <class 'float'>  
            <class 'complex'>
            ```
        **a) Số nguyên**
        
        * đối với số nguyên thì trong python không có giới hạn về giá trị mà số nguyên có thể lưu, bạn có thể xử lý số nguyên lớn trong python

        * ví dụ:
            ```python
            a = 3476554457474568237548235682648235482358
            print(a)
            print(type(a))
            ```
            kết quả:

            ```
            3476554457474568237548235682648235482358
            <class 'int'>
            ```

        * trong python thì các số nguyên thường được in ra dưới dạng cơ số 10, nhưng bạn cũng có thể in ra các số ở hệ 2, 8, 16

            |Tiền tố (Prefix)|Ý nghĩa (Interpretation)| Cơ số (Base)|
            |--|--|--|
            |'0b' hoặc '0B'|Hệ nhị phân (Binary)|2|
            |'0o' hoặc '0O'|Hệ bát phân (Octal)|8|
            |'0x' hoặc '0X'|Hệ 16 (Hexadecimal)|16|

        * ví dụ
            ```python
            a = 0b01101
            b = 0o15423
            c = 0x236af
            print(a, b, c, sep = '\n')
            ```
            Kết quả:

            ```
            13
            6931
            145071
            ```
        **b) Số thực**

        * Số thực là số âm, dương kèm theo phần thập phân

        * Trong python giá trị số thực có thể lưu lớn nhất xấp xỉ 1,8.10<sup>308</sup>, các giá trị lớn hơn số này được mô tả bởi chuỗi `inf` (infinity). Giá trị số thực nhỏ nhất có thể lưu là 5,0.10<sup>-324</sup>, các giá trị nhỏ hơn số này được coi là `0`

            * ví dụ:
                ```python
                a = 3.5
                b = 3e5
                c = 1.9e308
                d = 5.3e-325
                print(a, b, c, d, sep = '\n')
                ```
                Kết quả:

                ```
                3.5
                300000.0
                inf
                0.0
                ```
        
        * In số thực với lượng chữ số sau dấu phẩy xác định:

            * ví dụ:
                ```python
                a = 28.235123
                print('%.2f' % a)
                print(round(a, 2))
                print('{:.2f}'.format(a))
                ```
                Kết quả:

                ```
                28.24
                28.24
                28.24
                ```
        **c) Số phức**

        * Số phức gồm phần thực (real part) và phần ảo (imaginary part) đi kèm `j`

        * Bạn có thể trích xuất phần thực và phần ảo của số phức bằng `.real` và `.imag`

        * ví dụ
            ```python
            a = 6 + 10j
            print(a.real, a.imag, sep = '\n')
            ```
            Kết quả:

            ```
            6.0
            10.0
            ```

* ***Kiểu đúng sai***

    * Kiểu Bool chỉ lưu 2 giá trị `True` hoặc `False`

        * Ví dụ:
            ```python
            a = True
            b = False
            print(type(a))
            print(type(b))
            ```
            Kết quả:

            ```
            <class 'bool'>
            <class 'bool'>
            ```
            Chú ý: `True` và `False` viết hoa ở đầu tiên
        
    * Các giá trị được xác định là True nếu là xâu khác rỗng và số khác không

        * Ví dụ:
            ```python
            print(bool(100))
            print(bool(0))
            print(bool('2344'))
            print(bool(''))
            ```
            Kết quả:

            ```
            True
            False
            True
            False
            ```
    
* ***Kiểu xâu kí tự***

    * Xâu kí tự trong python được đặt trong nháy đơn hoặc nháy kép trên 1 dòng, trong TH xâu có nhiều dòng ta đặt giữa 3 nháy kép

    * ví dụ
        ```python
        a = "Mrs.Bat_Hop_Phap"
        b = """Tung
        Dvan
        """
        print(a)
        print(b)
        ```
        Kết quả:

        ```
        Mrs.Bat_Hop_Phap
        Tung
        Dvan
        ```

    * chú ý trong python thì một kí tự cũng được coi là 1 string

* ***Ép kiểu***
    
    * Khi bạn muốn định kiểu cho một biến nào đó bạn có thể ép kiểu cho nó. Quá trình casting trong Python được hoàn thành bằng cách sử dụng `constructor`

    * `int()`: Ép kiểu sang số nguyên

        * Ví dụ:
            ```python
            a = int(123)
            b = int('123')
            c = int(123.456)
            print(a, b, c, sep = '\n')
            ```
            Kết quả:

            ```
            123
            123
            123
            ```
    
    * Tương tự với `float()`, `str()`

    * Chú ý không thể ép sang mà định dạng nó tào lao

        * Ví dụ:
            ```python
            print(in('1245asf'))
            ```
            Kết quả:

            ```
            ValueError: invalid literal for int() with base 10: '1245asf'
            ```

## 4. Toán tử

*  Các loại toán tử trong python

    |||
    |--|--|
    |Toán tử gán|Assignment operator|
    |Toán tử toán học|Arthmetic operator|
    |Toán tử so sánh|Comparison operator|
    |Toán tử logic|Logical operator|
    |Toán tử nhận dạng|Identity operator|
    |Toán tử thành viên|Membership operartor|
    |Toán tử bit|Bitwire operator|

### a) Toán tử gán

* Cú pháp `a = b`. 
    
    * Ý nghĩa: gán giá trị b cho a

* Ví dụ:

    ```python
    a = 100
    print(a)


    b, c, d = 200, 300, 400     # gán trên cùng một dòng
    e, f = 10, '28tech'         # gán trên cùng một dòng có thể khác kiểu dữ liệu
    print(b, c, d)
    print(e, type(e))
    print(f, type(f))
    ```

    Kết quả:
    
    ```
    100   
    200 300 400
    10 <class 'int'>
    28tech <class 'str'>
    ```

* Hoán vị 2 giá trị `a, b = b, a`

    * Ví dụ:
        ```python
        a, b = 100, '28tech'
        print(a, b)
        print(type(a), type(b))
        a, b = b, a
        print(a, b)
        print(type(a), type(b))
        ```

        Kết quả:

        ```
        100 28tech
        <class 'int'> <class 'str'>
        28tech 100
        <class 'str'> <class 'int'>
        ```

### b) Toán tử toán học

|Toán tử|Ý nghĩa|Ví dụ|Kết quả|
|--|--|--|--|
|+|Cộng|a = 100 + 200|300|
|-|Trừ|a = 100 - 200|-100|
|*|Nhân|a = 100 * 200|20000|
|/|Chia thập phân|a = 100 / 200|0.5|
|//|Chia nguyên|a = 300 / 200|1|
|%|Chia dư|a = 15 % 2|1|
|**|Luỹ thừa|a = 2**10|1024|

* Ví dụ
    ```python
    a, b = 2, 5
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(a ** b)
    ```

    Kết quả:
    ```
    7   
    -3
    10
    0.4
    0
    2
    32
    ```

* Chú ý: ta có thể tính nhanh câu lệnh như `a = a + 100` thành `a += 100` (áp dụng tương tự với các phép khác như cộng trừ nhân chia ...)

    * Ví dụ:
        ```python
        a = 100
        a *= 10 # a = a * 10
        print(a)
        ```
        Kết quả:

        ```
        1000
        ```

### c) Toán tử so sánh

* Khi bạn sử dụng toán tử so sánh thì kết quả phép so sánh sẽ trả về True hoặc False

    |Toán tử|Ý nghĩa|Ví dụ|Kết quả|
    |--|--|--|--|
    |==|So sánh bằng|100 == 100|True|
    |>|Lớn hơn|200 > 300|False|
    |>=|Lơn hơn hoặc bằng|100 >= 100| True|
    |<|Nhỏ hơn| 1 < 2|True|
    |<=|Nhoe hơn hoặc bằng|9 <= 2|False|
    |!=|Khác|2 != 2|False|

### d) Toán tử logic

* Bạn có thể sử dụng các toán tử `and`, `or`, `not` để kết hợp nhiều biểu thức so sánh

    |Toán tử|Ý nghĩa|Ví dụ|Kết quả|
    |--|--|--|--|
    |and|Toán tử và|(20 == 20) and (1 < 0)|False|
    |or|Toán tử hoặc|(10 < 20) or (20 == 50)|True|
    |not|Toán tử phủ định|not(20 == 20)|False|

* Chú ý: `and` chỉ đúng khi tất cả đều đúng, `or` chỉ đúng khi ít nhất 1 cái đúng

* Ví dụ:
    ```python
    x = 50
    print((x > 60) or (x == 50))
    print((x > 40) and (x < 60))
    print(not(x))
    ```
    Kết quả:

    ```
    True
    True
    False
    ```
    
### e) Toán tử nhận dạng

* Toán tử nhận dạng dùng để so sánh 2 `đối tượng` chứ không phải so sánh 2 giá trị.


    |Toán tử|Ý nghĩa|
    |--|--|
    |is|Trả về True nếu 2 đối tượng là giống nhau|
    |is not|Trả về True nếu 2 đối tượng là khác nhau|

* Ví dụ học sinh A có tên là Nam (A: Nam), học sinh B có tên là Nam (B: Nam), nếu ta so sánh Nam(A) == Nam(B) thì trả về giá trị đúng, do 2 bạn A và B đều có tên là nam, nhưng nếu ta so sánh về đối tượng thì bạn A và bạn B là 2 bạn hoàn toàn khác nhau, ví dụ sau về list sẽ cho ta thấy điều đó.

    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
    print(id(a))
    print(id(b))
    print(a is b)
    ```
    Kết quả:

    ```
    True
    1824959944960
    1824959943040
    False
    ```

### f) Toán tử thành viên

* toán tử thành viên được dùng để kiểm tra sự tồn tại của một đối tượng trong list, xâu, tuple,...

    |Toán tử|Ý nghĩa|Ví dụ|Kết quả|
    |--|--|--|--|
    |in|Trả về True nếu đối tượng kiểm tra tồn tại|'a' in 'abcd'|True|
    |not in|Trả về True nếu đối tượng kiểm tra không tồn tại|'a' not in '28tech'|True|

* Ví dụ
    ```python
    s = 'Tung dep trai co mot khong hai'
    print("xau trai" in s)
    print('dep trai' in s)
    ```
    Kết quả:

    ```
    False
    True
    ```

    





