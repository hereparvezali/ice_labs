int main(){
    trisa = 0x00;
    porta = 0x00;
    
    while(1){
             porta=0xff;
             delay_ms(500);
             porta=0xff;
             delay_ms(500);
    }
}