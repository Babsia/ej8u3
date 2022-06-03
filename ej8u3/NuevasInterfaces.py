from zope.interface import Interface
from zope.interface import implementer

class ITesorero (Interface):

   def gastosSueldoPorEmpleado(cuil):
       pass

 

class IDirector (Interface):
   def modificarBasico(cuil, nuevoBasico):
       pass

   def modificarPorcentajeporcargo(cuil, nuevoPorcentaje):
     pass

   def modificarPorcentajeporcategoría(cuil, nuevoPorcentaje):
       pass

def modificarImporteExtra(cuil, nuevoImporteExtra):
       pass