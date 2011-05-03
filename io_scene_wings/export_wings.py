import bpy
import struct, time, sys, os, zlib, io
import mathutils
from mathutils.geometry import tesselate_polygon

#token_byte = b'a'
#token_int32 = b'b'
#token_double_str = b'c'
#token_atom = b'd'
#token_tuple = b'h'
#token_array_end = b'j'
#token_string = b'k'
#token_array_start = b'l'
#token_map = b'm'

#def write_token(data,token_):
  #(token_type,token) = token_
  #data.write(token_type)
  #if token_type == token_byte:
    #data.write(struct.pack(">B"),token)
  #elif token_type == token_int32:
    #data.write(struct.pack(">L",token))
  #elif token_type == token_double_str:
    #pass
  #elif token_type == token_atom:
    #data.write(struct.pack(">H"),len(token))
    #data.write(token)
  #elif token_type == token_tuple:
    #write_tuple(data,token,strip=0)
  #elif token_type == token_array_end:
    #pass
  #elif token_type == token_string:
    #data.write(struct.pack(">H"),len(token))
    ##data.write() #convert to byte io
  #elif token_type == token_array_start:
    #write_array(data,token,write_key=0)
  #elif token_type == token_map:
    #data.write(struct.pack(">L",len(token)))
    #data.write(token)

#def write_array(data,token,fn=write_token,write_key=1)
  #if write_key > 0:
    #data.write(token_array_start)
  #data.write(struct.pack(">L",len(token)))
  #for i in range(len(token))
    #fn(data,token[i])
  #data.write(token_array_end)
  #return

#def write_tuple(data,token,write_key=1):
  #if write_key > 0: data.write(token_tuple)
  #data.write(struct.pack(">B",len(token)))
  #for i in range(len(token)): write_token(data,token[i])
  #return

#def write_color(data,color):
  #(r,g,b) = color
  #data.write(struct.pack(">BLfff",token_map,12,r,g,b))

#def write_texcoord(data,tex):
  #(u,v)= tex
  #data.write(struct.pack(">BLdd",token_map,16,u,v))

#def write_vertex(data,v)
  #(x,y,z) = v
  #data.write(struct.pack(">BLddd",token_map,24,x,z,-y))

  
def write(filename):
  #objects bpy
  pass