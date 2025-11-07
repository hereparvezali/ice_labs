class ControlledThread extends Thread {
	private boolean suspended = false;
	private boolean stopped = false;
	// Lock object for synchronization
	private final Object lock = new Object();
	public void run() {
		int count = 1;
		while (true) {
			synchronized (lock) {
				while (suspended) {
					try {
						lock.wait(); // Wait until resumed
					} catch (InterruptedException e) {
						System.out.println("Thread interrupted");
					}
				}
				if (stopped)
					break;
			}

			System.out.println("Running: " + count++);
			try {
				Thread.sleep(1000); // Simulate work
			} catch (InterruptedException e) {
				System.out.println("Thread interrupted during sleep");
			}
		}
		System.out.println("Thread stopped");
	}
	public void suspendThread() {
		synchronized (lock) {
			suspended = true;
		}
	}
	public void resumeThread() {
		synchronized (lock) {
			suspended = false;
			lock.notify();
		}
	}
	public void stopThread() {
		synchronized (lock) {
			stopped = true;
			suspended = false; // In case it's suspended, resume first
			lock.notify();
		}
	}
}
public class suspend {
	public static void main(String[] args) throws Exception {
		ControlledThread t = new ControlledThread();
		t.start();

		Thread.sleep(3000);
		System.out.println("Suspending thread...");
		t.suspendThread();

		Thread.sleep(3000);
		System.out.println("Resuming thread...");
		t.resumeThread();

		Thread.sleep(3000);
		System.out.println("Stopping thread...");
		t.stopThread();
	}
}
