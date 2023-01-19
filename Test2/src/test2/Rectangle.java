package test2;

import java.awt.*;
import javax.swing.*;

public class Rectangle extends JPanel {
    
    private int value;
    private int width;
    private int height;
    
    private int x;
    private int y;
    public Rectangle(int value, int width, int height, int x, int y) {
        this.value = value;
        this.width = width;
        this.height = height;
        
        this.x = x;
        this.y = y;
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawRect(x, y, width, height);
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
}
