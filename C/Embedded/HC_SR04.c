#include "embedded.h"
#include "HC_SR04.h"

/*
 * Initialiseer de in en output poorten en Timer 0
 */
void Ultrasoon_Init (void) {
	DDRB = (1 << DDB0) | (0 << DDB3);
	TCCR0A = 0x00;
	TCCR0B = 0x00;
}

/*
 * Return de maximale afstand constante
 */
uint16_t getMaximumDistance(void) {
	return MAX_DIS;
}

/*
 * Return de minimale afstand constante
 */
uint16_t getMinimumDistance(void) {
	return MIN_DIS;
}

/*
 * Meet de afstand met de ultrasoon sensor
 */
uint16_t Ultrasoon_Trigger(void) {
	
	// Stuur een 10 us pulse naar de trigger van de sensor
	PORTB &= ~(1 << PORTB0);
	_delay_us(10);
	PORTB |= (1 << PORTB0);
	_delay_us(10);
	PORTB &= ~(1 << PORTB0);
	
	// Zet de waarde van de timer naar 0
	TCNT0 = 0;
	
	// Wacht tot de echo high wordt, zet dan de timer aan met prescaler 1024
	while ((PINB & (1 << PINB3)) == 0) {}
	TCCR0B |= (1 << CS02) | (1 << CS00);
	
	// Wacht tot de echo low wordt, stop dan de timer
	while ((PINB & (1 << PINB3)) != 0 && TCNT0 < 200) {}
	TCCR0B &= ~((1 << CS02) | (1 << CS01) | (1 << CS00));
	
	// Return de waarde van de timer
	return TCNT0 * 58 / 64;
}