import sys
sys.path.append("..")
from common.Publicon import obtenerConexion
from modelo.basePublibook import Usuario


def consultaUsuario():
	s=obtenerConexion()
	us=s.query(Usuario).first()
	print (us.nombre) 

consultaUsuario()