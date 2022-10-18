function countAndSay(n: number): string {
  let result = "1";
    for (let i = 1; i < n; i++) {
        let count = 1;
        let temp = "";
        for (let j = 1; j < result.length; j++) {
            if (result[j] == result[j - 1]) {
                count++;
            } else {
                temp += count + result[j - 1];
                count = 1;
            }
        }
        temp += count + result[result.length - 1];
        result = temp;
    }
    return result;
};