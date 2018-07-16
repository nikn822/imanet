#include "socket.h"
 
 
#define TM_BUF_SIZE 1400
#define TM_PACKETS_TO_SEND 10
#define TM_DEST_ADDR “10.129.36.52”
#define TM_DEST_PORT 9999
 
char testBuffer[TM_BUF_SIZE];
char * errorStr;
 
int tcpClient(void)
{
    int testSocket;
    unsigned int counter;
    struct sockaddr_in destAddr;
    int errorCode;
    int sockOption;
    int returnVal;
 
    returnVal = 0;
    counter = 0;

/* Specify the address family */
    destAddr.sin_family = AF_INET;
/* Specify the destination port */
    destAddr.sin_port = htons(TM_DEST_PORT);
/* Specify the destination IP address */
    destAddr.sin_addr.s_addr = inet_addr(TM_DEST_ADDR);
 
/* Create a socket */
    testSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
/*
* Verify the socket was created correctly. If not, return
* immediately
*/
    if (testSocket == TM_SOCKET_ERROR)
    {
        returnVal = tfGetSocketError(testSocket);
        errorStr = tfStrError(returnVal);
        goto tcpClientEnd;
    }
 
/* Connect to the server */
    errorCode = connect(testSocket, &destAddr, sizeof(destAddr));
/* Verify that we connected correctly */
    if (errorCode < 0)
    {
        returnVal = tfGetSocketError(testSocket);
        errorStr = tfStrError(returnVal);
        goto tcpClientEnd;
    }
 
/* While we haven’t yet sent enough packets... */
    while (counter < TM_PACKETS_TO_SEND)
    {
/* Send another packet to the destination specified above */
        errorCode = send(testSocket,
                         testBuffer,
                         TM_BUF_SIZE,
                         0);
/*
* Check if there was an error while sending. If so, break from the
* loop
*/
        if (errorCode < 0)
        {
            returnVal = tfGetSocketError(testSocket);
            errorStr = tfStrError(returnVal);
            break;
        }
/* Increment the number of packets sent by 1 */
        counter++;
    }
 
tcpClientEnd:
/* Make sure we have a socket before closing it */
    if (testSocket != -1)
    {
/* Close the socket */
        tfClose(testSocket);
    }
 
    return(returnVal);
}