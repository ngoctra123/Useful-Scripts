function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

const testEmails = ["test@gmail.com", "invalid-email", "hello@company.co"];
testEmails.forEach(email => {
    console.log(`${email}: ${isValidEmail(email) ? "Hợp lệ" : "Không hợp lệ"}`);
});
