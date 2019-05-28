from KryuGL import *

# Posicion de la Camara
eye = V3(1, 1, 5)
center = V3(0, 0, 0)
displace = V3(0, 1, 0)

# Llama las funciones para la escritura de la imagen .bmp
r = Bitmap(480, 480)
r.glViewPort(1, 1, 479, 479)
r.lookAt(eye, center, displace)

# Se elige un shader a utilizar en los modelos siguientes
r.shader = r.gouraud

# ---------- Cargar los modelos bmp con textura mtl ----------
# X-Wing
# Vista trasera
r.glLoad(
    './Modelos/x.obj',
    mtl='./Modelos/x.mtl',
    translate=(1,1,0),
    scale=(0.25,0.25,0.25),
    rotate=(0,0,0)
    )
    
r.glClearZbuffer()

# Vista Frontal
r.glLoad(
    './Modelos/x.obj',
    mtl='./Modelos/x.mtl',
    translate=(1,5,0),
    scale=(0.25,0.25,0.25),
    rotate=(1,0,0)
    )
    
r.glClearZbuffer()

# Vista de lado
r.glLoad(
    './Modelos/x.obj',
    mtl='./Modelos/x.mtl',
    translate=(4,1,0),
    scale=(0.25,0.25,0.25),
    rotate=(0,1,0)
    )
    
r.glClearZbuffer()

# Vista con angulo
r.glLoad(
    './Modelos/x.obj',
    mtl='./Modelos/x.mtl',
    translate=(4,4,0),
    scale=(0.25,0.25,0.25),
    rotate=(0,0,1)
    )
    
r.glClearZbuffer()
# ------------------------------------------------------------

# Creacion del Archivo
r.glFinish('StarMatrix.bmp')
