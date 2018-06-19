#!/bin/env python
import gridpy as gp   
#------------------Give input here----------------
input_file = 'SSSSS.geo'
jet = [6]
lastjet = 6
jet_letter = ['0','0','0','L']
switch = 0

#--------------End of input section------------------

for jet_number in jet:
 if jet_number == 1:
  block = gp.blocksort(jet_number)
  original_file = input_file
  jet_dia = jet_letter[0]

  print("--------------Replacing block near jet-1 area---------------------------")
  copy_file = gp.copyfile(jet_dia)
  gp.blockswap(jet_number,block,original_file,copy_file)
  switch = 1
  print("-------------Done--------------------------------------")


 elif jet_number == 2:
  block = gp.blocksort(jet_number)

  if switch ==0:
   original_file = input_file
  elif switch == 1:
   original_file = 'output_1'
  jet_dia = jet_letter[1]
  
  print ("--------------Replacing block near jet-2 area---------------------------")

  copy_file = gp.copyfile(jet_dia)
  gp.blockswap(jet_number,block,original_file,copy_file)
  switch = 2
  print ("-------------Done--------------------------------------")

 elif jet_number ==4 :
  block = gp.blocksort(jet_number)
  if switch ==0:
   original_file = input_file
  elif switch == 1:
   original_file = 'output_1'
  elif switch == 2:
   original_file = 'output_2'
  jet_dia = jet_letter[2]
  
  print ("--------------Replacing block near jet-4 area---------------------------")

  copy_file = gp.copyfile(jet_dia)
  gp.blockswap(jet_number,block,original_file,copy_file)
  switch = 4
  print ("-------------Done--------------------------------------")

 elif jet_number ==6:
  block = gp.blocksort(jet_number)
  if switch ==0:
   original_file = input_file
  elif switch == 1:
   original_file = 'output_1'
  elif switch == 2:
   original_file = 'output_2'
  elif switch == 4:
   original_file = 'output_4'
  jet_dia = jet_letter[3]
  
  print ("--------------Replacing block near jet-6 area---------------------------")
  copy_file = gp.copyfile(jet_dia)
  gp.blockswap(jet_number,block,original_file,copy_file)
  switch = 6
  print ("-------------Done--------------------------------------")

 else:
  print("you have given a wrong input")

jetcount = 0
for jet in jet:
 if jet != 0:
  jetcount = jetcount + 1
  source_block,target_block,source_plane,target_plane,a1,a2,d =gp.face_mapp_blocks(jet)
  for k in range(len(source_block)):

#The source block ################################

   if k ==0 and jetcount ==1:
    if lastjet   ==1:
     file_name ="output_1"
    elif lastjet   ==2:
     file_name ="output_2" 
    elif lastjet ==4:
     file_name ="output_4"
    elif lastjet ==6:
     file_name ="output_6"
   else :
    file_name = "file_input.geo"

   x,y,z,nx,ny,nz = gp.face_grid(file_name,source_block[k])
   print (source_block[0])
   nx = nx+1
   ny = ny+1
   nz = nz+1
   face =  gp.face_nodes(source_plane[k],nx,ny,nz)
 
 
   x_f_0 = []
   y_f_0 = []
   z_f_0 = []
 
   for elements in face:
     x_f_0.append(x[elements-1])
     y_f_0.append(y[elements-1])
     z_f_0.append(z[elements-1])

   coord_0 = [x_f_0, y_f_0, z_f_0]
   print ("------------Identified the source plane-----------")

#The target block#############################

   x,y,z,nx,ny,nz= gp.face_grid(file_name,target_block[k])
   nx = nx+1
   ny = ny+1
   nz = nz+1
   face =  gp.face_nodes(target_plane[k],nx,ny,nz)
 
   x_f_1 = []
   y_f_1 = []
   z_f_1 = []

   face = gp.indices_swap(face,nx,ny,nz,target_plane[k],a1[k],a2[k],d[k])




# to find tag for the mapping of the overlapping faces 
   mapping = []
   face_sorted = sorted(face)
   for i in range(0,len(face_sorted)):
    for j in range(0,len(face)):
     if face[j]== face_sorted[i]:
      mapping.append(j+1)

   print ("---------Identified the target plane and its connectivity----------")
  
 

   for elements in face:
     x_f_1.append(x[elements-1])
     y_f_1.append(y[elements-1])
     z_f_1.append(z[elements-1])

   x_count = 0
   y_count = 0
   z_count = 0
 
 
  
# Comparison of the coordinates of the overalapping faces 

 #for i in range(0,len(face)):

  #if abs(float(x_f_1[i])-float(x_f_0[i]))==0:
    #x_count = x_count +1 
  #if abs(float(y_f_1[i])-float(y_f_0[i]))==0:
    #y_count = y_count +1
  #if abs(float(z_f_1[i])-float(z_f_0[i]))==0:
    #z_count = z_count +1
 
 
 #print len(face),x_count,y_count,z_count
 
   print (k)
# Replacing the target file face corrdinates 
   gp.write_coord(coord_0,mapping,target_block[k],face_sorted,file_name)


                              
