char arr[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
 int i=2,j=3,k=4,l=5;
void main() {
     char mplx[]={0x0E,0x0D,0x0B,0x07};
     trisb=0x00;
     trisc=0x00;

     portb=0x00;
     portc=0xff;


     while(1){
              portc.f0=0;
              portb=arr[l];
              delay_ms(10);
              portc.f0=1;

              portc.f1=0;
              portb=arr[k];
              delay_ms(10);
              portc.f1=1;

              portc.f2=0;
              portb=arr[j];;
              delay_ms(10);
              portc.f2=1;

              portc.f3=0;
              portb=arr[i];
              delay_ms(10);
              portc.f3=1;
     }
}