import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class TemperatureConverter extends JFrame {
	private JTextField field1 = new JTextField();
	private JTextField field2 = new JTextField();
	private JComboBox<String> combobox1 = new JComboBox<>(new String[] { "C", "F", "K" });
	private JComboBox<String> combobox2 = new JComboBox<>(new String[] { "C", "F", "K" });

	public TemperatureConverter() {
		setTitle("Temperature Converter");
		setSize(300, 200);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setLayout(new GridLayout(2, 2, 4, 4));

		add(field1);
		add(combobox1);
		add(field2);
		add(combobox2);
		field1.addKeyListener(new KeyListener() {
			public void keyPressed(KeyEvent e) {}
			public void keyReleased(KeyEvent e) {convertTemperature();}
			public void keyTyped(KeyEvent e) {}
		});
		combobox1.addActionListener(e -> convertTemperature());
		combobox2.addActionListener(e -> convertTemperature());
	}

	private void convertTemperature() {
		try {
			double value1 = Double.parseDouble(field1.getText());
			String unit1 = (String) combobox1.getSelectedItem();
			String unit2 = (String) combobox2.getSelectedItem();

			if (unit1.equals(unit2)) {
				field2.setText(String.valueOf(value1));
			} else if (unit1.equals("C")) {
				if (unit2.equals("F")) {
					field2.setText(String.valueOf(value1 * 9 / 5 + 32));
				} else {
					field2.setText(String.valueOf(value1 + 273.15));
				}
			} else if (unit1.equals("F")) {
				if (unit2.equals("C")) {
					field2.setText(String.valueOf((value1 - 32) * 5 / 9));
				} else {
					field2.setText(String.valueOf((value1 - 32) * 5 / 9 + 273.15));
				}
			} else {
				if (unit2.equals("C")) {
					field2.setText(String.valueOf(value1 - 273.15));
				} else {
					field2.setText(String.valueOf((value1 - 273.15) * 9 / 5 + 32));
				}
			}
		} catch (NumberFormatException e) {
			field2.setText("");
		}
	}

	public static void main(String[] args) {
		new TemperatureConverter().setVisible(true);
	}
}
