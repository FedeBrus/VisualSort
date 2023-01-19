package visualsort;

import java.awt.*;
import javax.swing.*;

public class Rectangle extends JPanel {
    
    private int x;
    private int y;
    private int width;
    private int height;
    
    public Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        
        this.setSize(width, height);
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.WHITE);
        g.drawRect(x, y, width, height);
        g.fillRect(x, y, width, height);
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public void setHeight(int height) {
        this.height = height;
    }
}
