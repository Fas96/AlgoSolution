function numberToWords(num: number): string {

    let map: Map<number, string> = new Map();
    // 0 <= num <=Number.MAX_SAFE_INTEGER
    
    map.set(0, "Zero");
    map.set(1, "One");
    map.set(2, "Two");
    map.set(3, "Three");
    map.set(4, "Four");
    map.set(5, "Five");
    map.set(6, "Six");
    map.set(7, "Seven");
    map.set(8, "Eight");
    map.set(9, "Nine");
    map.set(10, "Ten");
    map.set(11, "Eleven");
    map.set(12, "Twelve");
        
    map.set(13, "Thirteen");
    map.set(14, "Fourteen");
    
    map.set(15, "Fifteen");
    map.set(16, "Sixteen");
    map.set(17, "Seventeen");
    map.set(18, "Eighteen");
    map.set(19, "Nineteen");
    map.set(20, "Twenty");
    map.set(30, "Thirty");
    map.set(40, "Forty");
    map.set(50, "Fifty");
    map.set(60, "Sixty");
    map.set(70, "Seventy");
    
    map.set(80, "Eighty");
    
    map.set(90, "Ninety");
    map.set(100, "Hundred");
    map.set(1000, "Thousand");
    map.set(1000000, "Million");
    map.set(1000000000, "Billion");

    // 0 <= num <=Number.MAX_SAFE_INTEGER
    
    if (num < 21) {
        return map.get(num);
    }
    if (num < 100) {
        let result: string = "";
        let tens: number = Math.floor(num / 10) * 10;
        let ones: number = num % 10;
        result += map.get(tens);
        if (ones > 0) {
            result += " " + map.get(ones);
        }
        return result;
    }
    if (num < 1000) {
        let result: string = "";
        let hundreds: number = Math.floor(num / 100);
        let rest: number = num % 100;
        result += map.get(hundreds) + " " + map.get(100);
        if (rest > 0) {
            result += " " + numberToWords(rest);
        }
        return result;
    }
    if (num < 1000000) {
        let result: string = "";
        let thousands: number = Math.floor(num / 1000);
        let rest: number = num % 1000;
        result += numberToWords(thousands) + " " + map.get(1000);
        if (rest > 0) {
            result += " " + numberToWords(rest);
        }
        return result;
    }
    if (num < 1000000000) {
        let result: string = "";
        let millions: number = Math.floor(num / 1000000);
        let rest: number = num % 1000000;
        result += numberToWords(millions) + " " + map.get(1000000);
        if (rest > 0) {
            result += " " + numberToWords(rest);
        }
        return result;
    }
    let result: string = "";
    let billions: number = Math.floor(num / 1000000000);
    let rest: number = num % 1000000000;
    result += numberToWords(billions) + " " + map.get(1000000000);
    if (rest > 0) {
        result += " " + numberToWords(rest);
    }
    return result;
    
};