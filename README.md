## Mục tiêu của project
Nhóm nghiên cứu tập trung vào việc phát triển mô hình phát hiện gian lận điểm danh trong lớp học trực tuyến. 
Những mục tiêu mà nhóm nghiên cứu muốn hướng đến và đã đạt được trong project này là:
-	Xây dựng một mô hình phát hiện người điểm danh (học sinh, sinh viên) có giả mạo hay không?
-	Xây dựng một trang web, mô phỏng việc phát hiện giả mạo điểm danh trong lớp học trực tuyến.

## Phương pháp nghiên cứu thực nghiệm
-	Phân tích yêu cầu của một mô hình phát hiện gian lận khuôn mặt.
-	Xây dựng một mô hình phát hiện gian lận khuôn mặt thông qua một vài khung ảnh của người học.
-	Xây dựng một trang web lớp học trực tuyến.
-	Tích hợp mô hình phát hiện giả mạo khuôn mặt vào trang web lớp học trực tuyến đã xây dựng.
-	Đánh giá kết quả đạt được dựa trên thực nghiệm.

    **Input:** 
    Là một chuỗi các frame ảnh (image sequence) được lấy từ video.
    
    **Output:** 
    Người đang thực hiện điểm danh có gian lận điểm danh hay không ? (được gán nhãn <span style="color: green"> Real </span> hoặc <span style="color: red"> Attack </span>).

## Dữ liệu
Replay-Attack Dataset 

*I. Chingovska, A. Anjos, S. Marcel,"On the Effectiveness of Local Binary Patterns in Face Anti-spoofing"; IEEE BIOSIG, 2012.*

## Mô hình
![plot](image//PlotModel.png)

## Đánh giá

**Consfusion Matrix**

![plot](image//ConsfusionMatrix.png)

## Đóng góp 
- Đề tài tập trung nghiên cứu, phát triển về lý thuyết và ứng dụng đối với hướng tiếp cận bài toán phát hiện gian lận điểm danh trong lớp học trực tuyến.

## Hạn chế
- Mô hình vẫn chưa thể nhận diện hoặc nhân diện sai trong nhiều điều kiện khác nhau, trong nhiều kiểu tấn công khác nhau.

## Hướng phát triển
Hiện tại, do hạn chế về thời gian, nghiên cứu dừng lại ở việc thử nghiệm với tập dữ liệu có kích cỡ nhỏ cũng như chưa tìm ra được thông số huấn luyện cho ra kết quả tốt nhất. Nhóm nghiên cứu dự định phát triển đề tài với quy mô lớn hơn về mặt kỹ thuật, cũng như cố gắng tìm ra nhiều bộ thông số huấn luyện nhằm tìm ra kết quả tốt nhất có thể.

Sau khi trải qua mùa dịch COVID, mô hình vẫn có thể được tiếp tục ứng dụng không chỉ riêng việc điểm danh, mà còn có thể ứng dụng vào các vấn đề liên quan tới bảo mật sinh trắc học với quy mô lớn hơn.

Ngoài ra mô hình còn có thể được ứng dụng và phát triển trên các trang web học trực tuyến, các ứng dụng xác thực khuôn mặt cũng như kết hợp với hệ thống nhận dạng danh tính của con người trong không gian thực.

[Nhấn vào đây](https://colab.research.google.com/drive/1a4fsJP_t_V3H3lg54IxDK2XP03VVBu2r) để xem chi tiết file Colab



