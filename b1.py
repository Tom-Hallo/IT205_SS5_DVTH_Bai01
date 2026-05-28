branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

result = ""

for branch in range(1, month_count + 1):
    for month in range(1, branch_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )
        
        result = result + f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"

print(result)

# Code cũ đang duyệt theo tháng trước nên dữ liệu bị nhóm theo tháng, không theo chi nhánh
# Theo nghiệp vụ, vòng lặp ngoài nên duyệt theo chi nhánh còn vòng lặp trong nên duyệt theo tháng