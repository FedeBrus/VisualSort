package visualsort;

import java.awt.*;
import java.awt.event.WindowListener;
import javax.swing.*;


public class SortingFrame extends JFrame {
    
    private final int WIDTH = 800;
    private final int HEIGHT = 500;
    private int size;
    
    private JFrame main;
    private SortingPanel pnlSorting;
    private JPanel pnlActions;
    
    private int[] arr;
    
    public SortingFrame(String algorithm, int size, WindowListener wl) { 
        this.size = size;
        arr = new int[size];
        
        for(int i = 1; i <= size; i++) {
            arr[i - 1] = i;
        }
        
        main = new JFrame(algorithm);
        pnlSorting = new SortingPanel(arr, WIDTH, HEIGHT);
        System.out.println(pnlSorting);
        pnlActions = new JPanel();
        JButton btn1 = new JButton("1");
        JButton btn2 = new JButton("2");
        JButton btn3 = new JButton("3");
        JButton btn4 = new JButton("4");
        JButton btn5 = new JButton("5");
        JButton btn6 = new JButton("6");
        
        main.addWindowListener(wl);
        main.setBounds(300, 300, 900, 800);
        main.setLayout(new FlowLayout());
        main.setVisible(true);
        
        pnlSorting.setBackground(Color.BLACK);
        pnlSorting.setLayout(null);
        pnlSorting.setPreferredSize(new Dimension(WIDTH, HEIGHT));
       
        pnlActions.setLayout(new GridLayout(3, 2));
        pnlActions.setPreferredSize(new Dimension(WIDTH, 200));
        
        main.add(pnlSorting);
        main.add(pnlActions);
        pnlActions.add(btn1);
        pnlActions.add(btn2);
        pnlActions.add(btn3);
        pnlActions.add(btn4);
        pnlActions.add(btn5);
        pnlActions.add(btn6);
    }
}
