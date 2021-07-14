package com;

public class Main {
    public static void main(String[] args) {
        int num = 1000;
        int[] result = new int[3000];
        int res = 0;
        result[0] = 1;

        for (int i = 2; i <= 1000; i++) {
            for (int j = 0; j < 2999; j++) {
                //System.out.println(j + ' '+res +' '+result[j]+'\n');
                res = result[j] * i;


                result[j] = res % 10;
                res /= 10;
                result[j+1] += res;
                //if (res == 0)
                  //  break;
                }
            }
        for (int i = 2999;i>=0;i--){
            System.out.print(result[i]);
        }
        }
}
