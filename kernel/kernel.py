from actions import *
import camera

def kernel(mainloop,used_modules):
    m0 = Motor(17,18)
    m1 = Motor(22,23)
    m2 = Motor(20,21)
    m3 = Motor(25,26)

    get_raw = None
    if "camera" in used_modules:
        get_raw = camera.init()
    
    while True:
        inp = {}
        if "camera" in used_modules:
            inp["raw_img"] = get_raw()
        
        actions = mainloop(inp)
        
        turning, linear = 0, 0
        for a in actions:
            if isinstance(a,Move):
                linear += a.speed
            if isinstance(a,Turn):
                turning += a.speed
        leftF = turning+linear
        rightF = linear-turning
        if leftF < 0:
            m0.backward(-leftF)
            m2.backward(-leftF)
        else:
            m0.forward(leftF)
            m2.forward(leftF)
        if rightF < 0:
            m1.backward(-rightF)
            m3.backward(-rightF)
        else:
            m1.forward(rightF)
            m3.forward(rightF)
