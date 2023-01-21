class Solution {
     public List<String> restoreIpAddresses(String s) {
        List<String> ans= new ArrayList<>();
        backTrack(s,ans,0,0);

        return ans;

    }


   private void backTrack(String s, List<String> ans, int i, int dot)
    {

        if (dot == 3)
        {
           
            if (isValidIp(s))
                ans.add(s);
            return;
        }
        if (i >= s.length())
            return;

        backTrack(s, ans, i + 1, dot);
       
        String temp="";
        
        for (int k = 0; k < i; k++)
            temp += s.charAt(k);
        temp += '.';
        for (int k = i; k < s.length(); k++)
            temp += s.charAt(k);
        backTrack(temp, ans, i + 1, dot + 1);
    }

    private int convertToInt(String str){
        if(str.length()==0||str.length()>3)return 256;
        int leading_zeroes = 0;
        for (int i = 0; i < str.length(); i++)
        {
            if (str.charAt(i) != '0')
                break;
            else
                leading_zeroes++;
        }
        if (leading_zeroes >= 1 && (str.length() != 1))
            return 256;
        int converted_number = 0;
        for (int i = 0; i < str.length(); i++)
        {
            converted_number *= 10;
            converted_number += (str.charAt(i) - '0');
        }

        return converted_number;
    }

    private boolean isValidIp(String IP_part)
    {

        for (int i = 0; i < IP_part.length(); i++)
            if (IP_part.charAt(i) != '.' && (IP_part.charAt(i) < '0' || IP_part.charAt(i) > '9'))
                return false;

        String valid_IP_part = "";
        for (int i = 0; i < IP_part.length(); i++)
        {
            if (IP_part.charAt(i) == '.')
            {

                if ((valid_IP_part == "") || (convertToInt(valid_IP_part) > 255))
                    return false;
                else
                    valid_IP_part = "";
            }
            else
                valid_IP_part += IP_part.charAt(i);
        }

        if (convertToInt(valid_IP_part) > 255)
            return false;
        return true;
    }
}