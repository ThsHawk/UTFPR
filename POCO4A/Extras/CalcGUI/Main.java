package POCO4A.Extras.CalcGUI;

import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
 
public class Main {
    public static void addComponentsToPane(Container pane) {
        pane.setLayout(new BoxLayout(pane, BoxLayout.PAGE_AXIS));
        addATextDisplay("teste", pane);
        addANumPad(pane);
    }
    
    private static void addANumPad(Container container){
        JPanel numPad = new JPanel(new GridLayout(4, 4));
        numPad.setMaximumSize(new Dimension(400, 400));
        addAButton("7", numPad);
        addAButton("8", numPad);
        addAButton("9", numPad);
        addAButton("+", numPad);
        addAButton("4", numPad);
        addAButton("5", numPad);
        addAButton("6", numPad);
        addAButton("-", numPad);
        addAButton("1", numPad);
        addAButton("2", numPad);
        addAButton("3", numPad);
        addAButton("/", numPad);
        addAButton("0", numPad);
        addAButton(",", numPad);
        addAButton("=", numPad);
        addAButton("*", numPad);
        container.add(numPad);  
    }
    
    private static void addAButton(String text, Container container) {
        JButton button = new JButton(text);
        container.add(button);
    }

    private static void addATextDisplay(String text, Container container){
        JLabel tf = new JLabel(text, JLabel.CENTER);
        tf.setFont(new Font("nome", Font.BOLD, 38));
        tf.setMaximumSize(new Dimension(400, 100));
        container.add(tf);
    }

    private static void createAndShowGUI() {
        //Create and set up the window.
        JFrame frame = new JFrame("CalcGUI");
        frame.setSize(400, 500);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 
        //Set up the content pane.
        addComponentsToPane(frame.getContentPane());
 
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
