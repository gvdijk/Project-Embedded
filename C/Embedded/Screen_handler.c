/*
 * Screen_handler.c
 *
 * Created: 26-10-2018 15:41:33
 * Author: Justin, Gerard
 */ 

#include "embedded.h"
#include "Screen_handler.h"
#include "HC_SR04.h"
#include "ADC_handler.h"
#include "Servo_handler.h"

typedef enum { retracted, rolling, extended, floating } state;

bool screen_stop = false;
bool auto_sensor = true;
state screen_state = extended;
uint16_t sensor_trigger = 300;
uint16_t sensor_margin = 25;
uint8_t led_indicator = 0;

// Initialiseer de poorten om de lampjes aan te sturen
void LED_init(void) {
	DDRD |= (1 << PORTD5) |(1 << PORTD6) |(1 << PORTD7);	//Zet poorten 6, 7 en 8 van PORTD als output poort
	set_led(true);	// Zet het juiste lampje aan om de status van het zonnescherm te weergeven
}

// Check of er aan de hand van de sensordata iets met het scherm gedaan moet worden
void handle_sensors(void) {
	if (auto_sensor) {
		uint16_t lightvalue = get_ADCValue();
		if(lightvalue < (sensor_trigger + sensor_margin)){
			if (screen_state == extended || screen_state == floating) {
				set_servoTarget(4800);
				screen_roll_in();
			}
		}
		else if(lightvalue > (sensor_trigger - sensor_margin)){
			if (screen_state == retracted || screen_state == floating) {
				set_servoTarget(3000);
				screen_roll_out();
			}
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
	screen_state = rolling;
	if (!screen_stop) {
		if (Ultrasoon_Trigger() > getMinimumDistance()) {
			if (led_indicator >= 25){
				status_led_toggle();
				led_indicator = 0;
			}
			led_indicator += 1;
			SCH_Add_Task(servo_rollIn, 0, 0);
			SCH_Add_Task(screen_roll_in, 10, 0);
		} else {
			status_led_off();
			screen_state = retracted;
			set_led(false);
		}
	} else {
		screen_stop = false;
		screen_state = floating;
		status_led_off();
	}
}

// Rol het scherm uit als het ingeklapt is
void screen_roll_out(void) {
	screen_state = rolling;
	set_led(true);
	if (!screen_stop) {
		if (Ultrasoon_Trigger() < getMaximumDistance()) {
			if (led_indicator >= 25){
				status_led_toggle();
				led_indicator = 0;
			}
			led_indicator += 1;
			SCH_Add_Task(servo_rollOut, 0, 0);
			SCH_Add_Task(screen_roll_out, 10, 0);
		} else {
			status_led_off();
			screen_state = extended;
		}
	} else {
		screen_stop = false;
		screen_state = floating;
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
*	false = ga door naar behoren
*	true = annuleer het bewegen van het scherm
*/
void set_stopstate(bool state) {
	screen_stop = state;
}

/*	Switch het automatische inklappen op basis van de sensor
*
*	Returned de nieuwe status
*/
bool toggle_auto_sensor(void) {
	auto_sensor = (auto_sensor == true) ? false : true;
	return auto_sensor;
}


/*	Zet de sensor threshold van de aangesloten sensor
*/
void set_sensor_threshold(uint16_t val) {
	sensor_trigger = val;
}

/*	Verkrijg de sensor threshold van de aangesloten sensor
*/
uint16_t get_sensor_threshold(void) {
	return sensor_trigger;
}