@echo off
echo.
for %%f in (*.***) do (
    normalize -a 12dBFS "%%f"
)