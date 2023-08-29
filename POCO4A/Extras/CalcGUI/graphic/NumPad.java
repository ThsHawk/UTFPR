package POCO4A.Extras.CalcGUI.graphic;

import javax.swing.*;
import java.awt.Color;

public class NumPad extends JPanel{

    public NumPad(){
        
        setSize(180, 180);
        //setOpaque(true);
        setBackground(new Color(255, 0, 0));
        //
        Button one = new Button("1");
        one.setSize(50, 50);
        Button two = new Button("2");
        Button three = new Button("3");
        Button four = new Button("4");
        Button five = new Button("5");
        //
        add(one);
        add(two);
        add(three);
        add(four);
        add(five);

    }
    
}
