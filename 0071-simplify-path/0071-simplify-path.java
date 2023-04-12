class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        int n = paths.length;
        int i = 0;
        for (int j = 0; j < n; j++) {
            if (paths[j].equals("..")) {
                if (i > 0) i--;
            } else if (!paths[j].equals(".") && !paths[j].equals("")) {
                paths[i++] = paths[j];
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < i; j++) {
            sb.append("/").append(paths[j]);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }
}