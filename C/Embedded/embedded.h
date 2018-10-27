#include "AVR_TTC_scheduler.h"

#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>
#define F_CPU 16E6
#include <util/delay.h>

typedef enum { false, true } bool;

// Function prototypes voor de Screen_handler
void LED_init();
void handle_sensors();
void set_led();
void screen_roll_in();
void screen_roll_out();
void blink_led();
bool get_screenstate();
void set_screenstate(bool state);

// Function prototypes voor de ADC_handler
void ADC_init(void);
uint8_t get_ADCValue();