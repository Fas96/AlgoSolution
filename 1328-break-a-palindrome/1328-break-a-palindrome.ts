function breakPalindrome(palindrome: string): string {
  if(palindrome.length==1){
        return "";
    }
    let i=0;
    while(i<Math.floor(palindrome.length/2)){
        if(palindrome[i]!="a"){
            return palindrome.substring(0,i)+"a"+palindrome.substring(i+1);
        }
        i++;
    }
    return palindrome.substring(0,palindrome.length-1)+"b";
};