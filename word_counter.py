def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            print(f"Số lượng từ: {len(words)}")
            print(f"Số lượng ký tự: {len(text)}")
    except FileNotFoundError:
        print("Không tìm thấy file!")

# count_words('note.txt')
def count_words(filepath):
    # Sử dụng khối try-except để xử lý lỗi nếu không tìm thấy file
    try:
        # Mở file với đường dẫn 'filepath'
        # 'r': Chế độ đọc (read)
        # encoding='utf-8': Đảm bảo đọc đúng các ký tự tiếng Việt hoặc ký tự đặc biệt
        with open(filepath, 'r', encoding='utf-8') as f:
            # Đọc toàn bộ nội dung của file và lưu vào biến 'text'
            text = f.read()
 # Tách nội dung thành một danh sách các từ dựa trên khoảng trắng (dấu cách, xuống dòng, tab)
            words = text.split()
            
            # In ra số lượng phần tử trong danh sách 'words' (tương ứng với số từ)
            print(f"Số lượng từ: {len(words)}")
            
            # In ra độ dài của chuỗi 'text' (tương ứng với tổng số ký tự, bao gồm cả khoảng trắng)
            print(f"Số lượng ký tự: {len(text)}")
except FileNotFoundError:
        # Thông báo lỗi nếu đường dẫn file cung cấp không chính xác hoặc file không tồn tại
        print("Không tìm thấy file! Vui lòng kiểm tra lại đường dẫn.")
