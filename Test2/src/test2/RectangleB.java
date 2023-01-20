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
    
    private int frameW;
    private int frameH;
    
    public RectangleB(int value, int pos, int unit, int frameW, int frameH) {
        this.unit = unit;
        this.value = value;
        this.pos = pos;
        this.frameW = frameW;
        this.frameH = frameH;
        rectW = unit;
        rectH = (unit * value);
        x = unit * pos;
        y = (frameH - rectH);
        
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawRect(x, y, rectW, rectH);
        this.setBackground(pos%2==0?Color.black:Color.white);
    }
    
    public void E_come_il_debug_ma_non_e_il_debug() {
        System.out.println("------------------------\n" 
                    + "\tUnit: " + unit + "\n"
                    + "Value: " + value + "\tPosition: " + pos + "\n" 
                    + "RectW: " + rectW + "\tRectH: " + rectH + "\n"
                    + "X: " + x + "\t\tY: " + (y+37) + "\n");
    }

//    public int getX() {
//        return x;
//    }
    
    public int getY() {
        return y;
    }
    
    public int getWidth() {
        return rectW;
    }

    public int getHeight() {
        return rectH;
    }
}