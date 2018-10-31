/*
 * HC_SR04.c
 *
 * Author: Gerard
 */ 

#include "embedded.h"
#include "HC_SR04.h"

uint8_t min_dis = 6;
uint8_t max_dis = 160;

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
uint8_t getMaximumDistance(void) {
	return max_dis;
}

/*
 * Return de minimale afstand constante
 */
uint8_t getMinimumDistance(void) {
	return min_dis;
}

/*
 * Set de maximale afstand constante
 */
void setMaximumDistance(uint8_t dis) {
	max_dis = dis;
}

/*
 * Set de minimale afstand constante
 */
void setMinimumDistance(uint8_t dis) {
	min_dis = dis;
}

/*
 * Meet de afstand met de ultrasoon sensor
 */
uint8_t Ultrasoon_Trigger(void) {
	
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