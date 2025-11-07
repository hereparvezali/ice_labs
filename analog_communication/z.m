% Example usage
fs = 44100; % Sampling frequency
t = 0:1/fs:1; % Time vector from 0 to 1 second
input_signal = sin(2 * pi * 1000 * t); % Example input signal (1000 Hz sine wave)

alpha = 0.97; % Pre-emphasis and de-emphasis coefficient

% Apply pre-emphasis
preemphasized_signal = [input_signal(1), input_signal(2:end) - alpha * input_signal(1:end-1)];

% Apply de-emphasis
deemphasized_signal = [preemphasized_signal(1), preemphasized_signal(2:end) + alpha * deemphasized_signal(1:end-1)];

% Plot the signals
figure;

subplot(3,1,1);
plot(t, input_signal);
title('Original Signal');

subplot(3,1,2);
plot(t, preemphasized_signal);
title('Pre-emphasized Signal');

subplot(3,1,3);
plot(t, deemphasized_signal);
title('De-emphasized Signal');
