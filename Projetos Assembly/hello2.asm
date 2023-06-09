; fonte: https://stackoverflow.com/questions/4568306/outputting-hello-world-in-masm-using-win32-functions

.386
.model flat, stdcall
option casemap: none

include \masm32\include\windows.inc
include \masm32\include\user32.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\user32.lib
includelib \masm32\lib\kernel32.lib

.data
    szCaption   db  'Hello', 0
    szText      db  'Hello, World!', 0

.code
    start:
            invoke MessageBox, NULL, offset szText, offset szCaption, MB_OK
            invoke ExitProcess, NULL        
    end start