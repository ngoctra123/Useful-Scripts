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
