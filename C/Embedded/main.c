

#include "embedded.h"

void setup() {
	USART_Init();	// Initialiseer USART verbinding
	ADC_init();		// Initialiseer Analog to Digital conversie unit
	LED_init();		// Initialiseer de LEDS die het zonnescherm representeren
	
	SCH_Init_T1();
	SCH_Add_Task(waitForReceive, 100, 2);
	SCH_Add_Task(handle_sensors, 100, 2);
	SCH_Start();
}

int main() {
	setup();
	
	while (1) {
		SCH_Dispatch_Tasks();
	}
}
