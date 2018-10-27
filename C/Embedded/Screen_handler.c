/*
 * Screen_handler.c
 *
 * Created: 26-10-2018 15:41:33
 *  Author: justin
 */ 

#include "embedded.h"
#include "HC_SR04.h"

bool screen_state = false;
uint16_t temperature_trigger = 50;

// Initialiseer de poorten om de lampjes aan te sturen
void LED_init(){
	DDRD |= (1 << PORTD5) |(1 << PORTD6) |(1 << PORTD7);	//Zet poorten 6, 7 en 8 van PORTD als output poort
	set_led();	// Zet het juiste lampje aan om de status van het zonnescherm te weergeven
}

// Check of er aan de hand van de sensordata iets met het scherm gedaan moet worden
void handle_sensors(){
	uint16_t temperaturevalue = get_ADCValue();
	if(temperaturevalue < temperature_trigger && screen_state){
		screen_roll_in();
	}
	else if(temperaturevalue > temperature_trigger && !screen_state){
		screen_roll_out();
	}
}

/*	Zet de led aan die representeert in welke stand het scherm momenteel staat
*
*	Groen = Ingeklapt
*	Rood = Uitgeklapt
*/
void set_led(){
	if (screen_state){
		PORTD |= (1 << PORTD7);		// Zet poort D7 naar 1
		PORTD &= ~(1 << PORTD6);	// Zet poort D6 naar 0
	}else{
		PORTD |= (1 << PORTD6);		// Zet poort D6 naar 0
		PORTD &= ~(1 << PORTD7);	// Zet poort D7 naar 1
	}
}

// Rol het scherm in als het uitgeklapt is
void screen_roll_in(){
	screen_state = false;
	set_led();
	blink_led();
}

// Rol het scherm uit als het intgeklapt is
void screen_roll_out(){
	screen_state = true;
	set_led();
	blink_led();
}

// Knipper een geel lampje zolang het scherm bezig is met in- of uitrollen
void blink_led(){
	int temp = 0;
	int i = 0;
	while(temp < 10){
		SCH_Add_Task(reverse_led, i, 0);
		i += 250;
		temp++;
	}
}

// Zet het gele lampje aan als het uit is of uit als het aan is
void reverse_led(){
	PORTD ^= (1 << PORTD5);
}

/*	Return de status van het zonnescherm
*
*	false = ingeklapt	
*	true = uitgeklapt
*/
bool get_screenstate(){
	return screen_state;
}

/*	Zet de status van het zonnescherm
*
*	false = ingeklapt
*	true = uitgeklapt
*/
void set_screenstate(bool state){
	screen_state = state;
}