from cx_Freeze import setup,Executable

executables = [Executable("app.py")]

setup(
    name="my_python",
    version="0.1",
    description="python is backend",
    executables=executables
)
