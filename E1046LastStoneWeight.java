package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class E1046LastStoneWeight {

    public static int lastStoneWeight(int[] stones) {

        ArrayList<Integer> forArr=new ArrayList<Integer>(stones.length);

        for (int i = 0; i < stones.length; i++) {
            forArr.add(stones[i]);
        }
        List<Integer> integerListSort = forArr.stream().sorted().collect(Collectors.toList());

        return lastStoneWeightUt(integerListSort);
    }

    private static Integer lastStoneWeightUt(List<Integer> integerListSort) {
         if(integerListSort.size()==1)return integerListSort.get(0);
        if(integerListSort.size()==0)return 0;
        System.out.println(integerListSort);
        if(integerListSort.size()==2)return   integerListSort.get(1)-integerListSort.get(0);

        int differences = integerListSort.get(integerListSort.size()-1) - integerListSort.get(integerListSort.size()-2);


        if(differences>0){
           return lastStoneWeightUt(Collections.singletonList(integerListSort.subList(0, integerListSort.size() - 1).set(differences, integerListSort.size() - 1)));
        }else{
           return lastStoneWeightUt(integerListSort.subList(0,integerListSort.size()-2));
        }
//        System.out.println(integerListSort);

    }

    public static void main(String[] args) {
        System.out.println(lastStoneWeight(new int[]{2,7,2}));
    }
}
