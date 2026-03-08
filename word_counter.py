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
