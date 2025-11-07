void init(){
     trisb = 0x00;
     portb = 0x00;
     uart1_init(9600);
     adc_init();
}
unsigned int temp = 0;
unsigned char arr[8];
void main() {
     init();
     while(1){
              portb = 0x0f;
              temp = adc_read(0);
              inttostr(temp, arr);
              uart1_write_text(arr);
              uart1_write(13);
              delay_ms(500);
     }
}