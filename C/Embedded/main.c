

#include "embedded.h"

char result;
uint8_t value;


void setup() {
	DDRB = 0x01;	// Poort B als output poort instellen
	PORTB = 0x00;	// Schrijf 0 naar poort B
	USART_Init();	// Initialiseer USART verbinding
	ADC_init();		// Iinitialiseer Analog to Digital conversie unit
	
	SCH_Init_T1();
	SCH_Add_Task(waitForReceive, 100, 2);
	SCH_Start();
}

int main() {
	setup();
	
	while (1) {
		SCH_Dispatch_Tasks();
	}
}
