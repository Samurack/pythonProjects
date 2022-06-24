;https://stackoverflow.com/questions/62614287/how-to-create-three-key-combination-hotkey-using-autohotkey

::rd::cd C:/repositories {Enter}

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
v & s::
RunWait, C:\Users\elderrollins\AppData\Local\Programs\Microsoft VS Code\Code.exe
return 

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
d & v::
Run, https://dev.azure.com/churchofjesuschrist
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
Run, https://mail.google.com/mail/u/0/#inbox
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
s & t::
Run, https://mail.google.com/mail/u/0/#inbox
Run, https://jira.churchofjesuschrist.org/secure/RapidBoard.jspa?rapidView=3336&quickFilter=20180
Run, C:\Users\elderrollins\AppData\Roaming\Spotify\Spotify.exe
return

#If, GetKeyState("Numpad1") ;start of context sensitive hotkeys
b & k::
Run, https://www.cypruscu.com/
Run, https://www.chase.com/
Run, https://eastidahocu.org/
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