qty_laptop = 0
qty_phone = 0
qty_tablet = 0
while True:
    print("===== HỆ THỐNG QUẢN LÝ KHO TỰ ĐỘNG =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        print("\nBÁO CÁO SỐ LƯỢNG TỒN KHO")
        print(f"Laptop: {qty_laptop} sản phẩm")
        print(f"Phone:  {qty_phone} sản phẩm")
        print(f"Tablet: {qty_tablet} sản phẩm")
    elif choice == "2":
        print("\n=== TIẾN HÀNH NHẬP KHO ===")
        print("1 - Laptop | 2 - Phone | 3 - Tablet")
        item_choice = input("Chọn mặt hàng muốn nhập (1-3): ")
        if item_choice == "1" or item_choice == "2" or item_choice == "3":
            while True:
                qty_input = input("Nhập số lượng cần thêm vào kho: ")
                import_qty = int(qty_input)
                if import_qty < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue
                break 
            if item_choice == "1":
                qty_laptop += import_qty
                print(f"-> Đã cộng thêm {import_qty} Laptop vào hệ thống.")
            elif item_choice == "2":
                qty_phone += import_qty
                print(f"-> Đã cộng thêm {import_qty} Phone vào hệ thống.")
            elif item_choice == "3":
                qty_tablet += import_qty
                print(f"-> Đã cộng thêm {import_qty} Tablet vào hệ thống.")
        else:
            print("Mặt hàng không tồn tại. Hủy thao tác nhập.")
    elif choice == "3":
        print("\n=== TIẾN HÀNH XUẤT KHO ===")
        print("1 - Laptop | 2 - Phone | 3 - Tablet")
        item_choice = input("Chọn mặt hàng muốn xuất (1-3): ")
        if item_choice == "1" or item_choice == "2" or item_choice == "3":
            while True:
                qty_input = input("Nhập số lượng cần xuất khỏi kho: ")
                export_qty = int(qty_input)
                if export_qty < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue 
                break 
            if item_choice == "1":
                if export_qty > qty_laptop:
                    print("Không đủ hàng! Hủy thao tác xuất kho.")
                else:
                    qty_laptop -= export_qty
                    print(f"-> Đã xuất thành công {export_qty} Laptop.")   
            elif item_choice == "2":
                if export_qty > qty_phone:
                    print("Không đủ hàng! Hủy thao tác xuất kho.")
                else:
                    qty_phone -= export_qty
                    print(f"-> Đã xuất thành công {export_qty} Phone.")     
            elif item_choice == "3":
                if export_qty > qty_tablet:
                    print("Không đủ hàng! Hủy thao tác xuất kho.")
                else:
                    qty_tablet -= export_qty
                    print(f"-> Đã xuất thành công {export_qty} Tablet.")
        else:
            print("Mặt hàng không tồn tại. Hủy thao tác xuất.")
    elif choice == "4":
        print("\n=== KIỂM TRA MỨC ĐỘ AN TOÀN ===")
        warning_triggered = False
        if qty_laptop < 10:
            print(f"Mặt hàng Laptop sắp hết (Chỉ còn {qty_laptop} sản phẩm).")
            warning_triggered = True
        if qty_phone < 10:
            print(f"Mặt hàng Phone sắp hết (Chỉ còn {qty_phone} sản phẩm).")
            warning_triggered = True
        if qty_tablet < 10:
            print(f"Mặt hàng Tablet sắp hết (Chỉ còn {qty_tablet} sản phẩm).")
            warning_triggered = True
        if not warning_triggered:
            print("Tất cả mặt hàng đều đạt mức an toàn (Tồn kho >= 10).")
    elif choice == "5":
        print("\nTạm biệt! Cam on vi da den.")
        break 
    else:
        print("Lựa chọn không hợp lệ!")
