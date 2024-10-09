build_linux:
	nuitka --enable-plugin=pyside6 --standalone --onefile --follow-imports --output-dir=bin simple_mvc/app.py

build_win:
	nuitka --enable-plugin=pyside6 --standalone --onefile --follow-imports --output-dir=bin --windows-disable-console simple_mvc/app.py  