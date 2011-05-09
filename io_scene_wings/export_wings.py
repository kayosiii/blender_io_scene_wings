import bpy
import struct, time, sys, os, zlib, io
import mathutils
from mathutils.geometry import tesselate_polygon

token_byte = b'a'
token_int32 = b'b'
token_double_str = b'c'
token_atom = b'd'
token_tuple = b'h'
token_array_end = b'j'
token_string = b'k'
token_array_start = b'l'
token_map = b'm'

def write_token(data,token,value):
  data.write(token)
  if token == value_byte:
    data.write(struct.pack(">B"),value)
  elif token == value_int32:
    data.write(struct.pack(">L",value))
  elif token == value_double_str:
    pass
  elif token == value_atom:
    data.write(struct.pack(">H"),len(value))
    data.write(value)
  elif token == value_tuple:
    write_tuple(data,value,strip=0)
  elif token == value_array_end:
    pass
  elif token == value_string:
    data.write(struct.pack(">H"),len(value))
    #data.write() #convert to byte io
  elif token == value_array_start:
    write_array(data,value,write_key=0)
  elif token == value_map:
    data.write(struct.pack(">L",len(value)))
    data.write(value)

def write_tuple_header(data,size):
  data.write(token_tuple);
  data.write(struct.pack(">B",size))
  
def write_array(data,token,fn=write_token,write_key=1)
  if write_key > 0:
    data.write(token_array_start)
  data.write(struct.pack(">L",len(token)))
  for i in range(len(token))
    fn(data,token[i])
  data.write(token_array_end)
  return

def write_tuple(data,token,write_key=1):
  if write_key > 0: data.write(token_tuple)
  data.write(struct.pack(">B",len(token)))
  for i in range(len(token)): write_token(data,token[i])
  return

#def write_color(data,color):
  #(r,g,b) = color
  #data.write(struct.pack(">BLfff",token_map,12,r,g,b))

#def write_texcoord(data,tex):
  #(u,v)= tex
  #data.write(struct.pack(">BLdd",token_map,16,u,v))

#def write_vertex(data,v)
  #(x,y,z) = v
  #data.write(struct.pack(">BLddd",token_map,24,x,z,-y))
def write_shape(ob,data):
  write_tuple_header(data,4)
  write_token(data,token_atom,b'object')
  #write_string(ob.name)
  write_tuple_header(data,5)
  write_token(data,token_atom,b'winged')
  print("object name: ",ob.name)
  
def save(operator, context, filepath):
  base_name, ext = os.path.split(filepath)
  context_name = [base_name,'','',ext]
  orig_scene = context.scene
  #if bpy.ops.oject.mode_set.poll():
    #bpy.ops.object.mode_set(mode='OBJECT')
  export_scenes = [orig_scene]

  for scene in export_scenes:
    orig_frame = scene.frame_current
  else:
    scene_frame = [orig_frame]

  objects = context.selected_objects
  #objects = scene.objects
  data = io.BytesIO()
  write_tuple_header(data,3)
  write_token(data,token_atom,b'wings')
  write_token(data,token_byte,2)
  write_tuple_header(data,3)
  
  
  for ob in objects: write_shape(ob,data)
  full_path = ''.join(context_name)
  #data = generate_data()
  data = data.getvalue()
  dsize = len(data)
  data = zlib.compress(data,6)
  fsize = len(data)+5
  header = b'#!WINGS-1.0\r\n\032\04'
  misc = 0x8350

  file = open(filepath, "wb")
  file.write(header)
  file.write(struct.pack(">L",fsize))
  file.write(struct.pack(">H",misc))
  file.write(struct.pack(">L",dsize))
  #file.write(data)

  file.close()
  return {'FINISHED'}