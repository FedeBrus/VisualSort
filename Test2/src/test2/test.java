package test2;

import java.awt.*;
import javax.swing.*;

public class test2 {
    JFrame frame = new JFrame("Cane dio");
    JPanel pnl = new JPanel();
    int TITLEGAP = 38;
    int WIDTHerror = 10;
    int WIDTH = 504 + WIDTHerror, HEIGHT = 500 + TITLEGAP;
    
    public test2() {
        frame.setSize(WIDTH,HEIGHT);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(pnl);
        pnl.setBackground(Color.black);
//-------------------------------------------------------------------------        
        int size = 25;
        pnl.setLayout(new GridLayout(1, size)); //  <--------- sesso grande
        int value;
        int[] arr = new int[size];
        
        int i;
        for(i = 1; i <= size; i++)
            arr[i-1] = i;
        
        int rectX = 0, rectY, rectW, rectH;
        for(i = 0; i < size; i++) {
            value = arr[i];
            rectW = (WIDTH - WIDTHerror)/size;
            rectH = value*(HEIGHT-TITLEGAP)/size;
            rectX += rectW;
            rectY = HEIGHT;
            pnl.add(new Rectangle(value, rectW, rectH, rectX, HEIGHT));
        }
    }
    
    public static void main(String[] args) {
        new test2();
    }
}
