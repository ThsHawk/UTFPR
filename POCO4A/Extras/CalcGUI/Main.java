package POCO4A.Extras.CalcGUI;

import javax.swing.*;

import java.awt.BorderLayout;
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
        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //teste label
        final JTextField tf = new JTextField(var);
        tf.setSize(100, 100);
        
        //Add the button w/ "Hello" label.
        
        NumPad np = new NumPad();


        //frame.getContentPane().add(testButton1);
        //frame.getContentPane().add(tf, BorderLayout.LINE_START);
        frame.getContentPane().add(np, BorderLayout.LINE_END);
        frame.setLayout(null);

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
