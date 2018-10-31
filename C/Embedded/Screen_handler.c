/*
 * Screen_handler.c
 *
 * Created: 26-10-2018 15:41:33
 *  Author: justin
 */ 

#include "embedded.h"
#include "Screen_handler.h"
#include "HC_SR04.h"
#include "ADC_handler.h"

bool screen_stop = false;
bool auto_temp = false;
bool auto_light = false;
uint16_t temperature_trigger = 50;
uint16_t light_trigger = 0;

// Initialiseer de poorten om de lampjes aan te sturen
void LED_init(void) {
	DDRD |= (1 << PORTD5) |(1 << PORTD6) |(1 << PORTD7);	//Zet poorten 6, 7 en 8 van PORTD als output poort
	set_led(false);	// Zet het juiste lampje aan om de status van het zonnescherm te weergeven
}

// Check of er aan de hand van de sensordata iets met het scherm gedaan moet worden
void handle_sensors(void) {
	if (auto_temp) {
		uint16_t temperaturevalue = get_ADCValue();
		if(temperaturevalue < temperature_trigger + 1){
			screen_roll_in();
		}
		else if(temperaturevalue > temperature_trigger - 1){
			screen_roll_out();
		}
	}
}

/*	Zet de led aan die representeert in welke stand het scherm momenteel staat
*
*	Groen = Ingeklapt
*	Rood = Uitgeklapt
*/
void set_led(bool status) {
	if (status) {
		PORTD |= (1 << PORTD7);		// Zet poort D7 naar 1
		PORTD &= ~(1 << PORTD6);	// Zet poort D6 naar 0
	} else {
		PORTD |= (1 << PORTD6);		// Zet poort D6 naar 0
		PORTD &= ~(1 << PORTD7);	// Zet poort D7 naar 1
	}
}

// Rol het scherm in als het uitgeklapt is
void screen_roll_in(void) {
	if (!screen_stop) {
		if (Ultrasoon_Trigger() > getMinimumDistance()) {
			status_led_toggle();
			SCH_Add_Task(screen_roll_in, 250, 0);
		} else {
			status_led_off();
			set_led(false);
		}
	} else {
		screen_stop = false;
		status_led_off();
	}
}

// Rol het scherm uit als het ingeklapt is
void screen_roll_out(void) {
	set_led(true);
	if (!screen_stop) {
		if (Ultrasoon_Trigger() < getMaximumDistance()) {
			status_led_toggle();
			SCH_Add_Task(screen_roll_out, 250, 0);
		} else {
			status_led_off();
		}
	} else {
		screen_stop = false;
		status_led_off();
	}
}

// Zet het gele lampje aan als het uit is of uit als het aan is
void status_led_toggle(void) {
	PORTD ^= (1 << PORTD5);
}

// Zet het gele lampje aan als het uit is of uit als het aan is
void status_led_off(void) {
	PORTD &= ~(1 << PORTD5);
}

/*	Zet de status van de stop controlle
*
*	false = ingeklapt
*	true = uitgeklapt
*/
void set_stopstate(bool state) {
	screen_stop = state;
}

/*	Switch het automatische inklappen op basis van temperatuur
*
*	Returned de nieuwe status
*/
bool toggle_auto_temp(void) {
	auto_temp = (auto_temp == true) ? false : true;
	return auto_temp;
}

/*	Switch het automatische inklappen op basis van licht
*	
*	Returned de nieuwe status
*/
bool toggle_auto_light(void) {
	auto_light = (auto_light == true) ? false : true;
	return auto_light;
}


/*	Zet de temperatuur trigger
*/
void set_temperature(uint16_t val) {
	temperature_trigger = val;
}

/*	Zet de temperatuur trigger
*/
uint16_t get_temperature(void) {
	return temperature_trigger;
}


/*	Zet de temperatuur trigger
*/
void set_light(uint16_t val) {
	light_trigger = val;
}

/*	Zet de temperatuur trigger
*/
uint16_t get_light(void) {
	return light_trigger;
}