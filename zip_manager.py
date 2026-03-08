import shutil

def create_zip(folder_name, output_filename):
    shutil.make_archive(output_filename, 'zip', folder_name)
    print(f"Đã tạo file {output_filename}.zip")

def extract_zip(zip_file, extract_to):
    shutil.unpack_archive(zip_file, extract_to)
    print(f"Đã giải nén vào {extract_to}")

# create_zip('my_folder', 'backup')
