import bpy, os

scene = bpy.context.scene
blenderpath = bpy.data.filepath
blnderfilename =  os.path.splitext(os.path.basename(bpy.data.filepath))[0]
dirpath = os.path.dirname(blenderpath)

# The directory you want to build.
filepath = os.path.join(dirpath,"img")
os.makedirs(filepath, exist_ok=True)

ext = scene.render.file_extension
rendername = blnderfilename+"_"

renderimg = [i for i in bpy.data.images if i.type == "RENDER_RESULT"][0]
# set first save slot
renderimg.render_slots.active_index = 0


for renderslot in renderimg.render_slots:
    # The file path and render name (slot number) are combined here.
    path = os.path.join(filepath, rendername+renderslot.name+ext)
    try :
        renderimg.save_render(path, scene=scene)
        print("saved",renderslot.name)
    except :
        print("Slot  is empty",renderslot.name)
    # Move to next slot
    renderimg.render_slots.active_index = renderimg.render_slots.active_index+1
