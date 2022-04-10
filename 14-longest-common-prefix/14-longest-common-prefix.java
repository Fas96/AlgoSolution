class Solution {
    public String longestCommonPrefix(String[] strs) {
     
        List<String> collect = Arrays.stream(strs).sorted(Comparator.comparing(String::length)).collect(Collectors.toList());
        
        if(collect.size()==1) return collect.get(0);
        StringBuilder sb= new StringBuilder();
        for (int i = 0; i < collect.get(0).length(); i++) {
            int finalI = i;
            boolean allMatch = collect.stream().allMatch(e -> e.charAt(finalI) == collect.get(0).charAt(finalI));
            if(allMatch){sb.append(collect.get(0).charAt(i));}else{break;}
        }
        return String.valueOf(sb);
    }
}