import mola
from mola import module_rhino



mesh = mola.construct_cone(0,100,100,20,10)
mola.sliceTriangle(mesh.vertices,10)

outTemp = module_rhino.display_mesh(mesh)
    
    

