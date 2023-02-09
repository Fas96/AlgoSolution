class Solution {


    public long distinctNames(String[] ideas) {
        Map<Character, Set<String>> companyStartingInitialsMap = new HashMap<>();

        buildCompaniesStartingInitialsTable(ideas, companyStartingInitialsMap);

        long res = 0;
        for(char key: companyStartingInitialsMap.keySet())
        {
            Set<String> currentCompany=companyStartingInitialsMap.get(key);
            for(char key1: companyStartingInitialsMap.keySet())
            {
                if(isInitialsCompany(key, key1)) continue;
                Set<String> isNameMatchPossibleCompany=companyStartingInitialsMap.get(key1);

                Set<String> setOfSimilarNames=getSetSimilarCompanyNames(currentCompany, isNameMatchPossibleCompany);

                res+=((long) getUniqueNamesCount(isNameMatchPossibleCompany, setOfSimilarNames) * getUniqueNamesCount(currentCompany, setOfSimilarNames));
            }
        }


        return res;

    }
   private   Set<String> getSetSimilarCompanyNames(Set<String> s1, Set<String> s2)
    {
       return s2.stream().filter(s1::contains).collect(HashSet::new, Set::add, Set::addAll);
    }
    
    private  int getUniqueNamesCount(Set<String> isNameMatchPossibleCompany, Set<String> setOfSimilarNames) {
        return isNameMatchPossibleCompany.size() - setOfSimilarNames.size();
    }

    
    //check if key is same
    private static boolean isInitialsCompany(char key, char key1) {
        return key == key1;
    }
    

    private  void buildCompaniesStartingInitialsTable(String[] ideas, Map<Character, Set<String>> companyStartingInitialsMap) {
        for (String idea : ideas) {
            char initial = idea.charAt(0);
            Set<String> ls = companyStartingInitialsMap.getOrDefault(initial,new HashSet<>());
            ls.add(idea.substring(1));
            companyStartingInitialsMap.put(initial, ls);
        }
    }
}