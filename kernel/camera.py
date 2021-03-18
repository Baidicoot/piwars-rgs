WIDTH = 800
HEIGHT = 800
FOV_X = None
FOV_Y = None

def init():
    cap = VideoStream(usePiCamera=True,
                      resolution=(WIDTH,HEIGHT)).start()
    time.sleep(0.5)
    return cap.read
