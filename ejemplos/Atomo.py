#!/usr/bin/env python


# -----------
# Clase atomo
# -----------
class atomo(object):
  def __init__(self,noat,x,y,z):
    self.noat = noat
    self.posicion = (x,y,z)
  def simbolo(self):
    NoAt_a_Simbolo = { 1: 'H', 2:'He', 3:'Li', 4:'Be',5:'B', 6:'C' } 
  # un metodo de la clase
    return NoAt_a_Simbolo[self.noat]
  def __repr__(self):
  # sobrecarga impresion
    return '%d %10.4f %10.4f %10.4f'%(self.noat, self.posicion[0], self.posicion[1],self.posicion[2])
  def __str__(self):
  # sobrecarga cadena
    return '%d %10.4f %10.4f %10.4f'%(self.noat, self.posicion[0], self.posicion[1],self.posicion[2])

# --------------
# Clase Molecula
# --------------
class molecula:
  def __init__(self,nombre='Generico'):
    self.nombre = nombre
    self.lista_atomo = []
  def agrega_atomo(self,atomo):
    self.lista_atomo.append(atomo)
  def __repr__(self):
    cadena  = 'Esta es una molecula llamada %s\n' % self.nombre
    cadena  = cadena +'Tiene %d atomos\n' % len(self.lista_atomo)
    for atomo in self.lista_atomo:
      cadena  = cadena + str(atomo) + '\n'
    return cadena

# --------------
# Clase QM_Molecula
# --------------
class qm_molecula(molecula):
  def __repr__(self):
    cadena = 'QM Rifa!\n'
    for atomo in self.lista_atomo:
      cadena = cadena + str(atomo) + '\n'
    return cadena

# --------------
# Clase QM2_Molecula
# --------------
class qm2_molecula(molecula):
  def __init__(self,nombre="Generico",base="6-31G**"):
    self.base = base
    molecula.__init__(self,nombre)

# -----    
# Main
# -----    
# Probando la clase atomo
print('Probando la clase atomo')
at = atomo(6,0.0,1.0,2.0)
print at
print at.simbolo()
print('\n')

print('probando la clase molecula')

mol = molecula('Agua')
at = atomo(8,0.,0.,0.)
mol.agrega_atomo(at)
mol.agrega_atomo(atomo(1,0.,0.,1.))
mol.agrega_atomo(atomo(1,0.,0.,0.))
print mol

# probando la clase qm_molecula
print('probando la clase qm_molecula')
mol = qm_molecula('Agua')
at = atomo(8,0.,0.,0.)
mol.agrega_atomo(at)
mol.agrega_atomo(atomo(1,0.,0.,1.))
mol.agrega_atomo(atomo(1,0.,0.,0.))
print mol

# probando la clase qm2_molecula
print('probando la clase qm2_molecula')
mol = qm2_molecula('Agua')
at = atomo(8,0.,0.,0.)
mol.agrega_atomo(at)
mol.agrega_atomo(atomo(1,0.,0.,1.))
mol.agrega_atomo(atomo(1,0.,0.,0.))
print mol
print mol.base

