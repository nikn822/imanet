#include socket.h


#define TM_BUF_SIZE 1400
#define TM_DEST_PORT 9999
 
char testBuffer[TM_BUF_SIZE];
char * strError;
 
int tcpServer(void)
{
    int listenSocket;
    int newSocket;
    struct sockaddr_in sourceAddr;
    struct sockaddr_in destAddr;
    int errorCode;
    int addrLen;
    int returnVal;
 
    returnVal = 0;
 
/* Specify the address family */
    destAddr.sin_family = AF_INET;
/*
* Specify the dest port (this being the server, the destination
* port is the one we’ll bind to
*/
    destAddr.sin_port = htons(TM_DEST_PORT);
/*
* Specify the destination IP address (our IP address). Setting
* this value to 0 tells the stack that we don’t care what IP
* address we use - it should pick one. For systems with one IP
* address, this is the easiest approach.
*/
    destAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
 
/* Create a socket */
    listenSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
/* Make sure the socket was created successfully */
    if (listenSocket == TM_SOCKET_ERROR)
    {
        returnVal = tfGetSocketError(listenSocket);
        errorStr = tfStrError(returnVal);
        goto tcpServerEnd;
    }
 
/*
* Bind the socket to the port and address at which we wish to
* receive data
*/
    errorCode = bind(listenSocket, &destAddr, sizeof(destAddr));
/* Check for an error in bind */
    if (errorCode < 0)
    {
        returnVal = tfGetSocketError(listenSocket);
        errorStr = tfStrError(returnVal);
        goto tcpServerEnd;
    }
 
/* Set up the socket as a listening socket */
    errorCode = listen(listenSocket, 10);
/* Check for an error in listen */
    if (errorCode < 0)
    {
        returnVal = tfGetSocketError(listenSocket);
        errorStr = tfStrError(returnVal);
        goto tcpServerEnd;
    }
 
/* Do this forever... */
    while (1)
    {
/* Get the size of the sockaddr_in structure */
        addrLen = sizeof(sourceAddr);
/*
* Accept an incoming connection request. The address/port info for
* the connection’s source is stored in sourceAddr. The length of
* the data written to sourceAddr is stored in addrLen. The
* initial value of addrLen is checked to make sure too many
* bytes are not written to sourceAddr
*/
        newSocket = accept(listenSocket, &sourceAddr, &addrLen);
/* Check for an error in accept */
        if (newSocket < 0)
        {
            returnVal = tfGetSocketError(listenSocket);
            errorStr = tfStrError(returnVal);
            goto tcpServerEnd;
        }
 
/* Do this forever... */
        while (1)
        {
/* Receive data on the new socket created by accept */
            errorCode = recv(newSocket,
                             testBuffer,
                             TM_BUF_SIZE,
                             0);
/* Make sure there wasn’t an error */
            if (errorCode < 0)
            {
                tfClose(newSocket);
                returnVal = tfGetSocketError(newSocket);
                errorStr = tfStrError(returnVal);
                goto tcpServerEnd;
            }
/*
* Receiving 0 bytes of data means the connection has been closed.
* If this happens, close the new socket and break out of this
* (the inner) loop.
*/
            if (errorCode == 0)
            {
                tfClose(newSocket);
                break;
            }
        }
    }
 
tcpServerEnd:
/* Make sure there’s a socket there before closing it */
    if (listenSocket != -1);
    {
/* Close the listening socket */
        tfClose(listenSocket);
    }
 
    return(returnVal);
}