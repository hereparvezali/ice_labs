unsigned char letter[8] = {0x00, 0x3E, 0x09, 0x09, 0x3E, 0x00, 0x00, 0x00};

int i = 0;
int j = 0;


void main() {
    TRISB = 0x00;
    TRISD = 0x00;

    while (1) {
          for (i = 0; i < 8; i++) {
              PORTD = 1 << i;
              PORTB = letter[i];
              Delay_ms(2);
          }
    }
}
