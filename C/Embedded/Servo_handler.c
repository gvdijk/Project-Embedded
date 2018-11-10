/*
 * Servo_handler.c
 *
 * Created: 10-11-2018 16:40:07
 *  Author: justin
 */ 

#include "embedded.h"
#include "Servo_handler.h"

int servo_position = 3000;
int servo_target = 4800;
int servo_speed = 5;

void PWM_init(void){
	DDRB |= 1 << PINB1;										// Zet pin 9 op de arduino naar output
	TCCR1A |= (1 << WGM11) | (1 << COM1A1);					// Zet Fast PWM mode aan met de TOP op ICR1
	TCCR1B |= (1 << WGM12) | (1 << WGM13) | (1 << CS11);	// Zet prescaler mode op 8x
	ICR1 = 40000;											// Zet het ICR1 register op (1/16.000.000)*8*40000 = 20 ms interval
	OCR1A = 3000;											// Zet de servo naar de standaard beginpositie
}

void set_servoTarget(int target){
	servo_target = target;
}

void servo_rollOut(void){
	if (servo_position > servo_target){
		servo_position -= servo_speed;
		OCR1A = servo_position;
	}
}

void servo_rollIn(void){
	if (servo_position < servo_target){
		servo_position += servo_speed;
		OCR1A = servo_position;
	}
}