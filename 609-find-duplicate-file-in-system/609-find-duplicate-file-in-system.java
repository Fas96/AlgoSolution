class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        
          Map<String,List<String>> hm=new HashMap<>();
        List<List<String>> res=new ArrayList<>();

        for (String path:paths) {
            String[] split= path.split(" ");
            String root=split[0];
            for (int i = 1; i < split.length; i++) {
                
               String fileName=  split[i].toString().split("\\(")[0];
               String fileContent=  split[i].toString().split("\\(")[1];
               if(!hm.containsKey(fileContent)){
                   hm.put(fileContent,new ArrayList<>());
                   hm.get(fileContent).add(root+"/"+fileName);
               }else{
                  
                   hm.get(fileContent).add(root+"/"+fileName);
               }

            }

        }
        for (Map.Entry<String,List<String>> val:hm.entrySet()) {
            if(val.getValue().size()>1) res.add(val.getValue());
        }
         




        return  res;
    }
}