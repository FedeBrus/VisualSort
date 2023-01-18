package visualsort;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.border.*;

public class VisualSort {
    JFrame frame = new JFrame("Visual Sort");
    JPanel panel1 = new JPanel();
    JPanel panel2 = new JPanel();
    JPanel ptitle = new JPanel();
    JPanel bigp = new JPanel(new GridLayout(3, 1));
    JLabel lbl = new JLabel("Sorting Algorithm Type:          ");
    JLabel title = new JLabel("VISUAL SORT", SwingConstants.CENTER);
    JPanel psx = new JPanel(new GridLayout(2,1));
    JPanel pcx = new JPanel(new GridLayout(2,1));
    JPanel pdx = new JPanel(new GridLayout(2,1));
    JLabel cmps = new JLabel("Comparison Sorts", SwingConstants.CENTER);
    JLabel noncmps = new JLabel("Non-comparison Sorts", SwingConstants.CENTER);
    JLabel others = new JLabel("Others", SwingConstants.CENTER);
    JButton btn = new JButton("Okie dokie");
    
    String sorts[] = {"", "Comparison Sorts", "Non-comparison Sorts", "Others"};
    JComboBox cb0 = new JComboBox(sorts);
            
    String ComparisonSorts[] = {
        "Quicksort", "Merge Sort",
        "In-place Merge Sort", "Introsort",
        "Heapsort", "Insertion Sort",
        "Block Sort", "Timsort",
        "Selection Sort", "Cubesort",
        "Bubble Sort", "Exchange Sort",
        "Tree Sort", "Cycle Sort",
        "Library Sort", "Patience Sorting",
        "Smoothsort", "Tournament Sort",
        "Cocktail Shaker Sort", "Comb Sort",
        "Gnome Sort", "Odd-even Sort"
    };
    JComboBox cb1 = new JComboBox(ComparisonSorts);
    
    String Non_comparisonSorts[] = {
        "Pigeonhole Sort", "Bucker Sort (Uniform Keys)",
        "Bucket Sort (Integer Keys)", "Counting Sort",
        "LSD Radix Sort", "MSD Radix Sort",
        "MSD Radix Sort (In-place)", "Spreadsort",
        "Burstsort", "Flashsort",
        "Postman Sort"
    };
    JComboBox cb2 = new JComboBox(Non_comparisonSorts);
    
    String Others[] = {
        "Bead Sort", "Simple Pancake Sort",
        "I Can't Believe It Can Sort",
        "Spaghetti (Poll) Sort", "Sorting Network",
        "Bitonic Sorter", "Bogosort",
        "Stooge Sort", "SlowSort"
    };
    JComboBox cb3 = new JComboBox(Others);
    
    public void setup() {
        ptitle.add(title);
        ptitle.setBorder(new LineBorder(Color.DARK_GRAY, 6));
        ptitle.setBackground(Color.GRAY);
        title.setFont(new Font("Times New Roman", Font.BOLD, 30));
        frame.add(ptitle, BorderLayout.NORTH);
        
        bigp.add(panel1);
        bigp.add(panel2);
        bigp.add(btn);
        btn.setSize(10, 20);
        
        //frame.add(panel1);
        panel1.add(lbl);
        panel1.add(cb0);
        
        panel2.add(psx, BorderLayout.WEST);
        panel2.add(pcx, BorderLayout.CENTER);
        panel2.add(pdx, BorderLayout.EAST);
        
        psx.setBorder(new LineBorder(Color.LIGHT_GRAY,3, true));
        pcx.setBorder(new LineBorder(Color.LIGHT_GRAY,3, true));
        pdx.setBorder(new LineBorder(Color.LIGHT_GRAY,3, true));
        
        psx.add(cmps);
        psx.add(cb1);
        psx.setBackground(Color.gray);
        
        pcx.add(noncmps);
        pcx.add(cb2);
        pcx.setBackground(Color.gray);
        
        pdx.add(others);
        pdx.add(cb3);
        pdx.setBackground(Color.gray);
        
        frame.add(bigp);
        
        disableAll();
        setupActionListeners();
    }
    
    public void setupActionListeners() {
        cb0.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = cb0.getSelectedItem().toString();
                if(selected.equals("")) 
                    selection(0);
                else if(selected.equals("Comparison Sorts")) 
                    selection(1);
                else if(selected.equals("Non-comparison Sorts"))
                    selection(2);
                else if(selected.equals("Others"))
                    selection(3);
            }
        });
    }
    
    public void selection(int index) {
        disableAll();
        if(index != 0) {
            JComboBox cbEnable = index == 1 ? cb1 : index == 2 ? cb2 : cb3;
            JLabel lblEnable = index == 1 ? cmps : index == 2 ? noncmps : others;
            
            lblEnable.setBackground(Color.red);
            cbEnable.setEnabled(true);
        }
    }
    
    public void disableAll() {
        cb1.setEnabled(false);
            cmps.setBackground(Color.LIGHT_GRAY);
            cb2.setEnabled(false);
            noncmps.setBackground(Color.LIGHT_GRAY);
            cb3.setEnabled(false);
            others.setBackground(Color.LIGHT_GRAY);
            btn.setEnabled(false);
    }
    
    public VisualSort() {
        frame.setBounds(400, 200, 600, 300);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        
        setup();
    }
    
    public static void main(String[] args) {
        new VisualSort();
    }
}