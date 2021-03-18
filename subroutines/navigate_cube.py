def navigate_cube(inp,target_col):
    bounds = target_bounds(inp,target_col,10)
    if bounds is None:
        return [Turn(1)]

    xT,yT,zT = approx_target_pos(bounds[0],
                                 bounds[1],
                                 0.1)
    if zT < 0.2:
        if inp["ultra_dist"] < 0.05:
            return []
        else:
            ft, fl = calc_forces(xT,zT)
            return [Move(fl / 2),Turn(ft)]
    ft,fl = calc_forces(xT,zT)
    return [Move(fl),Turn(ft)]

def calc_forces(xT,zT):
    if zT == 0:
        return 1, 0
    else:
        ft = min(xT / zT,1)
        return ft, 1 - ft

def image_space(pos):
    return (2 * pos[0] / camera.WIDTH - 1,
            2 * pos[1] / camera.HEIGHT - 1)

def approx_target_pos(posA,posB,widthT):
    xA, yA = image_space(posA)
    xB, yB = image_space(posB)
    tanfov = tan(camera.FOV_X)
    zT = widthT / (tanfov * abs(xA - xB))
    xT = zT * atan(tanfov * (xA + xB) / 2)
    yT = zT * atan(tanfov * (yA + yB) / 2)
    return (xT, yT, zT)

def target_bounds(inp,col_range,min_size):
    frame = inp["raw_img"]
    frame_hsv = cv2.cvtColor(frame,
                             cv2.COLOR_BGR2HSV)
    filtered = cv2.inRange(frame_hsv,
                           col_range[0],
                           col_range[1])
    _, conts, _ = cv2.findContours(filtered,
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    if len(conts) == 0:
        return None
    target = sorted(conts,key=cv2.contourArea)[-1]
    if cv2.contourArea(target) < min_size:
        return None
    x,y,width,height = cv2.boundingRect(target)
    return ((x,y),(x+width,y+height))
