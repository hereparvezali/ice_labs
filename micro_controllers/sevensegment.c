
char arr[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};

void main() {
     int i=0;
     TRISB=0x00;
     PORTB=0x00;

     TRISC.f0=1;
     TRISC.f1=1;

     portc.f0=0;
     portc.f0=0;


     while(1){
              if(portc.f0 && i<9){
                          while(portc.f0) delay_ms(10);
                                      i++;
              }

              if(portc.f1 && i>0){
                          while(portc.f1) delay_ms(10);
                                      i--;
              }
              portb=arr[i];
//              delay_ms(100);
     }
}
