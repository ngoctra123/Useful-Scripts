import requests
from bs4 import BeautifulSoup

def get_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2') # Thay đổi tag tùy trang web
    for i, title in enumerate(titles[:10]):
        print(f"{i+1}. {title.text.strip()}")

get_titles("https://news.ycombinator.com/")
import requests  # Thư viện để gửi yêu cầu HTTP (tải nội dung trang web về)
from bs4 import BeautifulSoup  # Thư viện để phân tích và trích xuất dữ liệu từ HTML
def get_titles(url):
    try:
        # Gửi một yêu cầu GET đến địa chỉ URL được cung cấp
        response = requests.get(url)
        
        # Chuyển đổi nội dung HTML của trang web thành một đối tượng "soup" để dễ tra cứu
        # 'html.parser' là trình phân tích cú pháp mặc định của Python
        soup = BeautifulSoup(response.text, 'html.parser')
# Tìm tất cả các thẻ <h2> trong trang web (thường chứa tiêu đề bài viết)
        # Lưu ý: Mỗi trang web dùng thẻ khác nhau (h1, h2, h3, hoặc class)
        titles = soup.find_all('h2') 
        
      


