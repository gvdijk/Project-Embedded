

#include "embedded.h"
#include "UART.h"
#include "HC_SR04.h"
#include "Screen_handler.h"
#include "ADC_handler.h"
#include "Servo_handler.h"

void setup() {
	Ultrasoon_Init();	// Initialiseer de ultrasoon sensor
	UART_Init();		// Initialiseer USART verbinding
	ADC_init();			// Initialiseer Analog to Digital conversie unit
	LED_init();			// Initialiseer de LEDS die het zonnescherm representeren
	PWM_init();			// Initialiseer de Pulse Width Modulation unit om de servo aan te sturen
	
	SCH_Init_T1();
	SCH_Add_Task(UART_Receive, 100, 2);
	SCH_Add_Task(handle_sensors, 1000, 1000);
	SCH_Start();
}

int main() {
	setup();
	
	while (1) {
		SCH_Dispatch_Tasks();
	}
}
