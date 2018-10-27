

#include "embedded.h"
#include "USART.h"
#include "HC_SR04.h"

char result;


void setup() {
	Ultrasoon_Init();
	
	USART_Init();
	
	SCH_Init_T1();
	SCH_Add_Task(USART_Receive, 100, 2);
	SCH_Start();
}

int main() {
	setup();
	
	while (1) {
		SCH_Dispatch_Tasks();
	}
}
