#include "embedded.h"
#include "USART.h"
#include "HC_SR04.h"

uint8_t incoming;
uint16_t outgoing;

/*
 * Initialiseer de USART communicatie
 */
void USART_Init(void) {
	// Zet de baud rate
	UBRR0H = (UBRRVAL >> 8);
	UBRR0L = (UBRRVAL & 0xFF);

	// Disable U2X
	UCSR0A = 0;

	// Zet de transmitter en receiver aan
	UCSR0B = (1 << TXEN0) | (1 << RXEN0);

	// Zet frame format: Async, 8 data bits, 1 stop bit, no parity
	UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

/*
 * Lees instructies
 * 0x81		Lees licht sensor
 * 0x82		Lees temperatuur sensor
 * 0x83		Lees afstand
 * 0x84		Lees constante MIN_DIS
 * 0x85		Lees constante MAX_DIS
 * 
 * Actie instrucites
 * 0x8b		Rol zonnescherm uit
 * 0x8c		Rol zonnescherm in
 * 0x8d		Stop in- of uitrollen
 */ 
void handleCommand() {
	switch(incoming) {
		case 0x81:
			outgoing = get_ADCValue();
			break;
			
		case 0x82:
			outgoing = 16;
			break;
			
		case 0x83:
			outgoing = Ultrasoon_Trigger();
			break;
			
		case 0x84:
			outgoing = getMinimumDistance();
			break;
			
		case 0x85:
			outgoing = getMaximumDistance();
			break;
				
		case 0x8b:
			break;
			
		case 0x8c:
			break;
			
		case 0x8d:
			break;
			
		default:
			outgoing = 0xff;
			break;
	}
	
	SCH_Add_Task(USART_Transmit_High, 0, 0);
	SCH_Add_Task(USART_Transmit_Low, 1, 0);
}

/*
 * Wacht op een lege transmit buffer, stuur dan de high byte
 */
void USART_Transmit_High(void) {
	while ( !(UCSR0A &  (1 << UDRE0)));
	UDR0 = (outgoing >> 8);
}

/*
 * Wacht op een lege transmit buffer, stuur dan de low byte
 */
void USART_Transmit_Low(void) {
	while ( !(UCSR0A &  (1 << UDRE0)));
	UDR0 = (outgoing & 0xff);
}

/*
 * Wacht op het ontvangen van data, zet het resultaat, en voeg de taak toe aan de scheduler
 */
void USART_Receive(void) {
	if (UCSR0A & (1 << RXC0)) {
		incoming = UDR0;
		SCH_Add_Task(handleCommand, 0, 0);
	}
}

<<<<<<< HEAD

void waitForReceive() {
	USART_Receive();
}
=======
>>>>>>> master

