package POCO4A.Extras.CalcGUI;

import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.*;
import POCO4A.Extras.CalcGUI.graphic.*;       

public class Main {
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */

    private static String var;

    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("CalcGUI");
        frame.setLayout(new GridLayout(2, 1));
        frame.setSize(400, 500);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Separador
        JPanel display = new JPanel();
        display.setLayout(new BorderLayout(100, 100));
        display.setBackground(Color.RED);
        JTextField tf = new JTextField(var);
        tf.setSize(250, 70);
        display.add(tf, BorderLayout.CENTER);
        //teste label
        frame.add(display, BorderLayout.NORTH);
        
        
        //Add the button w/ "Hello" label.


        //frame.getContentPane().add(testButton1);
        //frame.getContentPane().add(tf, BorderLayout.LINE_START);

        //Display the window.
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}
