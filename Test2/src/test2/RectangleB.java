package test2;

import java.awt.*;
import javax.swing.*;

public class RectangleB extends JPanel {
    private int value;
    private int pos;
     
    private int unit;
    private int x;
    private int y;
    private int rectW;
    private int rectH;
    
    public RectangleB(int value, int pos, int unit) {
        this.unit = unit;
        this.value = value;
        this.pos = pos++;
        rectW = unit;
        rectH = (unit * value);
        x = unit * pos;
        y = (HEIGHT + rectH);
        this.setBackground(pos%2==0?Color.yellow:Color.darkGray);
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawRect(x, y, rectW, rectH);
    }
    
    public void E_come_il_debug_ma_non_e_il_debug() {
        System.out.println("------------------------\n" 
                    + "\tUnit: " + unit + "\n"
                    + "Value: " + value + "\tPosition: " + pos + "\n" 
                    + "RectW: " + rectW + "\tRectH: " + rectH + "\n"
                    + "X: " + x + "\t\tY: " + y + "\n");
    }
    
    
//    Penso che servano i getX e getY per girare il grafico 
//    ma 0 voglia di pensarci, buona fortuna programmatori
//
//    public int getX() {
//        return x;
//    }
//    
//    public int getY() {
//        return y;
//    }
    
    public int getWidth() {
        return rectW;
    }

    public int getHeight() {
        return rectH;
    }
}