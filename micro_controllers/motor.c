

void main() {
     trisb = 0x00;
     portb= 0x00;
     
     while(1){
              portb.f0=1;
              portb.f1=0;
              delay_ms(1000);
              
              portb.f0=0;
              portb.f1=0;
              delay_ms(500);
              
              portb.f0=0;
              portb.f1=1;
              delay_ms(1000);
              
              portb.f0=0;
              portb.f1=0;
              delay_ms(500);
     }
}