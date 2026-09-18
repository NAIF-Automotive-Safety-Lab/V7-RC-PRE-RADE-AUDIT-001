import cadquery as cq
from cadquery import exporters
from pathlib import Path
import json, hashlib, math

OUT=Path(r'/mnt/data/V7_ENGINEERING_BASELINE_R2_EXECUTED')

def box(l,w,h,center=True):
    return cq.Workplane('XY').box(l,w,h,centered=(center,center,False))

def cyl(r,h,axis='Z'):
    wp=cq.Workplane('XY').cylinder(h,r)
    if axis=='X': return wp.rotate((0,0,0),(0,1,0),90)
    if axis=='Y': return wp.rotate((0,0,0),(1,0,0),90)
    return wp

def translate(shape,x,y,z): return shape.translate((x,y,z))

def mk_part(name,shape,ref,material_status='TO_BE_CERTIFIED'):
    p=OUT/'CAD_STEP'/f'{name}.step'
    exporters.export(shape,str(p))
    return {'ref':ref,'name':name,'step':str(p.relative_to(OUT)),'material_status':material_status}

parts={}
# Coordinate system: X longitudinal, Y lateral, Z up. Seat centerline Y=0.
# V7 current baseline geometry is ENGINEERING_DEFINED; vehicle hardpoints are not claimed authoritative.
# 100 base: twin end plates + cross members
base = box(520,520,30).translate((0,0,0))
base=base.union(box(40,520,120).translate((-240,0,15)))
base=base.union(box(40,520,120).translate((240,0,15)))
for y in (-210,210): base=base.union(box(40,480,30).translate((0,y,30)))
parts['100']=mk_part('P100_BASE',base,'100')

# Rails 110L/R along X
for ref,y in [('110L',-210),('110R',210)]:
    rail=box(420,38,42).translate((0,y,105))
    # elevated guide beam
    rail=rail.union(box(420,24,28).translate((0,y,145)))
    parts[ref]=mk_part(f'P{ref}_RAIL',rail,ref)

# Carriage 120 spans rails, with guide blocks
car=box(470,460,28).translate((0,0,175))
for y in (-210,210): car=car.union(box(55,60,40).translate((0,y,205)))
parts['120']=mk_part('P120_CARRIAGE',car,'120')

# Absorber cartridges 130L/R aligned X
for side,y in [('L',-180),('R',180)]:
    a=box(260,44,44).translate((0,y,220))
    a=a.union(cyl(22,60,'X').translate((-120,y,242)))
    parts[f'130{side}']=mk_part(f'P130{side}_ABSORBER',a,f'130{side}')

# Pelvic control 140
pan=box(420,430,22).translate((0,0,208))
pan=pan.union(box(420,35,45).translate((165,-180,215))).union(box(420,35,45).translate((165,180,215)))
parts['140']=mk_part('P140_PELVIC_CONTROL',pan,'140')

# Seatback frame 160: uprights and cross member
back=box(32,50,620).translate((-185,-205,225)).union(box(32,50,620).translate((-185,205,225)))
back=back.union(box(32,410,50).translate((-185,0,235)))
back=back.union(box(32,410,50).translate((-185,0,820)))
parts['160']=mk_part('P160_SEATBACK_FRAME',back,'160')

# Rotation control links 150L/R, pinned bars
for side,y in [('L',-205),('R',205)]:
    link=box(30,24,300).translate((-145,y,370)).rotate((-145,y,370),(-145,y+1,370),-12 if side=='L' else 12)
    link=link.union(cyl(14,24,'Y').translate((-145,y-12 if side=='L' else y+12,370)))
    parts[f'150{side}']=mk_part(f'P150{side}_ROTATION_LINK',link,f'150{side}')

# Hinge set J: left/right hinge barrels along Y
hinge=cyl(18,50,'Y').translate((-185,-235,270)).union(cyl(18,50,'Y').translate((-185,185,270)))
parts['J']=mk_part('PJ_HINGE_PIVOT',hinge,'J')

# Lock 170 housing + pawl capture geometry, real solids
lock=box(90,60,45).translate((-80,0,320))
lock=lock.union(cyl(12,60,'Y').translate((-55,-30,342)))
lock=lock.union(box(18,54,18).translate((-55,0,345)))
parts['170']=mk_part('P170_LOCK170',lock,'170')

# Rebound 180: rear damper body
reb=box(180,50,50).translate((115,0,250)).union(cyl(18,70,'X').translate((25,0,275)))
parts['180']=mk_part('P180_REBOUND',reb,'180')

# Restraint interface 190: anchor blocks, conceptual/extension
rest=box(45,40,60).translate((120,-235,560)).union(box(45,40,60).translate((120,235,560)))
parts['190']=mk_part('P190_RESTRAINT_INTERFACES',rest,'190')

# Occupant guidance 200: curved-ish side guide blocks approximated by loft between profiles
wp1=cq.Workplane('YZ',origin=(-80,0,360)).rect(24,260)
wp2=cq.Workplane('YZ',origin=(40,0,470)).rect(24,320)
guide=wp1.workplane(offset=120).rect(24,320).loft(combine=True)
guide=guide.translate((0,-250,0)).union(guide.translate((0,250,0))) # V7-RC-002 CHANGE-001: resolve 130/200 hard interference; retain guidance function
parts['200']=mk_part('P200_OCCUPANT_GUIDANCE',guide,'200')

# Sensor interface 210: mounting plate + bosses
sens=box(100,80,8).translate((80,0,335))
for y in (-28,28): sens=sens.union(cyl(6,20,'Z').translate((110,y,343)))
parts['210']=mk_part('P210_SENSOR_INTERFACE',sens,'210')

# Assembly compound STEP
shapes=[]
for p in parts.values():
    s=cq.importers.importStep(str(OUT/p['step']))
    shapes.append(s)
assy_shape=cq.Compound.makeCompound([s.val() for s in shapes if hasattr(s,'val')])
assembly_step=OUT/'CAD_STEP'/'V7_ENGINEERING_RECONSTRUCTION_ASSEMBLY.step'
exporters.export(assy_shape,str(assembly_step))

# Source native CadQuery script copy is this file itself.
# Build basic parameter register.
params={
 'seat_width_mm':{'value':520,'status':'DESIGN_DEFINED','source':'V7 R0 concept reference'},
 'seat_pan_depth_mm':{'value':500,'status':'DESIGN_DEFINED','source':'V7 R0 concept reference'},
 'seatback_height_mm':{'value':650,'status':'DESIGN_DEFINED','source':'V7 R0 concept reference'},
 'rail_spacing_mm':{'value':420,'status':'DESIGN_DEFINED','source':'V7 R0 concept reference'},
 'ride_down_budget_mm':{'value':350,'status':'DESIGN_TARGET','source':'V7 R0 concept reference'},
 'capture_frame_width_mm':{'value':470,'status':'DESIGN_DEFINED','source':'V7 R0 concept reference'},
 'rail_travel_current_baseline_mm':{'value':180,'status':'DESIGN_TARGET','source':'V7 engineering definition; not measured'},
 'absorber_force_target_kN':{'value':'18–22','status':'DESIGN_TARGET','source':'V7 engineering definition; not measured'},
 'H_point_vehicle_authority':{'value':None,'status':'TO_BE_DEFINED','source':'vehicle-specific data absent'}
}
(OUT/'TRACEABILITY'/'V7_PARAMETER_REGISTER.json').write_text(json.dumps(params,indent=2),encoding='utf-8')

# Assembly manifest
asm={
 'revision':'V7-RC-001',
 'classification':'V7_ENGINEERING_RECONSTRUCTION / CONTROLLED_CURRENT_BASELINE',
 'historical_binary_master':False,
 'coordinate_system':{'origin':'bench fixture datum origin','X':'longitudinal forward','Y':'lateral right','Z':'up'},
 'parts':list(parts.values()),
 'assembly_step':str(assembly_step.relative_to(OUT)),
 'optional_extension':['140','190','200']
}
(OUT/'ASSEMBLY'/'V7_ASSEMBLY_MANIFEST.json').write_text(json.dumps(asm,indent=2),encoding='utf-8')

print('parts',len(parts),'assembly',assembly_step)
