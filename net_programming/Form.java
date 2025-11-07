import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import java.util.LinkedList;

class User {
	String name, email;
	int id, age;

	public User(int id, String name, String email, int age) {
		this.id = id;
		this.name = name;
		this.email = email;
		this.age = age;
	}
}

public class Form extends JFrame {
	Connection conn = null;
	JTextField name = new JTextField(10), email = new JTextField(10), age = new JTextField(5);
	JButton submit = new JButton("Submit"), update = new JButton("Update"), showall = new JButton("Show-All");
	JPanel form = new JPanel(), table = new JPanel();
	LinkedList<User> data = new LinkedList<>();

	public Form() throws SQLException {
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/formdb", "parvez", "mypass");
		setTitle("Form by Parvez");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(500, 400);
		setLayout(new BorderLayout(4, 4));

		form.setLayout(new GridLayout(5, 2, 4, 4));
		form.add(new JLabel("Name")); form.add(name);
		form.add(new JLabel("email")); form.add(email);
		form.add(new JLabel("age")); form.add(age);
		form.add(submit); form.add(update);
		form.add(showall);
		submit.addActionListener(e -> handleSubmit());
		showall.addActionListener(e -> handleShowAll());

		table.setLayout(new FlowLayout());

		add(form, BorderLayout.NORTH);
		add(table, BorderLayout.CENTER);
	}

	private void handleSubmit() {
		try {
			var stmt = conn.prepareStatement("insert into users (name, email, age) values (?, ?, ?)");
			stmt.setString(1, name.getText());
			stmt.setString(2, email.getText());
			stmt.setInt(3, Integer.parseInt(age.getText()));
			stmt.executeUpdate();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	private void handleShowAll() {
		try {
			data.clear();
			var stmt = conn.prepareStatement("select * from users");
			var rs = stmt.executeQuery();
			while (rs.next()) {
				data.add(new User(rs.getInt("id"), rs.getString("name"), rs.getString("email"), rs.getInt("age")));
			}
			table.removeAll();
			table.setLayout(new GridLayout(data.size(), 1, 4, 4));
			for (User user : data) {
				JPanel row = new JPanel(new FlowLayout());
				row.add(new JLabel(user.id + ""));
				row.add(new JLabel(user.name));
				row.add(new JLabel(user.email));
				row.add(new JLabel(user.age + ""));

				JButton deleteButton = new JButton("Delete");
				JButton updateButton = new JButton("Update");
				row.add(deleteButton);
				row.add(updateButton);

				deleteButton.addActionListener(ev -> {
					try {
						var deleteStmt = conn.prepareStatement("delete from users where id = ?");
						deleteStmt.setInt(1, user.id);
						deleteStmt.executeUpdate();
						handleShowAll();
					} catch (SQLException ex) {
						ex.printStackTrace();
					}
				});

				updateButton.addActionListener(ev -> {
					name.setText(user.name);
					email.setText(user.email);
					age.setText(String.valueOf(user.age));
					update.addActionListener(e -> {
						try {
							var updateStmt = conn
									.prepareStatement("update users set name = ?, email = ?, age = ? where id = ?");
							updateStmt.setString(1, name.getText());
							updateStmt.setString(2, email.getText());
							updateStmt.setInt(3, Integer.parseInt(age.getText()));
							updateStmt.setInt(4, user.id);
							updateStmt.executeUpdate();
							handleShowAll();
						} catch (SQLException ex) {
							ex.printStackTrace();
						}
					});
				});

				table.add(row);
			}
			table.revalidate();
			table.repaint();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws Exception {
		new Form().setVisible(true);
	}
}