from cx_Freeze import setup, Executable

setup(
    name='SimpleCalc',
    version='1.0',
    description='Just a simple calculator without any special functions',
    executables = [Executable("SimpleCalc.py")]
    )
