% Phase Modulation (PM) Example

% Parameters
carrier_frequency = 50; % Carrier frequency in Hertz
message_frequency = 5; % Message signal frequency in Hertz
modulation_index = 5; % Modulation index

% Time settings
duration = 1; % Duration of the signal in seconds
sampling_frequency = 5000; % Sampling frequency in Hertz

% Generate time vector
t = linspace(0, duration, duration * sampling_frequency);

% Generate message signal (sine wave)
message_signal = sin(2 * pi * message_frequency * t);
carrier_signal = sin(2*pi*carrier_frequency*t);

% Generate phase modulation
pm_signal = sin(2 * pi * carrier_frequency * t + modulation_index * message_signal);

% Plot the signals
figure;

subplot(3, 1, 1);
plot(t, message_signal);
title('Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');
subplot(3, 1, 2);
plot(t, carrier_signal);
title('Carrier Signal');
xlabel('Time (s)');
ylabel('Amplitude');
subplot(3, 1, 3);
plot(t, pm_signal);
title('Phase Modulated Signal');
xlabel('Time (s)');
ylabel('Amplitude');

% Display the plot
sgtitle('Phase Modulation Example');
