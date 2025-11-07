% Amplitude Modulation (AM) Example

% Parameters
carrier_frequency = 50; % Carrier frequency in Hertz
message_frequency = 2; % Message signal frequency in Hertz
amplitude_modulation_index = .75; % Modulation index (0 to 1)

% Time settings
duration = 1; % Duration of the signal in seconds
sampling_frequency = 1000; % Sampling frequency in Hertz

% Generate time vector
t = linspace(0, duration, duration * sampling_frequency);

% Generate message signal (sine wave)
message_signal = sin(2 * pi * message_frequency * t);

% Generate carrier signal (sine wave)
carrier_signal = sin(2 * pi * carrier_frequency * t);

% Perform amplitude modulation
am_signal = (1 + amplitude_modulation_index * message_signal) .* carrier_signal;

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
plot(t, am_signal);
title('Amplitude Modulated Signal');
xlabel('Time (s)');
ylabel('Amplitude');

% Display the plot
sgtitle('Amplitude Modulation Example');

