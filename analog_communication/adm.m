% Amplitude Modulation (AM) Example

% Parameters
carrier_frequency = 20; % Carrier frequency in Hertz
message_frequency = 5; % Message signal frequency in Hertz
amplitude_modulation_index = 0.5; % Modulation index (0 to 1)

% Time settings
duration = 1; % Duration of the signal in seconds
sampling_frequency = 5000; % Sampling frequency in Hertz

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
plot(t, am_signal);
title('Amplitude Modulated Signal');
xlabel('Time (s)');
ylabel('Amplitude');

[b, a] = butter(5, message_frequency*2/sampling_frequency,"low");

% Demodulate the AM signal using envelope detection
demodulated_envelope = abs(am_signal);

demodulated_signal = filtfilt(b, a, demodulated_envelope);
% demodulated_signal = demod(am_signal,carrier_frequency,sampling_frequency,"am");

% Plot the demodulated signal
subplot(3,1,3);
plot(t, demodulated_signal);
title('Demodulated Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');
