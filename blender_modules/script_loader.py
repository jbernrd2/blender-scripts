# Path to scripts folder
path = "C:/Users/j_ber/root/blender_scripts/blender_modules/panels/"


# Names of python files to import
filenames = ["vertex_tools.py"]


for file in filenames:
    exec(compile(open(path + file).read(), path + file, 'exec'))



