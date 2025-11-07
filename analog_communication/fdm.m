


% Frequency Modulation (FM) Example

% Parameters
cf = 20; % Carrier frequency in Hertz
mf = 2; % Message signal frequency in Hertz
mi = 5; % Modulation index

% Time settings
duration = 1; % Duration of the signal in seconds
sf = 5000; % Sampling frequency in Hertz

% Generate time vector
t = linspace(0, duration, duration * sf);

% Generate message signal (sine wave)
m = sin(2 * pi * mf * t);

% Generate phase deviation proportional to the message signal
c = sin(2*pi*cf*t);

% Generate frequency-modulated signal
fm = sin(2*pi*cf*t + mi .* m);

% Plot the signals
figure;

subplot(3, 1, 1);
plot(t, m);
title('Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(3, 1, 2);
plot(t, fm);
title('Frequency Modulated Signal');
xlabel('Time (s)');
ylabel('Amplitude');

[b,a]=butter(5,mf*2/500,"high");
recovered_m=filtfilt(b,a,fm);
[d,c]=butter(5,mf*3/500,"low");
re_m=filtfilt(d,c,recovered_m);
% Plot the original message signal and the recovered message signal
othoba = demod(fm,cf,sf,"fm");
subplot(3, 1, 3);
plot(t, othoba);
title('Recovered Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');

