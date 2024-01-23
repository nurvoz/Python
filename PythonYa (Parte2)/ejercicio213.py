'''
Codificaremos un programa mínimo que muestre una ventana con el mensaje "Hola Mundo" empleando el paquete wxPython
'''
# Importar la biblioteca wxPython
import wx

# Crear una instancia de la aplicación wxPython
aplicacion = wx.App()

# Crear una ventana (Frame) con el título "Hola Mundo"
ventana = wx.Frame(parent=None, title="Hola Mundo")

# Mostrar la ventana
ventana.Show()

# Iniciar el bucle principal de la aplicación wxPython
aplicacion.MainLoop()
