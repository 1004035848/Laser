print('This program create a SVG file for a square laser cutting box')#brief introduction
print('Please customized the box parameters')
def EnterSideLength():  ## This function ask for the desired length of each side
    while True:
        global a
        try:
            trya = float(input("enter the side length of the square box in mm(between 50 to 180 mm:"))
        except ValueError:  # ask for re-enter if input is not a number
            print('invalid input, please enter again')
            continue
        else:
            a = trya  # if the input is a number, assign it to a
            break
def EnterTslotLength(): #the length of the teeth
    while True:
        global b
        try:
            tryb = float(input("enter the length of teeth in mm(between 1/4 and 1/2 of the side length:"))
        except ValueError:  # ask for re-enter if input is not a number
            print('invalid input, please enter again')
            continue
        else:
            b = tryb  # if the input is a number, assign it to b
            break
def EnterBoltLength():
    while True:
        global c
        try:
            tryc = float(input("enter the length of bolt in inch:"))
        except ValueError:  # ask for re-enter if input is not a number
            print('invalid input, please enter again')
            continue
        else:
            c = tryc  # assign the value
            break
def EnterThickness():
    while True:
        global d
        try:
            tryd = float(input("enter material thickness in between 1-6 mm:"))
        except ValueError:  # ask for re-enter if input is not a number
            print('invalid input, please enter again')
            continue
        else:
            d = tryd  # assign the value
            break
def EnterFrontText():
    Text = input('enter up tp 25 characters for front face, or "N" to skip')
    if side_length < 100:
        Font = 6
        print('font is %i px'%Font)
    elif side_length >= 100:
        Font = 8
        print('font is %i px' % Font)
    if Text == "N":
        pass
    else:
        Textonfront = Text[0:24]
        x_coord = 15; y_coord = 15+1.7*side_length
        f.write('<text x="{0}" y="{1}"\n'.format(x_coord,y_coord))
        f.write('style="fill:#000000; stroke: #000000; font-size: %spx;">\n' %Font)
        f.write('%s\n' %Textonfront)
        f.write('</text>\n')

def EnterTopText():
    Text = input('enter up tp 15 characters for top face, or "N" to skip')
    if side_length < 100:
        Font = 10
    elif side_length >= 100:
        Font = 12
        print('font is %i px' % Font)
    if Text == "N":
        pass
    else:
        Textonfront = Text[0:14]
        x_coord = 25+2.3*side_length;
        y_coord = 5+0.45*side_length
        f.write('<text x="{0}" y="{1}"\n'.format(x_coord, y_coord))
        f.write('style="fill:#000000; stroke: #000000; font-size: %spx;">\n' % Font)
        f.write('%s\n' % Textonfront)
        f.write('</text>\n')

def ColumbiaLogo():
    choice = input('enter "A" for a Columbia capital letter C at the front surface, enter other keys to skip')
    if choice == 'A':
        x_coord = 5+0.4*side_length; y_coord = 15+1.3*side_length
        f.write('<text x="{0}" y="{1}"\n'.format(x_coord, y_coord))
        f.write('style="fill:None; stroke: #000000; font-size: %34px;">\n')
        f.write('C\n')
        f.write('</text>\n')
    else:
        pass

def Selectimages():
    choice = input('enter "A" for a Chevron pattern at the right surface, Enter other keys to skip')
    if choice == 'A':
        x1 = 15+1.2*side_length; y1 = 5+0.12*side_length;
        x2 = x1+0.12*side_length; y2 = y1+0.12*side_length;
        x3 = x2+0.12*side_length; y3 = y1;
        x4 = x3+0.12*side_length; y4 = y2;
        x5 = x4+0.12*side_length; y5 = y1;
        x6 = x5+0.12*side_length; y6 = y2;
        f.write('<path fill="none" stroke="red" d="M {0},{1} L {2},{3} L{4},{5} L{6},{7} L{8},{9} L{10},{11}"/>\n'.format(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6))
        yy1 = y1+0.2*side_length; yy2 = y2+0.2*side_length;  yy3 = yy1;  yy4 = yy2; yy5 = yy1; yy6 = yy2;
        f.write('<path fill="none" stroke="red" d="M {0},{1} L {2},{3} L{4},{5} L{6},{7} L{8},{9} L{10},{11}"/>\n'.format(x1,yy1,x2,yy2,x3,yy3,x4,yy4,x5,yy5,x6,yy6))
        yy1 = y1+0.2*side_length; yy2 = y2+0.2*side_length;  yy3 = yy1;  yy4 = yy2; yy5 = yy1; yy6 = yy2;
        f.write('<path fill="none" stroke="red" d="M {0},{1} L {2},{3} L{4},{5} L{6},{7} L{8},{9} L{10},{11}"/>\n'.format(x1,yy1,x2,yy2,x3,yy3,x4,yy4,x5,yy5,x6,yy6))
        yyy1 = yy1+0.2*side_length; yyy2 = yy2+0.2*side_length;  yyy3 = yyy1;  yyy4 = yyy2; yyy5 = yyy1; yyy6 = yyy2;
        f.write('<path fill="none" stroke="red" d="M {0},{1} L {2},{3} L{4},{5} L{6},{7} L{8},{9} L{10},{11}"/>\n'.format(x1,yyy1,x2,yyy2,x3,yyy3,x4,yyy4,x5,yyy5,x6,yyy6))
    else:
        pass

def SketchBackSurface():
    #coordinates for each points on the figure
    ax = 5; ay = 5; bx = 5+side_length; by = 5; cx = 5+side_length; cy = 5+side_length
    dx = 5; dy = 5+side_length; ex = 5+side_length; ey = 5+(side_length-slot_length)/2;
    fx = ex-thickness; fy=ey; gx = ex; gy = 5+(side_length+slot_length)/2; hx = fx; hy = gy;
    ix = 5+(side_length+slot_length)/2; iy = 5+side_length; jx = ix; jy = iy-thickness;
    lx = 5+(side_length-slot_length)/2; ly = iy; mx = lx; my = jy;
    nx = 5; ny = 5+(side_length+slot_length)/2; ox = nx+thickness; oy = ny;
    px = 5; py = 5+(side_length-slot_length)/2; qx = ox; qy = py;
    aax = fx; aay = 5+(side_length/2)-1.5; abx = aax-(bolt_length-3); aby = aay;
    acx = abx; acy = aby-1.5; adx = acx-2; ady =acy; aex = adx; aey = ady+6; afx = acx; afy = aey;
    agx = abx; agy = aby+3; ahx = aax; ahy = aay+3;
    bax = 5+(side_length/2)+1.5; bay = jy; bbx = bax; bby = bay-(bolt_length-3); bcx = bbx+1.5; bcy = bby;
    bdx = bcx; bdy = bcy-2; bex = bdx-6; bey = bdy; bfx = bex; bfy = bby; bgx = bbx-3; bgy = bfy; bhx = bgx; bhy = bay;
    cax = ox; cay = 5+(side_length/2)+1.5; cbx = cax+(bolt_length-3); cby = cay; ccx = cbx; ccy = cby+1.5;
    cdx = ccx+2; cdy = ccy; cex = cdx; cey = cdy-6; cfx = cbx; cfy = cey; cgx = cfx; cgy = cby-3; chx = cax; chy = cgy;
    #sketch in svg file
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} \n'.format(ax,ay,bx,by,ex,ey,fx,fy,aax,aay))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(abx,aby,acx,acy,adx,ady,aex,aey,afx,afy,agx,agy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ahx,ahy,hx,hy,gx,gy,cx,cy,ix,iy,jx,jy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bax,bay,bbx,bby,bcx,bcy,bdx,bdy,bex,bey,bfx,bfy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bgx,bgy,bhx,bhy,mx,my,lx,ly,dx,dy,nx,ny))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ox,oy,cax,cay,cbx,cby,ccx,ccy,cdx,cdy,cex,cey))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11}"\n'.format(cfx,cfy,cgx,cgy,chx,chy,qx,qy,px,py,ax,ay))
    f.write('stroke="black" stroke-width="1" fill="none" />\n')

def SketchRightSurface():
    #assign coordinates
    ax = 5+side_length+10+thickness; ay = 5; bx = ax+side_length-2*thickness; by = 5; cx = bx; cy = by+side_length; dx = ax; dy = cy;
    ex = bx; ey = by+(side_length-slot_length)/2; fx = ex+thickness; fy = ey; gx = fx; gy = by+(side_length+slot_length)/2;
    hx = ex; hy = gy; ix = dx+(side_length-2*thickness+slot_length)/2; iy = cy; jx = ix; jy = iy-thickness; kx = dx+(side_length-2*thickness-slot_length)/2;
    ky = jy; lx = kx; ly = iy; mx = ax; my =hy; nx = mx-thickness;ny = my; ox = nx; oy = ey; px = ax; py = oy;
    aax = fx; aay = 5+(side_length/2)-1.5; abx = aax-4; aby = aay; acx = abx; acy = aby+3; adx = aax; ady = acy;
    bax = ox+(side_length/2)+1.5; bay = jy; bbx = bax; bby = bay-(bolt_length-3); bcx = bbx+1.5; bcy = bby;
    bdx = bcx; bdy = bcy-2; bex = bdx-6; bey = bdy; bfx = bex; bfy = bcy; bgx = bfx+1.5; bgy = bfy; bhx=bgx; bhy =bay;
    cax = ox; cay = ay+(side_length/2)+1.5; cbx = cax+4; cby = cay; ccx = cbx; ccy = cby-3; cdx = cax; cdy = ccy;
    # sketch in svg file
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} \n'.format(ax,ay,bx,by,ex,ey,fx,fy,aax,aay))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(abx,aby,acx,acy,adx,ady,gx,gy,hx,hy,cx,cy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ix,iy,jx,jy,bax,bay,bbx,bby,bcx,bcy,bdx,bdy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bex,bey,bfx,bfy,bgx,bgy,bhx,bhy,kx,ky,lx,ly))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(dx,dy,mx,my,nx,ny,cax,cay,cbx,cby,ccx,ccy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7}" stroke="black" stroke-width="1" fill="none" /> \n'.format(cdx,cdy,ox,oy,px,py,ax,ay))

def SketchFrontSurface():
    ax = 5; ay = 5+side_length+10; bx = 5+side_length; by = ay; cx = 5+side_length; cy = by+side_length;
    dx = 5; dy = cy; ex = bx; ey = by+(side_length-slot_length)/2;
    fx = ex-thickness; fy=ey; gx = ex; gy = by+(side_length+slot_length)/2; hx = fx; hy = gy;
    ix = dx+(side_length+slot_length)/2; iy = cy; jx = ix; jy = iy-thickness;
    lx = dx+(side_length-slot_length)/2; ly = iy; mx = lx; my = jy;
    nx = dx; ny = ay+(side_length+slot_length)/2; ox = nx+thickness; oy = ny;
    px = ax; py = ay+(side_length-slot_length)/2; qx = ox; qy = py;
    aax = fx; aay = by+(side_length/2)-1.5; abx = aax-(bolt_length-3); aby = aay;
    acx = abx; acy = aby-1.5; adx = acx-2; ady =acy; aex = adx; aey = ady+6; afx = acx; afy = aey;
    agx = abx; agy = aby+3; ahx = aax; ahy = aay+3;
    bax = dx+(side_length/2)+1.5; bay = jy; bbx = bax; bby = bay-(bolt_length-3); bcx = bbx+1.5; bcy = bby;
    bdx = bcx; bdy = bcy-2; bex = bdx-6; bey = bdy; bfx = bex; bfy = bby; bgx = bbx-3; bgy = bfy; bhx = bgx; bhy = bay;
    cax = ox; cay = ay+(side_length/2)+1.5; cbx = cax+(bolt_length-3); cby = cay; ccx = cbx; ccy = cby+1.5;
    cdx = ccx+2; cdy = ccy; cex = cdx; cey = cdy-6; cfx = cbx; cfy = cey; cgx = cfx; cgy = cby-3; chx = cax; chy = cgy;
    #sketch in svg file
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} \n'.format(ax,ay,bx,by,ex,ey,fx,fy,aax,aay))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(abx,aby,acx,acy,adx,ady,aex,aey,afx,afy,agx,agy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ahx,ahy,hx,hy,gx,gy,cx,cy,ix,iy,jx,jy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bax,bay,bbx,bby,bcx,bcy,bdx,bdy,bex,bey,bfx,bfy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bgx,bgy,bhx,bhy,mx,my,lx,ly,dx,dy,nx,ny))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ox,oy,cax,cay,cbx,cby,ccx,ccy,cdx,cdy,cex,cey))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11}"\n'.format(cfx,cfy,cgx,cgy,chx,chy,qx,qy,px,py,ax,ay))
    f.write('stroke="black" stroke-width="1" fill="none" />\n')

def SketchLeftSurface():
     #assign coordinates
    ax = 5+side_length+10+thickness; ay = 5+side_length+10; bx = ax+side_length-2*thickness; by = ay; cx = bx; cy = by+side_length; dx = ax; dy = cy;
    ex = bx; ey = by+(side_length-slot_length)/2; fx = ex+thickness; fy = ey; gx = fx; gy = by+(side_length+slot_length)/2;
    hx = ex; hy = gy; ix = dx+(side_length-2*thickness+slot_length)/2; iy = cy; jx = ix; jy = iy-thickness; kx = dx+(side_length-2*thickness-slot_length)/2;
    ky = jy; lx = kx; ly = iy; mx = ax; my =hy; nx = mx-thickness;ny = my; ox = nx; oy = ey; px = ax; py = oy;
    aax = fx; aay = by+(side_length/2)-1.5; abx = aax-4; aby = aay; acx = abx; acy = aby+3; adx = aax; ady = acy;
    bax = ox+(side_length/2)+1.5; bay = jy; bbx = bax; bby = bay-(bolt_length-3); bcx = bbx+1.5; bcy = bby;
    bdx = bcx; bdy = bcy-2; bex = bdx-6; bey = bdy; bfx = bex; bfy = bcy; bgx = bfx+1.5; bgy = bfy; bhx=bgx; bhy =bay;
    cax = ox; cay = ay+(side_length/2)+1.5; cbx = cax+4; cby = cay; ccx = cbx; ccy = cby-3; cdx = cax; cdy = ccy;
    # sketch in svg file
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} \n'.format(ax,ay,bx,by,ex,ey,fx,fy,aax,aay))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(abx,aby,acx,acy,adx,ady,gx,gy,hx,hy,cx,cy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ix,iy,jx,jy,bax,bay,bbx,bby,bcx,bcy,bdx,bdy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(bex,bey,bfx,bfy,bgx,bgy,bhx,bhy,kx,ky,lx,ly))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(dx,dy,mx,my,nx,ny,cax,cay,cbx,cby,ccx,ccy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7}" stroke="black" stroke-width="1" fill="none" /> \n'.format(cdx,cdy,ox,oy,px,py,ax,ay))

def SketchBottomSurface():
    # coordinates for each points on the figure
    ax = 5+2*side_length+10+10+thickness; ay = 5+side_length+10+thickness; bx = ax+side_length-2*thickness; by = ay; cx = bx; cy = by+side_length-2*thickness;
    dx = ax; dy = cy; ex = ax+(side_length-2*thickness-slot_length)/2; ey = ay; fx = ex; fy = ey-thickness; gx = fx+slot_length; gy = fy;
    hx = gx; hy = ey; ix = bx; iy = by+(side_length-2*thickness-slot_length)/2; jx = ix+thickness; jy = iy; kx = jx; ky = jy+slot_length;
    lx = ix; ly = ky; mx = dx+(side_length-2*thickness+slot_length)/2; my = cy; nx = mx; ny = my+thickness; ox = nx-slot_length; oy =ny;
    px = ox; py = my; qx = ax; qy = ay+(side_length-2*thickness+slot_length)/2; rx = qx-thickness; ry = qy; sx = rx; sy = ry-slot_length;
    tx = ax; ty = sy; aax = fx+(slot_length/2)-1.5; aay = fy; abx = aax; aby = aay+4; acx = aax+3; acy = aby;
    adx = acx; ady = aay; bax = jx; bay = jy+(slot_length/2)-1.5; bbx = bax-4; bby = bay; bcx = bbx; bcy = bby+3;
    bdx = bax; bdy = bcy; cax = ox+(slot_length/2)+1.5; cay = ny; cbx = cax; cby = cay-4;
    ccx = cbx-3; ccy = cby; cdx = ccx; cdy = cay; dax = rx; day = sy+(slot_length/2)+1.5;
    dbx = dax+4; dby = day; dcx = dbx; dcy = dby-3; ddx = dax; ddy = dcy;
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} \n'.format(ax,ay,ex,ey,fx,fy,aax,aay,abx,aby))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(acx,acy,adx,ady,gx,gy,hx,hy,bx,by,ix,iy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(jx,jy,bax,bay,bbx,bby,bcx,bcy,bdx,bdy,kx,ky))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(lx,ly,cx,cy,mx,my,nx,ny,cax,cay,cbx,cby))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(ccx,ccy,cdx,cdy,ox,oy,px,py,dx,dy,qx,qy))
    f.write('{0},{1} {2},{3} {4},{5} {6},{7} {8},{9} {10},{11} \n'.format(rx,ry,dax,day,dbx,dby,dcx,dcy,ddx,ddy,sx,sy))
    f.write('{0},{1} {2},{3}" \n'.format(tx,ty,ax,ay))
    f.write('stroke="black" stroke-width="1" fill="none" />\n')

def SketchCover():
    ax = 5+2*side_length+10+10; ay = 5; bx = ax+side_length+2; by = ay;
    cx = bx; cy = by+side_length+2; dx = ax; dy = cy;
    f.write('<polyline points="{0},{1} {2},{3} {4},{5} {6},{7} {8},{9}" \n'.format(ax,ay,bx,by,cx,cy,dx,dy,ax,ay))
    f.write('stroke="black" stroke-width="1" fill="none" />\n')

try: side_length
except NameError: side_length = None
while side_length is None:
    EnterSideLength()
    if a <= 180 and a >= 50:#check if input is in the appropriate range
        side_length = a
    elif a > 180:
        print('value entered is too large, length was adjusted to 180mm')
        side_length = 180
    elif a < 50:
        print('Too small, side length was adjusted to 50mm')
        side_length = 50
try:slot_length
except NameError: slot_length = None
while slot_length is None:
    EnterTslotLength()
    if b <= side_length*0.5 and b >= side_length*0.25:
        slot_length = b
    elif b > side_length*0.5:
        print('Value is too large, length was adjusted to half of the side length')
        slot_length = side_length*0.5
    elif b < side_length*0.25:
        print('Value is too small, length was adjusted to 1/4 of the side length')
        slot_length = side_length * 0.25
try: bolt_length
except NameError: bolt_length = None
while bolt_length is None:
    EnterBoltLength()
    if c <= 1 and c >= 0.1:#check if input is in the appropriate range
        bolt_length = c * 25.4
    elif c > 1:
        print('value entered is too large, length was adjusted to 1 inch')
        bolt_length = 1 * 25.4
    elif c < 0.1:
        print('Too small, length was adjusted to 0.1 inch')
        bolt_length = 0.1 * 25.4
try: thickness
except NameError: thickness = None
while thickness is None:
    EnterThickness()
    if d <= 6 and d >= 1:#check if input is in the appropriate range
        thickness = d
    elif c > 6:
        print('value entered is too large, thickness was adjusted to 6mm')
        thickness = 6
    elif c < 0.1:
        print('Too small, sickness was adjusted to 1mm')
        thickness = 1

print('the side length is: %f mm' %side_length )
print('the length of T-slot is: %f mm' %slot_length)
print('screw length is: %f mm' %bolt_length)
f = open("square.svg", "w")
f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
f.write('<svg viewBox="0 0 457 610" xmlns="http://www.w3.org/2000/svg">\n')
EnterFrontText()
EnterTopText()
ColumbiaLogo()
Selectimages()
SketchBackSurface()
SketchRightSurface()
SketchFrontSurface()
SketchLeftSurface()
SketchBottomSurface()
SketchCover()
f.write('</svg>')
f.close()
