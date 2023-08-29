package POCO4A.Extras.CalcGUI;

import javax.swing.*;
import POCO4A.Extras.CalcGUI.graphic.*;       

public class Main {
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("CalcGUI");
        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Add the button w/ "Hello" label.
        Button one = new Button("1");

        //frame.getContentPane().add(testButton1);
        frame.setContentPane(one);

        //Display the window.
        frame.pack();
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
