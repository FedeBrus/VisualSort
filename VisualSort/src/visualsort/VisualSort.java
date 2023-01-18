package visualsort;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.*;

public class VisualSort {
    private JFrame menu;
    private JLabel title;
    private JPanel body;
    private JComboBox algorithms;
    private JComboBox sizes;
    private JButton start;
    
    private static String[] algorithmsNames = {"Bubble Sort", "Insertion Sort"};
    private static String[] sizesValues = {"10", "100", "250", "500"};
    
    public VisualSort() {
        menu = new JFrame("Visual Sort");
        title = new JLabel("Visual Sort", JLabel.CENTER);
        body = new JPanel();
        algorithms = new JComboBox(algorithmsNames);
        sizes = new JComboBox(sizesValues);
        start = new JButton("Start");
        
        setup();
    }
    
    public void setup() {
        menu.setBounds(500, 500, 500, 200);
        menu.setVisible(true);
        menu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        menu.setLayout(new GridLayout(2, 1));
        menu.add(title);
        menu.add(body);
        
        body.setLayout(new FlowLayout());
        body.add(algorithms);
        body.add(sizes);
        body.add(start);
    
        start.addActionListener((ActionEvent e) -> {
            algorithms.setEnabled(false);
            sizes.setEnabled(false);
            start.setEnabled(false);
            
            new SortingFrame(
                (String)algorithms.getSelectedItem(),
                Integer.parseInt((String)sizes.getSelectedItem()),
                new WindowAdapter() {
                    @Override
                    public void windowClosing(WindowEvent e) {
                        algorithms.setEnabled(true);
                        sizes.setEnabled(true);
                        start.setEnabled(true);
                    }
                }
            );
        });
    }
}
