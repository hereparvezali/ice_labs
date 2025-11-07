class YieldThread extends Thread {
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println("YieldThread: " + i);
			Thread.yield(); // Suggests that the current thread be paused to let others execute
		}
		System.out.println("YieldThread finished");
	}
}
class SleepThread extends Thread {
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println("SleepThread: " + i);
			try {
				Thread.sleep(1000); // Sleeps for 1 second
			} catch (InterruptedException e) {
				System.out.println("SleepThread interrupted");
			}
		}
		System.out.println("SleepThread finished");
	}
}
class StopThread extends Thread {
	public void run() {
		int i = 0;
		while (true) {
			System.out.println("StopThread running: " + i++);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				System.out.println("StopThread interrupted");
			}
		}
	}
}
public class YieldSleepStop {
	@SuppressWarnings("deprecation")
	public static void main(String[] args) {
		System.out.println(System.getProperty("java.version"));
		YieldThread yt = new YieldThread();
		SleepThread st = new SleepThread();
		StopThread stopT = new StopThread();
		yt.start();
		st.start();
		stopT.start();
		try {
			Thread.sleep(3000); // Let StopThread run for 3 seconds
		} catch (InterruptedException e) {
			System.out.println("Main thread interrupted");
		}
		System.out.println("Stopping StopThread (deprecated)");
		stopT.stop(); // Deprecated, unsafe in real applications
	}
}
