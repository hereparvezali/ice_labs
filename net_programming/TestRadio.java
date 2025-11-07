import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TestRadio extends JFrame {
	ButtonGroup radios = new ButtonGroup();
	JCheckBox male_btn = new JCheckBox("male");
	JCheckBox female_btn = new JCheckBox("female");
	JColorChooser color = new JColorChooser();

	public TestRadio() {
		setSize(200, 200);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLayout(new FlowLayout());


		radios.add(male_btn);
		radios.add(female_btn);

		add(male_btn);
		add(female_btn);

		JButton checker = new JButton("Check");
		checker.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				System.out.println(male_btn.isSelected());
				System.out.println(female_btn.isSelected());
			}
		});
		add(checker);
		add(color);
	}

	public static void main(String[] args) {
		new TestRadio().setVisible(true);
	}
}
