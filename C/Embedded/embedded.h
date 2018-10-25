#include "AVR_TTC_scheduler.h"

#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>
#define F_CPU 16E6
#include <util/delay.h>



void USART_Init(void);
void USART_Transmit(void);
void USART_Receive(void);
void Toggle_LED(void);
void waitForReceive();


#define UBRRVAL 51
#define MIN_DIS 6
#define MAX_DIS 160

