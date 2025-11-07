void servoRotate0()        // 0 Degree
{
        unsigned int i;
        for(i=0;i<50;i++)
        {
            PORTB.F0=1;
            Delay_us(1300);      //1ms = 0 degree
            PORTB.F0=0;
            Delay_us(18700);
        }
}

void servoRotate90()           // 90 Degree
{
        unsigned int i,j;
        for(i=0;i<50;i++)
        {
            PORTB.F0=1;
            Delay_us(1495);     //1.5ms = 90 degree
            if(i==0);
            PORTB.F0=0;
            Delay_us(18500);
        }
}

void servoRotate180()             // 180 Degree
{
        unsigned int i;
        for(i=0;i<50;i++)
        {
            PORTB.F0=1;
            Delay_us(2200);      //2ms = 180 degree
            PORTB.F0=0;
            Delay_us(17800);
        }
}



void main() {

            TRISB=0;          // PortB as output port
           while(1){
                    servoRotate0();          // 0 Degree
                    Delay_ms(2000);

                    servoRotate90();          // 90 Degree
                    Delay_ms(2000);

                    servoRotate180();         // 180 Degree
                    Delay_ms(2000);


                    servoRotate90();         // 90 Degree
                    Delay_ms(2000);

            }
}