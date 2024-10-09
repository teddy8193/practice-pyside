build_linux:
	nuitka --enable-plugin=pyside6 --standalone --onefile --output-dir=bin simple_mvc/app.py

build_win:
	nuitka --enable-plugin=pyside6 --standalone --onefile --output-dir=bin --windows-console-mode=disable --assume-yes-for-downloads simple_mvc/app.py  