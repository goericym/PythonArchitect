@echo off
for /R . %%F in (*.pyc *.spec *DiagnosticAssistantInstaller*.exe) DO del /Q %%F
for %%F in (logger.log) DO del /Q %%F
for /D %%F in (dist* build) DO rd /Q /S %%F
exit /b