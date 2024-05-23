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
