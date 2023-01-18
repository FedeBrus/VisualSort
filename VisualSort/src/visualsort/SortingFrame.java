package visualsort;

import java.awt.Color;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.WindowListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JSplitPane;

public class SortingFrame {
    
    private int WIDTH;
    private int HEIGHT;
    private int size;
    
    private int rectX;
    private int rectY;
    
    private JFrame main;
    private JSplitPane pnlMain;
    private JPanel pnlSorting;
    private JPanel pnlActions;
    
    private int[] arr;
    
    public SortingFrame(String algorithm, int size, WindowListener wl) {
        main = new JFrame(algorithm);
        pnlSorting = new JPanel();
        pnlActions = new JPanel();
        pnlMain = new JSplitPane();
        
        this.size = size;
        arr = new int[size];
        
        main.addWindowListener(wl);
        setup();
        setupArray();
    }
    
    public void setup() {
        //main.setBounds(500, 500, 1000, 500);
        //main.setVisible(true);

        //pnlMain = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, pnlSorting, pnlActions);
        //pnlMain.setDividerLocation(500);
        
        //pnlMain.setLeftComponent(pnlSorting);
        //pnlMain.setRightComponent(pnlActions);
        //pnlMain.setEnabled(false);
        
        //pnlSorting.setBackground(Color.BLACK);
        
        //main.add(pnlMain);
        //WIDTH = 500;
        //HEIGHT = 500;
        //rectX = WIDTH / size;
        //rectY = HEIGHT / size;
        //main.setBounds(500, 500, (rectX * size) + 500, (rectY * size) + 45);
    }
    
    public void setupArray() {
        //for(int i = 0; i < size; i++) {
        //    arr[i] = i;
        //}
        
        //System.out.println(rectX);
        //System.out.println(rectY);
        //int rX = 20, rY = 300;
        //pnlSorting.add(new Rectangle(rX, rY, rectX, -(rectY * 4)));
        
        //for(int i = 1; i <= size; i++) {
        //    pnlSorting.add(new Rectangle(rX, rY, rectX, -(rectY * i)));
        //    rX += rectX;
        //}
        
    }
}
