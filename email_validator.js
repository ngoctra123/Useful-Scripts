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
