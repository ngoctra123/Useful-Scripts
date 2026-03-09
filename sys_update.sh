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
