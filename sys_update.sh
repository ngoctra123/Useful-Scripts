#!/bin/bash
echo "Đang bắt đầu cập nhật hệ thống..."
sudo apt update && sudo apt upgrade -y
echo "Dọn dẹp các file thừa..."
sudo apt autoremove -y
echo "Hoàn thành!"
#!/bin/bash
# Dòng trên gọi là Shebang, thông báo cho hệ thống rằng file này sẽ được thực thi bằng Bash shell

# In thông báo ra màn hình để người dùng biết quá trình bắt đầu
echo "Đang bắt đầu cập nhật hệ thống..."
# sudo apt update: Cập nhật danh sách các gói phần mềm từ các kho lưu trữ (repositories)
# &&: Toán tử logic "AND", lệnh phía sau chỉ chạy nếu lệnh phía trước thành công
# sudo apt upgrade -y: Nâng cấp tất cả các phần mềm đã cài đặt lên phiên bản mới nhất
# -y: Tự động trả lời "Yes" (đồng ý) cho tất cả các câu hỏi xác nhận trong quá trình nâng cấp
sudo apt update && sudo apt upgrade -y
# In thông báo dọn dẹp
echo "Dọn dẹp các file thừa..."

# sudo apt autoremove -y: Tự động gỡ bỏ các gói phần mềm/thư viện đã được cài đặt tự động 
# nhưng hiện tại không còn chương trình nào cần dùng đến chúng nữa (giúp tiết kiệm dung lượng)
sudo apt autoremove -y


