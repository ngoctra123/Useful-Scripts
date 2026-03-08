#!/bin/bash
echo "Đang bắt đầu cập nhật hệ thống..."
sudo apt update && sudo apt upgrade -y
echo "Dọn dẹp các file thừa..."
sudo apt autoremove -y
echo "Hoàn thành!"
