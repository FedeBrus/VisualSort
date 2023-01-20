package test2;

import java.awt.*;
import javax.swing.*;

public class test2 {
    JFrame frame = new JFrame("Grazie Dio");
    JPanel pnl = new JPanel();
    static int widthAdj = 14, heightAdj = 37;
    static int WIDTH = 500, HEIGHT = 500;
    int size = 250;
    
    public test2() throws InterruptedException {
        frame.setSize(WIDTH+widthAdj, HEIGHT + heightAdj);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(pnl);
        frame.setResizable(false);
        pnl.setBackground(Color.darkGray);
//-------------------------------------------------------------------------        
        pnl.setLayout(new GridLayout(1, size));
        int[] arr = new int[size];
        
        int i;
        for(i = 1; i <= size; i++)
            arr[i-1] = i;
        
        //Ordinamenti.shuffle(arr);
        
        int value;
        int unit = WIDTH/size;
        for(i = 0; i < size; i++) {
            value = arr[i];         
            RectangleB rect = new RectangleB(value, i, unit, WIDTH, HEIGHT);
            pnl.add(rect);
            rect.E_come_il_debug_ma_non_e_il_debug();
        }
        Thread.sleep(1);
        frame.setSize(WIDTH+1, HEIGHT+1);
        frame.setSize(WIDTH+widthAdj, HEIGHT+heightAdj);
    }
    
    public static void main(String[] args) throws InterruptedException {
        new test2();
    }
}
