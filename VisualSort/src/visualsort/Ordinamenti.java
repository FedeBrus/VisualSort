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
    private static void scambia(int[] arr, int i1, int i2){
            int temp = arr[i1];
            arr[i1] = arr[i2];
            arr[i2] = temp;
    }
    
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
            scambia(arr, i1, i2);
        }
    }
    
    public static void bubbleSort(int[] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr.length - 1 - i; j++){
                if(arr[j] > arr[j + 1]){
                    scambia(arr, j, j + 1);
                }
            }
        }
    }
    
    public static void insertionSort(int[] arr){
        for(int i=0;i<arr.length;++i){
            int j = i;
            while(j > 0 && arr[j-1]>arr[j]){
                int key = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = key;
                j = j-1; 
            }
      }
    }
}
