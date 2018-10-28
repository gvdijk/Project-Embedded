#include "embedded.h"
#include "USART.h"
#include "HC_SR04.h"

uint8_t incoming = 0;
uint8_t instruction = 0;
uint16_t value = 0;
uint16_t outgoing = 0;

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
 * Voer de schrijfinstructies uit
 */
void handleInstruction(void) {
	switch(instruction) {
		case 0xe1:
			// TODO: Pas de minimale afstand aan
			break;
		
		case 0xe2:
			// TODO: Pas de maximale afstand aan
			break;
		
		case 0xf1:
			// TODO: Pas de lichtintensiteit threshold aan
			break;
		
		case 0xf2:
			// TODO: Pas de temperatuur threshold aan
			break;
	}
	instruction = 0;
	value = 0;
	outgoing = 0xff;
	SCH_Add_Task(USART_Transmit_Low, 0, 0);
}

/*
 * Lees instructies
 * 0x81		Lees licht sensor
 * 0x82		Lees temperatuur sensor
 * 0x91		Lees afstand
 * 0x92		Lees constante MIN_DIS
 * 0x93		Lees constante MAX_DIS
 * 
 * Actie instrucites
 * 0xc1		Rol zonnescherm uit
 * 0xc2		Rol zonnescherm in
 * 0xc3		Stop in- of uitrollen
 * 0xc4		Toggle automatische bediening licht
 * 0xc5		Toggle automatische bediening temeratuur
 *
 * Schrijf instructies
 * 0xe1		Pas de minimale afstand aan
 * 0xe2		Pas de maximale afstand aan
 * 0xf1		Pas de lichtintensiteit threshold aan
 * 0xf2		Pas de temperatuur threshold aan
 */ 
void handleCommand(void) {
	if (instruction != 0) {
		if (value != 0) {
			value += (incoming << 8);
			handleInstruction();
		} else {
			value = incoming;
			if ((instruction >> 4) == 0xe) {
				handleInstruction();
			} else if ((instruction >> 4) == 0xf) {
				outgoing = 0xf0;
				SCH_Add_Task(USART_Transmit_Low, 0, 0);
			}
		}
	} else {
		if ((incoming >> 4) == 0xe || (incoming >> 4) == 0xf) {
			instruction = incoming;
			outgoing = 0xf0;
			SCH_Add_Task(USART_Transmit_Low, 0, 0);
		} else {
			switch(incoming) {
				case 0x81:
				outgoing = 0;
				break;
				
				case 0x82:
				outgoing = 0;
				break;
			
				case 0x91:
				outgoing = Ultrasoon_Trigger();
				break;
			
				case 0x92:
				outgoing = getMinimumDistance();
				break;
			
				case 0x93:
				outgoing = getMaximumDistance();
				break;
			
				case 0xc1:
				break;
			
				case 0xc2:
				break;
			
				case 0xc3:
				break;
				
				case 0xc4:
				break;
				
				case 0xc5:
				break;
			
				default:
				outgoing = 0xff;
				break;
			}
			if ((incoming >> 4) == 0x81 || (incoming >> 4) == 0x82) {
				SCH_Add_Task(USART_Transmit_High, 0, 0);
				SCH_Add_Task(USART_Transmit_Low, 1, 0);
			} else {
				SCH_Add_Task(USART_Transmit_Low, 0, 0);
			}
		}
	}
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
