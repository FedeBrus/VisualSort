package test2;

import java.awt.*;
import javax.swing.*;

public class test2 {
    JFrame frame = new JFrame("Cane dio");
    JPanel pnl = new JPanel();
    public int WIDTHerror = 10, HEIGTHerror = 37;
    public int WIDTH = 504 + WIDTHerror, HEIGHT = 500 + HEIGTHerror;
    public int size = 500;
    
    public test2() throws InterruptedException {
        frame.setSize(WIDTH,HEIGHT);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(pnl);
        pnl.setBackground(Color.black);
//-------------------------------------------------------------------------        
        pnl.setLayout(new GridLayout(1, size)); //  <--------- sesso grande
        int value;
        int[] arr = new int[size];
        
        int i;
        for(i = 1; i <= size; i++)
            arr[i-1] = i;
        
        int rectX = 0, rectY, rectW, rectH;
        Ordinamenti.shuffle(arr);
        
        int unit = (WIDTH - WIDTHerror)/size;

        for(i = 0; i < size; i++) {
            value = arr[i];
            
            RectangleB rect = new RectangleB(value, i, unit);
            pnl.add(rect);
            rect.E_come_il_debug_ma_non_e_il_debug();


//            rectW = (WIDTH - WIDTHerror)/size;
//            rectH = (value*(HEIGHT-HEIGTHerror)/size);
//            rectX += rectW;
//            rectY = -HEIGHT + rectH;            
//            pnl.add(new Rectangle(value, rectW, rectH, rectX, rectY));
//            
//            System.out.println("------------------------\n"
//                    + "Value: " + value + "\n"
//                    + "RectW: " + rectW + "\tRectH: " + rectH + "\n"
//                    + "RectX: " + rectX + "\tRectY: " + rectY + "\n");
        }
        
        Thread.sleep(1000);
        frame.setSize(WIDTH+1, HEIGHT +1);
        frame.setSize(WIDTH, HEIGHT);
    }
    
    public static void main(String[] args) throws InterruptedException {
        new test2();
    }
}
