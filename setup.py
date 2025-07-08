from cx_Freeze import setup, Executable
import os


executables = [Executable("main.py")]

setup(
    name="MeteorRunner",
    version="1.0",
    description="Meteor Runner app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
