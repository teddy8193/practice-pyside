build_linux:
	nuitka --enable-plugin=pyside6 --standalone --onefile --follow-imports simple_mvc/app.py  