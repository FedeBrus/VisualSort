/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package visualsort;

import java.util.Random;

/**
 *
 * @author Nicola Corato
 */
public class Ordinamenti {
    public static void stampaArray(int[] arr){
        for(int e : arr){
            System.out.println(e);
        }
    }
    
    public static void shuffle(int[] arr){
        Random r = new Random();
        for(int i = 0; i < arr.length * 1.5; i++){
            int i1 = r.nextInt(arr.length);
            int i2 = r.nextInt(arr.length);
            int temp = arr[i1];
            arr[i1] = arr[i2];
            arr[i2] = temp;
        }
    }
}
