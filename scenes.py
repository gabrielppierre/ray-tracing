from plane import *
from sphere import *
from mesh import *
from material import *
from color import *
from environment import *
from light import *
from camera import *
import mesh_shapes as shape

# -- Cores ------------------------------------------------------------------------------------------------- #

White = Color(255, 255, 255)
Black = Color(0, 0, 0)
Red = Color(255, 0, 0)
Green = Color(0, 255, 0)
Blue = Color (0, 0, 255)
Gold = Color(249, 166, 2)
YellowGround = Color(180, 180, 19)
Ceu = Color(29, 155, 255)

# ---------------------------------------------------------------------------------------------------------- #
# -- Exemplo ----------------------------------------------------------------------------------------------- #
# Background:
back_color = Black

# Materiais:
ambient_coef = 0.1
plane_difusion = 0.6
plane_specular = 0.1
plane_roughness = 2
spheres_difusion = 0.55
spheres_specular = 0.1
spheres_roughness = 2

p_material = Material(color=YellowGround, ambient=ambient_coef, difusion=plane_difusion, specular=plane_specular, roughness=plane_roughness)
s_material_1 = Material(color=Red, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)
s_material_2 = Material(color=Green, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)
s_material_3 = Material(color=Blue, ambient=ambient_coef, difusion=spheres_difusion, specular=spheres_specular, roughness=spheres_roughness)

# Objetos
plane = Plane(point=Point(0, 0, 0), normal=Vector(0, 0, 1), material=p_material) 
sphere1 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_1)
sphere2 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_2)
sphere3 = Sphere(center=Point(0, 0, 0), radius=50, material=s_material_3)
objects_list = [sphere1, sphere2, sphere3, plane]

# Transformações:
sphere1.move(Vector(75, 0, 0))
sphere2.move(Vector(120, 110, 50))
sphere3.move(Vector(120, -110, 50))

# Luz:
l = Light(color=White, position=Point(15, -120, 120))
lights_list = [l]

# Camera:
c = Camera(position=Point(-55, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=70,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Black)

EXEMPLO = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #
# -- Casa -------------------------------------------------------------------------------------------------- #
# Background:
back_color = Ceu

# Materiais:
ambient_coef = 0.1
obj_difusion = 1
obj_specular = 0
obj_roughness = 1

cubo_material = Material(color=White, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)
teto_material = Material(color=Red, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)
chao_material = Material(color=Green, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)

# Objetos
cubo_v = shape.CUBE["vertices"]
cubo_t = shape.CUBE["triplas"]
cubo = Mesh(cubo_v, cubo_t, len(cubo_t), len(cubo_v), cubo_material)
teto_v = shape.ROOF["vertices"]
teto_t = shape.ROOF["triplas"]
teto = Mesh(teto_v, teto_t, len(teto_t), len(teto_v), teto_material)
chao = Plane(Point(0,0,0), Vector(0,0,1), chao_material, inf=False, distance=2500)
objects_list = [chao, cubo, teto]

# Transformações:
cubo.move(Vector(-0.5, 0.5, -0.5))
cubo.scale(Vector(50, 30, 30))
cubo.move(Vector(30, 0, 15))
teto.move(Vector(-0.5, 0.5, -0.3333333333333333))
teto.scale(Vector(55,35,16))
teto.move(Vector(30, 0, 34))
casa = [cubo, teto]
for o in casa:
    o.move(Vector(50,-90,0))
    o.rotate(-65, 2)

# Luz:
l = Light(color=White, position=Point(-2000, 1000, 4000))
lights_list = [l]

# Camera:
c = Camera(position=Point(-50, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=90,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Blue)

CASA = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #
# -- Teste ------------------------------------------------------------------------------------------------- #
# Background:
back_color = Black

# Materiais:
ambient_coef = 0.04
obj_difusion = 5
obj_difusion = 0.55
obj_specular = 0.1
obj_roughness = 2

obj_material = Material(color=White, ambient=ambient_coef, difusion=obj_difusion, specular=obj_specular, roughness=obj_roughness)

# Objetos
obj = Sphere(center=Point(0, 0, 0), radius=50, material=obj_material)
objects_list = [obj]

# Transformações:
obj.move(Vector(80, 0, 40))

# Luz:
l = Light(color=White, position=Point(-100, 100, 175))
lights_list = [l]

# Camera:
c = Camera(position=Point(-55, 0, 40), target=Point(0, 0, 40), screen_distance=50, fov_angle=90,
           resolution_height=450, resolution_width=600)

# Ambiente:
env = Environment(objects=objects_list, lights=lights_list, color=Blue)

TESTE = {"camera": c, "env" : env, "background" : back_color}

# ---------------------------------------------------------------------------------------------------------- #