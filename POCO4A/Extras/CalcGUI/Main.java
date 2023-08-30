package POCO4A.Extras.CalcGUI;

import java.awt.Component;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
 
public class Main {
    public static void addComponentsToPane(Container pane) {
        pane.setLayout(null);
 
        //addATextDisplay("teste", pane);
        addANumPad(pane);

    }
    
    private static void addANumPad(Container container){
        JPanel numPad = new JPanel(new GridLayout(4, 4));
        addAButton("Button 1", numPad);
        addAButton("Button 2", numPad);
        addAButton("Button 3", numPad);
        addAButton("Long-Named Button 4", numPad);
        addAButton("5", numPad);
        container.add(numPad);
        
    }
    
    private static void addAButton(String text, Container container) {
        JButton button = new JButton(text);
        button.setSize(50, 50);
        //button.setAlignmentX(Component.CENTER_ALIGNMENT);
        container.add(button);
    }

    private static void addATextDisplay(String text, Container container){
        JTextField tf = new JTextField(text, 20);
        tf.setSize(250, 100);
        tf.setAlignmentX(Component.CENTER_ALIGNMENT);
        container.add(tf);
    }
 
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("CalcGUI");
        frame.setSize(400, 500);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 
        //Set up the content pane.
        addComponentsToPane(frame.getContentPane());
 
        //Display the window.
        //frame.pack();
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
