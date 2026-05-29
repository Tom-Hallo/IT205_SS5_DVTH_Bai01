# ==========================================
# PHÂN TÍCH LỖI VÀ CÁCH SỬA (LEGACY CODE):
# 1. Vì sao cách duyệt cũ sai?
#    - Code cũ đặt vòng lặp 'tháng' ở ngoài, 'chi nhánh' ở trong.
#    - Điều này khiến hệ thống in tháng 1 của tất cả chi nhánh rồi mới tới tháng 2, 
#      làm báo cáo bị phân mảnh, không thể theo dõi liền mạch 3 tháng của một chi nhánh.
# 2. Cách sửa theo đúng nghiệp vụ:
#    - Vòng lặp ngoài: Phải duyệt theo 'chi nhánh'.
#    - Vòng lặp trong: Phải duyệt theo 'tháng'.
# ==========================================

# Khai báo số lượng chi nhánh và tháng cần báo cáo
so_chi_nhanh = 3
so_thang = 3

# Tạo một danh sách 2 chiều để lưu trữ dữ liệu doanh thu
du_lieu_doanh_thu = []

# VÒNG LẶP NGOÀI: Duyệt theo chi nhánh
for chi_nhanh in range(1, so_chi_nhanh + 1):
    doanh_thu_1_chi_nhanh = []
    
    # VÒNG LẶP TRONG: Duyệt theo từng tháng của chi nhánh đó
    for thang in range(1, so_thang + 1):
        tien = int(input(f"Nhập doanh thu Chi nhánh {chi_nhanh}, tháng {thang}: "))
        doanh_thu_1_chi_nhanh.append(tien)
        
    # Thêm danh sách doanh thu của chi nhánh vào mảng tổng
    du_lieu_doanh_thu.append(doanh_thu_1_chi_nhanh)
    print() # In dòng trống cho dễ nhìn giữa các lần nhập chi nhánh

# Hiển thị báo cáo
print("-------------- Kết quả --------------")
# Tiếp tục dùng cấu trúc vòng lặp Chi nhánh (Ngoài) -> Tháng (Trong) để in kết quả
for chi_nhanh in range(1, so_chi_nhanh + 1):
    for thang in range(1, so_thang + 1):
        # Lấy dữ liệu ra (trừ 1 do index trong Python bắt đầu từ 0)
        tien_thuc_te = du_lieu_doanh_thu[chi_nhanh - 1][thang - 1]
        print(f"Chi nhánh {chi_nhanh}, tháng {thang}: {tien_thuc_te} triệu đồng")