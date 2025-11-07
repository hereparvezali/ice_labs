void InitMain() {
     trisb = 0x00;
     portb = 0x00;
     trisc = 0x00;
     portc = 0x00;
     trisd = 0xff;
     portd = 0x00;
}
int ii=5,jj=5,i=0,j=0;
void main() {
     InitMain();
     while (1) {
           if(portd.B0){
                        while(portd.b0);
                        ii+=ii+1>10?0:1;
                        jj-=jj-1<0?0:1;
           }
           if(portd.B1){
                        while(portd.b1);
                        ii-=ii-1<0?0:1;
                        jj+=jj+1>10?0:1;
           }
           portb=0b01;
           for(i=0;i<ii;i++) delay_ms(1);
           portb=0b00;
           for(j=0;j<jj;j++) delay_ms(1);
     }
}