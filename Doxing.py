#coded by Jey Zeta
import sys, os, webbrowser, platform, subprocess

import webbrowser

def __limpiar():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')
def menu():
	__limpiar()

	print """

\033[1;31m                                ____            _
\033[1;31m                               |  _ \  _____  _(_)_ __   __ _
\033[1;37m                               | | | |/ _ \ \/ / | '_ \ / _` |
\033[1;37m                               | |_| | (_) >  <| | | | | (_| |
\033[1;31m                               |____/ \___/_/\_\_|_| |_|\__, |
\033[1;31m                                                        |___/

					  \033[1;31mHacking Live\033[1;m
			  \033[1;34mHecho por:\033[1;m Victor Bancayan & Kelvin Parra
  				       \033[1;35mVersion: Beta 1.0
  				      
"""
	print '''
\033[1;32m 1. Pipl 	 \033[1;32m 7. Sis            \033[1;32m 13. Censo           \033[1;32m19. Sanciones   \033[1;32m 25. Direccion
\033[1;32m 2. Dni	 	 \033[1;32m 8. FecNac         \033[1;32m 14. EstadoDoc    \033[1;32m   20. Sat 	 \033[1;32m 26. SkypeIp
\033[1;32m 3. EstCiv    	 \033[1;32m 9. Credito       \033[1;32m  15. BuscarDatos  \033[1;32m   21. Runt  	 \033[1;32m 27. Multas
\033[1;32m 4. Operdora    \033[1;32m 10. Sentinel       \033[1;32m 16. Certificados   \033[1;32m 22. Libreta \033[1;32m     28. Username
\033[1;32m 5. Ruc       	\033[1;32m 11. ExifData       \033[1;32m 17. Licencia  	 \033[1;32m23. StalkScan  \033[1;32m  29. About
\033[1;32m 6. Tinfoleak   \033[1;32m 12. Acreditacion   \033[1;32m 18. Curp          \033[1;32m  24. Colegiados  \033[1;32m 30. Exit

		'''
	d = raw_input("\033[1;30m Doxing > ")

	if d == "1":
		webbrowser.open('https://pipl.com/')

		menu()
	elif d == "2":
		webbrowser.open('http://www.consultadni.info/')
		menu()
	elif d == "3":
		webbrowser.open('https://cel.reniec.gob.pe/valreg/valreg.do')
		menu()
	elif d == "4":
		webbrowser.open('http://www.deperu.com/celulares/')
		menu()
	elif d == "5":
		webbrowser.open('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias')
		menu()
	elif d == "6":
		webbrowser.open('https://tinfoleak.com/')
		menu()
	elif d == "7":
		webbrowser.open('http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx')
		menu()
	elif d == "8":
		webbrowser.open('https://www.reniec.gob.pe/concer/concer.do')
		menu()
	elif d == "9":
		webbrowser.open('https://www.icetex.gov.co/portalacces/tradicional/solicitar/cptConsultarEstado.asp?origen=portal')
		menu()
	elif d == "10":
		webbrowser.open('https://misentinel.sentinelperu.com/misentinel/misentinel.aspx')
		menu()
	elif d == "11":
		webbrowser.open('http://exifdata.com')
		menu()
	elif d == "12":
		webbrowser.open('http://ww4.essalud.gob.pe:7777/acredita/index.jsp')
		menu()
	elif d == "13":
		webbrowser.open('https://wsp.registraduria.gov.co/censo/_censoResultado.php')
		menu()
	elif d == "14":
		webbrowser.open('https://wsp.registraduria.gov.co/estadodocs/')
		menu()
	elif d == "15":
		webbrowser.open('http://buscardatos.com/')
		menu()
	elif d == "16":
		webbrowser.open('http://certificados.sena.edu.co/')
		menu()
	elif d == "17":
		webbrowser.open('http://web.mintransporte.gov.co/Consultas/transito/Consulta23122010.htm')
		menu()
	elif d == "18":
		webbrowser.open('https://consultas.curp.gob.mx/')
		menu()
	elif d == "19":
		webbrowser.open('https://consulta.simit.org.co/Simit/index.html')
		menu()
	elif d == "20":
		webbrowser.open('https://www.sat.gob.pe/Websitev9')
		menu()
	elif d == "21":
		webbrowser.open('https://www.runt.com.co/consultaCiudadana/#/consultaPersona')
		menu()
	elif d == "22":
		webbrowser.open('https://www.libretamilitar.mil.co/Modules/Consult/MilitarySituation')
		menu()
	elif d == "23":
		webbrowser.open('https://stalkscan.com/')
		menu()
	elif d == "24":
		webbrowser.open('http://www.cipica.com/buscolegiado/buscolegiado.php')
		menu()
	elif d == "25":
		webbrowser.open('http://www.midis.gob.pe/padron/')
		menu()
	elif d == "26":
		webbrowser.open('http://mostwantedhf.info/')
		menu()
	elif d == "27":
		webbrowser.open('http://aplicaciones007.jne.gob.pe/multas/')
		menu()
	elif d == "28":
		webbrowser.open('https://namechk.com/')
		menu()
	elif d == "29":
		webbrowser.open('https://www.facebook.com/HackingEnVivo/')
		menu()
	elif d == "30":
		sys.exit()

menu()
