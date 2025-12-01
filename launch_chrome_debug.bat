@echo off
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=9222 ^
  --user-data-dir="C:\Users\himan\AppData\Local\Google\Chrome\User Data" ^
  --profile-directory="Profile 2" ^
  --no-first-run ^
  --no-default-browser-check
