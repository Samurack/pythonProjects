;https://stackoverflow.com/questions/62614287/how-to-create-three-key-combination-hotkey-using-autohotkey

::rd::cd C:/repositories {Enter}

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
v & s::
RunWait, C:\xxxxx\xxxxx\AppData\Local\Programs\Microsoft VS Code\Code.exe
return 

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
g & t::
Run, https://github.com/
return 

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
y & u::
Run, https://www.youtube.com/
return 

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
g & m::
Run, https://mail.google.com
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
s & t::
Run, https://mail.google.com
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
c & m::
RunWait, cmd.exe
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
s & h::
Run, C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
w & d::
Run, C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE
return
