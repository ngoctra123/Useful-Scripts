function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

const testEmails = ["test@gmail.com", "invalid-email", "hello@company.co"];
testEmails.forEach(email => {
    console.log(`${email}: ${isValidEmail(email) ? "Hợp lệ" : "Không hợp lệ"}`);
});
/**
 * Hàm kiểm tra xem một chuỗi có phải là email hợp lệ hay không
 * @param {string} email - Chuỗi email cần kiểm tra
 * @returns {boolean} - Trả về true nếu hợp lệ, false nếu không
 */
function isValidEmail(email) {
    // Định nghĩa biểu thức chính quy (Regex) để kiểm tra định dạng email
    // ^: Bắt đầu chuỗi
    // [^\s@]+: Một hoặc nhiều ký tự KHÔNG phải là khoảng trắng hoặc ký hiệu @
    // @: Phải có một ký hiệu @ ở giữa
    // [^\s@]+: Tên miền (ví dụ: 'gmail', 'yahoo') - không chứa khoảng trắng/@
    // \.: Phải có một dấu chấm (.) sau tên miền
    // [^\s@]+: Phần mở rộng (ví dụ: 'com', 'vn') - không chứa khoảng trắng/@
    // $: Kết thúc chuỗi
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
// Sử dụng phương thức .test() để so khớp chuỗi email với biểu thức chính quy
    return regex.test(email);
}

// Danh sách các email mẫu để chạy thử nghiệm
const testEmails = ["test@gmail.com", "invalid-email", "hello@company.co"];

// Duyệt qua từng email trong mảng testEmails
testEmails.forEach(email => {
   

