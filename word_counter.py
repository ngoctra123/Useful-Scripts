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
