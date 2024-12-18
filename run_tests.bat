@echo off
echo Installing required Python packages...
pip install -r requirements.txt

echo Running the VAPT API tests...
python Testcase/Test_Script.py
pause
