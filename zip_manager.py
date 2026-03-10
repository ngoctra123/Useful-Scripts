import shutil

def create_zip(folder_name, output_filename):
    shutil.make_archive(output_filename, 'zip', folder_name)
    print(f"Đã tạo file {output_filename}.zip")

def extract_zip(zip_file, extract_to):
    shutil.unpack_archive(zip_file, extract_to)
    print(f"Đã giải nén vào {extract_to}")

# create_zip('my_folder', 'backup')
import shutil  # Nhập thư viện shutil, chuyên dùng cho các thao tác tệp tin và thư mục nâng cao (như sao chép, nén)
# Hàm dùng để nén một thư mục thành tệp .zip
def create_zip(folder_name, output_filename):
# shutil.make_archive thực hiện việc nén:
    # - output_filename: Tên tệp nén sẽ tạo ra (hàm sẽ tự thêm đuôi .zip)
    # - 'zip': Định dạng nén (có thể thay bằng 'tar', 'gztar', v.v.)
# - folder_name: Đường dẫn tới thư mục mà bạn muốn nén
    shutil.make_archive(output_filename, 'zip', folder_name)
