# Phân tích Báo cáo tài chính để đánh giá rủi ro và độ tin cậy

## 1. Mục đích báo cáo
Báo cáo này tổng hợp kết quả phân tích theo dữ liệu trong file `dữ liệu lớn.csv` và các biểu đồ, kết quả phân tích có trong notebook `Untitled-1.ipynb`. Mục tiêu là:
- Đánh giá mức độ rủi ro tài chính.
- Xác định nhóm dữ liệu có độ tin cậy cao/ thấp.
- Đưa ra nhận xét, đánh giá và khuyến nghị thuyết phục cho khách hàng.

## 2. Giới thiệu dữ liệu
File `dữ liệu lớn.csv` chứa dữ liệu bảng tài chính với các cột chính sau:
- Tổng tài sản (`Total_Assets`)
- Tổng nợ (`Total_Liabilities`)
- Doanh thu (`Revenue`)
- Chi phí hoạt động (`Operating_Expenses`)
- Lợi nhuận ròng (`Net_Income`)
- Dòng tiền hoạt động (`Cash_Flow_Operating`)
- Dòng tiền đầu tư (`Cash_Flow_Investing`)
- Dòng tiền tài chính (`Cash_Flow_Financing`)
- Tỷ lệ thanh khoản (`Current_Ratio`)
- Tỷ lệ nợ/vốn (`Debt_to_Equity`)
- Biên lợi nhuận gộp (`Gross_Margin`)
- Tỷ suất sinh lợi tài sản (`Return_on_Assets`)
- Tỷ suất sinh lợi vốn chủ sở hữu (`Return_on_Equity`)
- Trạng thái tài chính (`Financial_Status`)

Các giá trị dữ liệu đã được tiền xử lý, phần lớn nằm trong khoảng chuẩn hóa quanh [-1, 1]. Cột mục tiêu `Trạng thái tài chính` phân loại dữ liệu thành:
- `Normal`
- `High Risk`
- `Anomaly`

## 3. Phân tích chính
### 3.1. Phân phối và rủi ro theo nhóm
Các biểu đồ boxplot trong notebook đã cho thấy sự khác biệt rõ giữa ba nhóm:
- Nhóm `Normal`: phân phối giá trị gọn, ít giá trị ngoại lai, thể hiện tính ổn định.
- Nhóm `High Risk`: median thấp hơn ở nhiều chỉ số chính, nhiều giá trị lệch, hàm ý rủi ro thanh khoản và lợi nhuận kém.
- Nhóm `Anomaly`: phân phối rộng, nhiều outliers, biểu hiện dữ liệu bất thường và tiềm ẩn sai số hoặc dấu hiệu hoạt động tài chính không điển hình.

### 3.2. Các chỉ số đặc trưng cần chú ý
- Lợi nhuận ròng (`Net_Income`): nhóm `High Risk` và `Anomaly` có trung vị thấp hơn, nhiều giá trị âm. Đây là chỉ báo chính của lợi nhuận kém và rủi ro giảm doanh thu.
- Tỷ lệ thanh khoản (`Current_Ratio`): nhóm rủi ro cao thường có tỷ lệ thanh khoản thấp hơn, khiến khả năng trả nợ ngắn hạn kém.
- Tỷ lệ nợ/vốn (`Debt_to_Equity`): nhóm `High Risk` và `Anomaly` cho thấy nợ/vốn cao hơn, tức cấu trúc vốn dễ mất cân bằng.
- Tỷ suất sinh lợi tài sản (`Return_on_Assets`) và Tỷ suất sinh lợi vốn chủ sở hữu (`Return_on_Equity`): những nhóm không bình thường có ROA/ROE kém hoặc âm, chỉ ra hiệu suất sử dụng tài sản và vốn giảm.

## 4. Kết quả tương quan giữa các chỉ số
Heatmap tương quan trong notebook cho thấy:
- Doanh thu (`Revenue`) và Chi phí hoạt động (`Operating_Expenses`) có tương quan dương cao, phù hợp với logic kinh doanh khi doanh thu tăng kéo theo chi phí vận hành.
- Lợi nhuận ròng (`Net_Income`) có tương quan dương mạnh với Tỷ suất sinh lợi tài sản (`Return_on_Assets`) và Tỷ suất sinh lợi vốn chủ sở hữu (`Return_on_Equity`), khẳng định lợi nhuận là nhân tố chính cải thiện hiệu suất vốn.
- Tổng tài sản (`Total_Assets`) và Tổng nợ (`Total_Liabilities`) có tương quan dương cao, phản ánh mối quan hệ chặt chẽ giữa quy mô tài sản và quy mô nợ.
- Tỷ lệ nợ/vốn (`Debt_to_Equity`) và Tỷ lệ thanh khoản (`Current_Ratio`) có tương quan âm lớn, nghĩa là khi nợ tăng, tỷ lệ thanh khoản giảm.

## 5. Nhận xét chung
### 5.1. Đánh giá độ tin cậy
- Nhóm `Normal` có độ tin cậy cao nhất do phân phối ổn định và ít giá trị bất thường.
- Nhóm `Anomaly` có thể gồm dữ liệu bất thường hoặc sai lệch, do đó cần kiểm tra kỹ nguyên nhân để tránh kết luận không chính xác.
- Nhóm `High Risk` tuy không nhất thiết là lỗi dữ liệu, nhưng thể hiện rõ rủi ro tài chính thực sự.

### 5.2. Đánh giá rủi ro
- Những hồ sơ có Lợi nhuận ròng (`Net_Income`) và Tỷ suất sinh lợi tài sản (`Return_on_Assets`) thấp, đồng thời Tỷ lệ nợ/vốn (`Debt_to_Equity`) cao và Tỷ lệ thanh khoản (`Current_Ratio`) thấp, là ứng viên rủi ro cao nhất.
- Nhóm `High Risk` là phần dữ liệu cần ưu tiên đánh giá thêm vì khả năng mất khả năng thanh toán và hiệu suất kém.
- Nhóm `Anomaly` yêu cầu phân tích tiếp để xác định xem đó là tình huống đặc thù hoặc là dữ liệu cần làm sạch.

## 6. Khuyến nghị cụ thể
1. **Kiểm tra dữ liệu bất thường**: với nhóm `Anomaly`, nên thực hiện rà soát báo cáo, so sánh với báo cáo gốc để xác định liệu đây là vấn đề báo cáo, dữ liệu sai, hoặc thực trạng tài chính khác thường.
2. **Ưu tiên đánh giá doanh nghiệp `High Risk`**: các doanh nghiệp mang đặc tính này cần phân tích sâu hơn về dòng tiền, hậu quả nợ, và khả năng tái cơ cấu.
3. **Đo lường hệ số thanh khoản và đòn bẩy**: kiểm tra kỹ Tỷ lệ thanh khoản (`Current_Ratio`) và Tỷ lệ nợ/vốn (`Debt_to_Equity`) vì chúng là các chỉ số trực tiếp phản ánh mức độ rủi ro trả nợ.
4. **Sử dụng mô hình đa chỉ số**: tránh chỉ dùng một chỉ số đơn lẻ cho đánh giá. Kết quả heatmap cho thấy các chỉ số tài chính gắn kết, nên cần đánh giá tổng hợp.
5. **Áp dụng kỹ thuật robust**: đối với dữ liệu có outliers, cần dùng phương pháp phân tích chịu nhiễu (robust) để tránh bị lệch do giá trị ngoại lai.

## 7. Kết luận
- Dữ liệu hiện tại cho thấy nhóm `Normal` có độ tin cậy cao và rủi ro thấp.
- Nhóm `High Risk` rõ ràng có dấu hiệu tài chính không bền vững với lợi nhuận thấp, nợ cao và thanh khoản kém.
- Nhóm `Anomaly` cần điều tra thêm trước khi ra quyết định đầu tư hoặc đánh giá rủi ro.

> Với khách hàng, báo cáo này khẳng định rằng việc phân loại và đối chiếu song song các chỉ số tài chính là yếu tố quyết định để xác định cả **rủi ro** và **độ tin cậy** của đánh giá. Đề xuất ưu tiên giám sát các doanh nghiệp có chỉ số `Debt_to_Equity` cao cùng với lợi nhuận âm và thanh khoản giảm.
