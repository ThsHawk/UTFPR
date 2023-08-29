package POCO4A.Extras.CalcGUI.graphic;

import javax.swing.*;
import java.awt.event.*;

public class Button extends JButton{

    public Button(String l){
        JButton button = new JButton(l);
        button.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){  
                //tf.setText("Welcome to Javatpoint.");  
            }  
        });        
    }

}
