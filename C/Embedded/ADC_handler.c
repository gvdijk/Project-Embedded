/*
 * ADC_handler.c
 *
 * Created: 25-10-2018 17:33:22
 *  Author: justin
 */ 

#include "embedded.h"

// Configureer de ADC (Analog to Digital) unit op de arduino uno
void ADC_init(void){
	ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);	// ADC prescaler register instellen op 128x prescaler voor 125 KHz input
	ADCSRA |= (1 << ADATE);									// ADC van manual mode naar auto-trigger zetten
	ADCSRB |= (0 << ADTS0) | (0 << ADTS1) | (0 << ADTS2);	// ADC auto-trigger instellen op free-running mode (blijft oneindig meten)
	
	ADMUX |= (1 << REFS0);											// ADC referentie voltage zetten op het interne voltage van het bordje (5v)
	ADMUX |= (0 << MUX0) | (0 << MUX1) | (0 << MUX2) | (0 << MUX3);	// ADC poort A0 instellen als inputpoort
	
	ADCSRA |= (1 << ADEN);	// ADC unit aanzetten
	ADCSRA |= (1 << ADSC);	// ADC conversie starten
}

// Return de waarde van de lichtgevoelige sensor
uint16_t get_ADCValue(){
	return (ADCH << 8) + ADCL;
}