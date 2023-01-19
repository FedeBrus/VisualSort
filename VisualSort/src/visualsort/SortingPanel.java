package visualsort;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.*;

public class SortingPanel extends JPanel {
    private int WIDTH;
    private int HEIGHT;
    private int[] arr;
    
    public SortingPanel(int[] arr, int WIDTH, int HEIGHT) {       
        this.WIDTH = WIDTH;
        this.HEIGHT = HEIGHT;
        this.arr = new int[arr.length];       
        for(int i = 0; i < arr.length; i++) {
            this.arr[i] = arr[i];
        }
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.WHITE);
        int rX = 0, rY = HEIGHT;
        for(int i = 1; i <= arr.length; i++) {
            g.drawRect(rX, rY, WIDTH / arr.length, -((HEIGHT / (arr.length + 1)) * arr[i - 1]));
            g.fillRect(rX, rY, WIDTH / arr.length, -((HEIGHT / (arr.length + 1)) * arr[i - 1]));
            rX += WIDTH / arr.length;
        }
    }
}
