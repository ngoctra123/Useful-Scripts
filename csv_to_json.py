import csv
import json

def convert_csv_json(csv_path, json_path):
    data = []
    with open(csv_path, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for rows in csv_reader:
            data.append(rows)
            
    with open(json_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# convert_csv_json('data.csv', 'data.json')
import csv   # Thư viện hỗ trợ đọc và ghi file CSV
import json  # Thư viện hỗ trợ xử lý dữ liệu định dạng JSON
def convert_csv_json(csv_path, json_path):
    """
    Hàm thực hiện chuyển đổi một file CSV thành file JSON.
    csv_path: Đường dẫn tệp CSV nguồn.
    json_path: Đường dẫn tệp JSON đích sẽ tạo ra.
    """
    data = [] # Khởi tạo danh sách để chứa dữ liệu từ các dòng của CSV
  # Bước 1: Mở và đọc file CSV
    # Sử dụng 'with' để đảm bảo file được đóng tự động sau khi xử lý xong
    # encoding='utf-8' giúp đọc được các ký tự tiếng Việt hoặc ký tự đặc biệt
    with open(csv_path, encoding='utf-8') as csvf:
        # DictReader sẽ biến mỗi dòng trong CSV thành một Dictionary (Object)
        # Trong đó: Key là tiêu đề cột, Value là dữ liệu tương ứng của dòng đó
        csv_reader = csv.DictReader(csvf)
        
        # Duyệt qua từng dòng dữ liệu trong file CSV
        for rows in csv_reader:
            # Thêm dictionary của dòng hiện tại vào danh sách data
            data.append(rows)


