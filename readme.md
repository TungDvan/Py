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
            print(int('1245asf'))
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

# BÀI 6: NHẬP DỮ LIỆU TỪ BÀN PHÍM TRONG PYTHON BẰNG HÀM INPUT VÀ MAP

## Nhập dữ liệu với hàm input   

* Cú pháp: `input(prompt)`

    * Trong đó `prompt` là thứ sẽ hiện ra chương trình trước khi nhập

* Giá trị trả về: input() trả về xâu kí tự ở kiểu str, các bạn cần chú ý ép kiểu dữ liệu tương ứng của biến trong đề bài.

* Ví dụ:
    ```python
    s = input('xin nhap du lieu tu ban phim: ')
    print('xau vua nhap la: ', s)
    ```

    * input: Tung dep trai co mot khong hai
    * output:
        ```
        xin nhap du lieu tu ban phim: Tung dep trai co mot khong hai
        xau vua nhap la:  Tung dep trai co mot khong hai
        ```

* chú ý hàm `input` sẽ đọc toàn bộ 1 dòng nhập vào và lưu ở dưới dạng `str`

* Nếu muốn nhập một số nguyên thì chúng ta cần phải ép kiểu, bơi vì input trả về kiểu dữ liệu str:
    * Ví dụ:
        ```python
        a = input('nhap mot so nguyen: ')
        print(a, type(a))
        a = int(a)
        print(a, type(a))
        ```
        * Input: 23
        * Output:

        ```
        23 <class 'str'>
        23 <class 'int'>
        ```

    * Chúng ta có thể nhập nhanh như sau:
        ```python
        a = int(input('Nhap mot so nguyen: '))
        print(a, type(a))
        ```
        * Input: 23
        * Output:
        ```
        23 <class 'int'>
        ```
* Tương tự như thế nếu ta muốn ép kiểu sang `float` hay `int`

## Nhập nhiều số trên cùng một dòng

* Tư tưởng: tách chuỗi ra, ép kiểu của tùng giá trị trong chuỗi đó thành kiểu mình muốn

* Ví dụ: input `100 200 300`
    * tách chuỗi thành `100` `200` `300` (đang ở dạng string)
    * Ép kiểu sang số nguyên: `100`, `200`, `300`

* Các công đoạn trong python sẽ như sau (nếu muốn hiểu thì đọc qua, còn không thì next luôn đến ý tiếp theo)

    * Bước 1: Nhập

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        ```

    * Bước 2: Tách ra

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        # B2: Tach ca so ra
        b = a.split()
        # In thu ra xem b la gi
        print(b)
        ```
        * Input: `200 100 300`
        * Output:
            ```
            Nhap 3 so: 200 100 300
            ['200', '100', '300']
            ```

    * Bước 3: Sử dụng map để ép các phần tử trong list sang kiểu dữ liệu mong muốn

        ```python
        # B1: Nhap
        a = input('Nhap 3 so: ')
        # B2: Tach ca so ra
        b = a.split()
        # B3: Su dung map de ep cac phan tu trong lít => kieu du lieu mong muon
        x, y, z = map(int, b)
        # In thu ra xem x, y, z la gi
        print(x + y + z)
        ```

        * Input: `100 200 300`
        * Output:
            ```
            Nhap 3 so: 100 200 300
            600
            ```

        * Chú ý, nếu ở bước 3 chúng ta không có dòng `x, y, z = map(int, b)` mà thay vào đó là `x, y, z = b` thì lúc này x, y, z vẫn sẽ nhận các giá trị và các `string` lần lượt là `'100'` `'200'` `'300'` và phép cộng x + y + z là phép cộng `string` nên kết quả sẽ là `100200300`

            ```python
            # B1: Nhap
            a = input('Nhap 3 so: ')
            # B2: Tach ca so ra
            b = a.split()
            # B3: 
            x, y, z = b
            # In thu ra xem x, y, z la gi
            print(x + y + z)
            ```
            * Input: `100 200 300`
            * Output:
                ```
                Nhap 3 so: 100 200 300
                10020030
                ```

* Làm gọn lại các bước nhập trên 1 dòng sau 3 bước ở trên:

    ```python
    x, y, z = map(int, input('Nhap 3 so nguyen duong: ').split())
    print(x, type(x), y, type(y), z, type(z))
    ```
    * Input: `100 200 300`
    * Output:
        ```
        Nhap 3 so nguyen duong: 100 200 300
        100 <class 'int'> 200 <class 'int'> 300 <class 'int'> 
        ```

# BÀI 7: CÁC HÀM PHỔ BIẾN TRONG PYTHON (SQRT, POW, FLOOR, FACTORIAL, SUM,...)

* Muốn sử dụng những hàm có sẵn ở trong thư viện thì phải có dòng thêm thư viện là `import math` để có thể sử dụng

    * bạn có thể sử dụng câu lệnh `print(help(math))` để biết thư viện này cung cấp những hàm có sẵn và cú pháp các hàm như thế nào

    * Ví dụ:
        ```python
        import math
        print(help(math))
        ```

        Sẽ ra một đống thứ như sau:
        ```
        NAME
            math

        DESCRIPTION
            This module provides access to the mathematical functions
            defined by the C standard.

        FUNCTIONS
            acos(x, /)
                Return the arc cosine (measured in radians) of x.

                The result is between 0 and pi.

            acosh(x, /)
                Return the inverse hyperbolic cosine of x.

            asin(x, /)
                Return the arc sine (measured in radians) of x.

        -- More  --
        ```

## Hàm căn bậc 2: sqrt (square root)

* Cú pháp `math.sqrt()` và nó trả về float (số thực)

* Ví dụ:
    ```python
    import math
    print(math.sqrt(5))
    ```

    Kết quả:

    ```
    2.23606797749979
    ```

* Nhưng mà thay vì ta phải `import math` rùi dùng hàm nào ta sử dụng `math.` rùi tới hàm đó (`math.sqrt`) thì ta có thể sử dụng cú pháp `from math import *`
    * Dấu `*` đại diện cho `all`, tức là ta sẽ ***import*** hết tất cả hàm trong modun math vào chương trình của mình và lúc này ta không cần sử dụng `math.` nữa mà chỉ cần tên hàm có sẵn ra thui
    * Ví dụ
        ```python
        from math import *
        print(sqrt(36))
        ```

        Kết quả:
        ```
        6.0
        ```

## Hàm isqrt (chỉ lấy phần nguyên trong căn bậc 2, chắc là integer square root)

* Cú pháp `isqrt()` và trả về kiểu số nguyên

* Ví dụ:
    ```python
    from math import *
    print(isqrt(37))
    print(type(isqrt(37)))
    ```
    Kết quả:

    ```
    6
    <class 'int'>
    ```

## Hàm pow (hàm luỹ thừa power)

* Cú pháp: `pow(a, b)` (a ^ b) và trả về float

* Ví dụ:
    ```python
    from math import *
    print(pow(2, 10))
    print(type(pow(2, 10)))
    print(pow(10, 1/3)) #Tinh 10^(1/3) = căn bậc 3 của 10
    ```
    Kết quả:
    
    ```
    1024.0
    <class 'float'>
    2.154434690031884
    ```

## Hàm ceil: ceiling (làm tròn lên)

* Cú pháp: `ceil()` và trả về int

* Ví dụ:
    ```python
    from math import *
    print(ceil(2.0))
    print(ceil(2.1))
    print(ceil(2.8))
    ```
    Kết quả:

    ```
    2
    3
    3
    ```

## Hàm floor (làm tròn xuống)

* Cú pháp: `floor()` và trả về int

* Ví dụ:
    ```python
    from math import *
    print(floor(2.0))
    print(floor(2.1))
    print(floor(2.8))
    ```
    Kết quả:

    ```
    2
    2
    2
    ```

## Hàm factorial (hàm giai thừa)

* Cú pháp: `factorial()` trả về int

* Ví dụ:
    ```python
    from math import *
    print(factorial(1000))
    ```

    Kết quả:

    ```
    402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    ```

## Hàm ước chung lớn nhất: gcd(a, b)

* Cú pháp `gcd(a, b)` trả về ucln(a, b)

* Ví dụ:
    ```python
    from math import *
    print(gcd(100, 243))
    ```
    Kết quả:

    ```
    1
    ```

## Hàm tính tổ hợp cập k của n (nCk) comb() (combination)

* Cú pháp: comb(n, k) trả về nCk

* Ví dụ:
    ```python
    from math import *
    print(comb(10, 6))
    ```
    Kết quả:

    ```
    210
    ```

## Hàm fabs: Hàm lấy trị tuyệt đối

* Cú pháp: fabs() và trả về float

* Ví dụ:
    ```python
    from math import *
    print(fabs(-19))
    print(type(fabs(-19)))
    ```
    Kết quả:

    ```
    19.0
    <class 'float'>
    ```

## Những hàm build-in (không cần import math) (các hàm ở trên là math modle)

### Hàm abs (lấy trị tuyệt đối)

* Cú pháp: `abs()` trả về int hoặc float tuy từng TH

* Ví dụ:
    ```python
    print(abs(-19.9), type(abs(-19.9)))
    print(abs(10), type(abs(10)))
    ```
    Kết quả:

    ```
    19.9 <class 'float'>
    10 <class 'int'>
    ```

### Hàm round (làm tròn theo đúng nghĩa đen, theo đúng nguyên tắc làm tròn)

* Cú pháp: `round()` trả về số nguyên

* Ví dụ:
    ```python
    print(type(round(10)))
    print(round(10.9))
    print(round(10.1))
    print(round(10.5))
    ```
    Kết quả:
    
    ```
    11
    10
    10
    ```

### Hàm max, min

* Cú pháp max(x1, x2, ... xn)

* Ví dụ:
    ```python
    print(min(1, 2, 3, 4, 5, 6, -2))
    print(max(1, 3, 653, 345, 234))
    ```
    Kết luận:

    ```
    -2
    653
    ```

### Hàm sum: tính tổng trong một list

* Cú pháp: sum(list)

* Ví dụ:
    ```python
    a = [1, 2, 4, 6, 3]
    print(sum(a))
    print(sum([1, 2, 4, 6, 3]))
    ```
    Kết quả:

    ```
    16
    16
    ```
