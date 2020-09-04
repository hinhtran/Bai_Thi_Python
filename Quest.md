# Quest
## Q1. What is the difference between list and tuples in Python?
List chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, List có thể chứa bất kỳ kiểu dữ liệu nào. Một List được tạo bởi cặp dấu [].
-Giống List một sự khác biệt với kiểu List đó là các phần tử trong Tuple không thể bị thay đổi sau khi gán chính vì vậy tốc độ của Tuple luôn luôn nhanh hơn so với List, Tuple chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, có thể chứa bất kỳ kiểu dữ liệu nào. Một tuple được tạo bởi cặp dấu ().

## Q2. What are the key features of Python?
+,Dễ hiểu và dễ hiểu

+,Ngôn ngữ lập trình hữu ích

+,Có sẵn cho bất kỳ ai

+,Ngôn ngữ thân thiện với lập trình viên

+,Dễ dàng di chuyển ngôn ngữ

+,Đối tượng định hướng

+,Không phức tạp chạy mã

+,Dễ dàng mở rộng

+,Thư viện tiêu chuẩn tuyệt vời

+,Đặc điểm kỹ thuật dữ liệu

## Q3. What type of language is python?
Python là một ngôn ngữ thông dịch được định kiểu động. Các loại ngôn ngữ này thường được gọi là ngôn ngữ "kịch bản" vì mã không được biên dịch sang dạng nhị phân. Bằng cách nhập động, tôi có nghĩa là các kiểu không cần phải khai báo khi mã hóa, trình thông dịch sẽ tìm ra chúng trong thời gian chạy.

## Q4. How is Python an interpreted language?
Python được gọi là ngôn ngữ thông dịch vì nó đi qua một trình thông dịch, biến mã bạn viết thành ngôn ngữ mà bộ xử lý máy tính của bạn hiểu được. Sau này, khi bạn làm việc trên một dự án trên máy tính của mình, bạn sẽ tải xuống và sử dụng trình thông dịch Python để có thể viết mã Python và thực thi nó theo cách riêng của bạn!

## Q5. What is pep 8?
PEP 8 là hướng dẫn kiểu Python. Đó là một tập hợp các quy tắc về cách định dạng mã Python của bạn để tối đa hóa khả năng đọc của nó. Viết mã cho một đặc tả giúp tạo ra các cơ sở mã lớn, với nhiều người viết, đồng nhất và dễ đoán hơn.

## Q6. How is memory managed in Python?
Trình quản lý bộ nhớ Python quản lý các khối bộ nhớ được gọi là "Khối". Một tập hợp các khối có cùng kích thước tạo nên “Pool”. Các hồ bơi được tạo trên Arenas, các phần của bộ nhớ 256kB được phân bổ trên heap = 64 pool. Nếu các đối tượng bị phá hủy, trình quản lý bộ nhớ sẽ lấp đầy không gian này bằng một đối tượng mới có cùng kích thước.

## Q7. What is name space in Python?

Không gian tên là một cách để triển khai phạm vi. Trong Python, mỗi gói, mô-đun, lớp, hàm và hàm phương thức sở hữu một "không gian tên" trong đó các tên biến được phân giải. Khi một chức năng, mô-đun hoặc gói được đánh giá (nghĩa là bắt đầu thực thi), một vùng tên được tạo. Hãy coi nó như một "bối cảnh đánh giá". Khi một hàm, v.v., kết thúc thực thi, không gian tên sẽ bị xóa. Các biến bị loại bỏ. Thêm vào đó, có một không gian tên chung được sử dụng nếu tên không có trong không gian tên cục bộ.

Mỗi tên biến được kiểm tra trong không gian tên cục bộ (phần thân của hàm, mô-đun, v.v.), và sau đó được kiểm tra trong không gian tên chung.

Các biến thường chỉ được tạo trong một không gian tên cục bộ. Các câu lệnh toàn cục và phi địa phương có thể tạo các biến trong không gian tên cục bộ.

## Q8. What is PYTHON PATH?
PYTHONPATH là một biến môi trường mà bạn có thể đặt để thêm các thư mục bổ sung nơi python sẽ tìm kiếm các mô-đun và gói. Đối với hầu hết các cài đặt, bạn không nên đặt các biến này vì chúng không cần thiết để Python chạy. Python biết tìm thư viện chuẩn của nó ở đâu.

## Q9. What are python modules?
Một mô-đun cho phép bạn tổ chức hợp lý mã Python của mình. Nhóm mã liên quan thành một mô-đun làm cho mã dễ hiểu và dễ sử dụng hơn. Mô-đun là một đối tượng Python với các thuộc tính được đặt tên tùy ý mà bạn có thể liên kết và tham chiếu.

Đơn giản, một mô-đun là một tệp bao gồm mã Python. Một mô-đun có thể xác định các hàm, lớp và biến. Một mô-đun cũng có thể bao gồm mã chạy được

## Q10. What are local variables and global variables in Python? Please give an exam

-Nói chung, một biến được xác định trong một khối thì chỉ có trong khối đó. Nó không thể truy cập được bên ngoài khối. Một biến như vậy được gọi là biến cục bộ. Các mã định danh đối số chính thức cũng hoạt động như các biến cục bộ.

Ví dụ sau sẽ nhấn mạnh điểm này. Nỗ lực in một biến cục bộ bên ngoài phạm vi của nó sẽ dẫn đến lỗi tên.

Example: Function with a Local Variable Copy
def Hello():
    user='Hinh'
    print ("user = ", user)
    return

Example: Function with a Global Variable Copy
user='Hinh'
def Hello():
    print ("user = ", user)
    return

## Q11. What is __init__?
-__ init__ là một phương thức Python đặc biệt được gọi tự động khi bộ nhớ được cấp phát cho một đối tượng mới. Mục đích duy nhất của __init__ là khởi tạo giá trị của các thành viên thể hiện cho đối tượng mới. Sử dụng __init__ để trả về một giá trị ngụ ý rằng một chương trình đang sử dụng __init__ để làm điều gì đó khác với việc khởi tạo đối tượng. Logic này sẽ được chuyển sang phương thức thể hiện khác và được chương trình gọi sau, sau khi khởi tạo.


## Q12. What is self in Python?

Trong Python, từ self là tham số đầu tiên của các phương thức đại diện cho thể hiện của lớp. Do đó, để gọi các thuộc tính và phương thức của một lớp, người lập trình cần sử dụng self.
