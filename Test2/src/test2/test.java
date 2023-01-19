package test2;

import java.awt.*;
import javax.swing.*;
import visualsort.Rectangle;
import visualsort.Rectangle;

public class test {
    JFrame frame = new JFrame("Cane dio");
    JPanel pnl = new JPanel();
    int TITLEGAP = 40;
    int WIDTH = 500, HEIGHT = 500 + TITLEGAP;
    
    public test() {
        frame.setSize(WIDTH,HEIGHT);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(pnl);
        pnl.setBackground(Color.black);
//-------------------------------------------------------------------------        
        int size = 10;
        pnl.setLayout(new GridLayout(1, size)); //  <--------- sesso grande
        int value;
        int[] arr = new int[10];
        
        int i;
        for(i = 1; i <= size; i++)
            arr[i-1] = i;
        
        for(i = 0; i < size; i++) {
            value = arr[i];
            pnl.add(new Rectangle(value, WIDTH/size, value*(HEIGHT-TITLEGAP)/size,0, -HEIGHT));
        }
    }
    
    public static void main(String[] args) {
        new test();
    }
}
