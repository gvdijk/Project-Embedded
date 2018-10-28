
void USART_Init(void);
void USART_Transmit_High(void);
void USART_Transmit_Low(void);
void USART_Transmit_Ready(void);
void USART_Receive(void);
void waitForReceive();

#define UBRRVAL 51