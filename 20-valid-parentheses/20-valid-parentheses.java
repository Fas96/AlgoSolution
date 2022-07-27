class Solution {
    public boolean isValid(String str) {
        while (str.contains("()") || str.contains("[]") || str.contains("{}")) {
    str = str.replaceAll("\\(\\)", "")
      .replaceAll("\\[\\]", "")
      .replaceAll("\\{\\}", "");
}
return (str.length() == 0);
    }
}