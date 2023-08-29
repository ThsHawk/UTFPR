package POCO4A.Extras.CalcGUI.graphic;

import javax.swing.*;

public class Button {
    
    private String label;

    public Button(String l){
        this.label = l;
        JButton button = new JButton(this.label);

    }

}
