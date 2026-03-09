const exchangeRates = {
    "USD_TO_VND": 25000,
    "EUR_TO_VND": 27000,
    "JPY_TO_VND": 165
};

function convertToVND(amount, currency) {
    const rate = exchangeRates[`${currency}_TO_VND`];
    if (rate) {
        return (amount * rate).toLocaleString('vi-VN') + " VND";
    }
    return "Không hỗ trợ loại tiền này";
}

console.log(convertToVND(100, "USD"));
/ 1. Khai báo một đối tượng (Object) lưu trữ tỷ giá hối đoái
// Mỗi thuộc tính đóng vai trò như một "bản đồ" để tra cứu giá trị quy đổi sang VND
const exchangeRates = {
    "USD_TO_VND": 25000, // 1 USD = 25,000 VND
    "EUR_TO_VND": 27000, // 1 EUR = 27,000 VND
    "JPY_TO_VND": 165    // 1 JPY = 165 VND
};
/**
 * Hàm chuyển đổi một số tiền ngoại tệ sang VND
 * @param {number} amount - Số tiền cần chuyển đổi
 * @param {string} currency - Mã loại tiền (ví dụ: "USD", "EUR", "JPY")
 */
function convertToVND(amount, currency) {
    // 2. Tạo mã tra cứu động bằng Template Literals (dấu backtick ``)
    // Nếu currency là "USD", biến key sẽ trở thành "USD_TO_VND"
    const rateKey = `${currency}_TO_VND`;

    // 3. Truy xuất tỷ giá từ đối tượng exchangeRates dựa trên mã vừa tạo
    const rate = exchangeRates[rateKey];
 // 4. Kiểm tra xem loại tiền này có tồn tại trong dữ liệu tỷ giá không
    if (rate) {
        // Thực hiện phép tính: Số tiền * Tỷ giá
        const total = amount * rate;
 // 5. Định dạng số tiền theo tiêu chuẩn Việt Nam (thêm dấu chấm phân cách hàng nghìn)
        // Ví dụ: 2500000 -> "2.500.000"
        return total.toLocaleString('vi-VN') + " VND";
    }

    // 6. Trả về thông báo lỗi nếu không tìm thấy tỷ giá phù hợp
    return "Không hỗ trợ loại tiền này";
}

// Chạy thử hàm: Chuyển đổi 100 USD sang VND
// Kết quả in ra: "2.500.000 VND"
console.log(convertToVND(100, "USD"));
