import turtle
import random

# 1. Screen Setup (Zabardasti Window Samne Layega)
screen = turtle.Screen()
screen.title("Toyota Land Cruiser LC300 - VS Code Premium Highway")
screen.setup(width=900, height=700)
screen.bgcolor("#1a2230") # Dark cyber night background
screen.tracer(0) # Smooth animation controller

# 2. Highway Road Borders & Lanes Layout
road = turtle.Turtle()
road.speed(0)
road.hideturtle()
road.penup()

def draw_static_highway():
    # Asphalt Gray Road Body
    road.goto(-250, 350)
    road.color("#252e3d")
    road.begin_fill()
    for _ in range(2):
        road.forward(500)
        road.right(90)
        road.forward(700)
    road.end_fill()
    
    # Left & Right Solid Yellow Lines
    road.color("#ffcc00")
    road.width(4)
    road.goto(-250, 350)
    road.setheading(270)
    road.pendown()
    road.forward(700)
    road.penup()
    road.goto(250, 350)
    road.pendown()
    road.forward(700)
    road.penup()

# 3. Endless Moving World Items (Stripes, Trees, Light Poles)
moving_items = []
road_speed = 0 # Starts at N (0 speed)

# Generate scenery positions initial
for y in range(-350, 400, 120):
    # White lane stripes (Left & Right lane dividers)
    moving_items.append({"type": "stripe", "x": -80, "y": y})
    moving_items.append({"type": "stripe", "x": 80, "y": y})
    # Left side custom Pine Trees & Poles
    moving_items.append({"type": "tree", "x": -310, "y": y})
    moving_items.append({"type": "pole", "x": -275, "y": y})
    # Right side custom Pine Trees
    moving_items.append({"type": "tree", "x": 310, "y": y})

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

def draw_scenery():
    drawer.clear()
    for item in moving_items:
        if item["type"] == "stripe":
            drawer.penup()
            drawer.goto(item["x"], item["y"])
            drawer.color("white")
            drawer.setheading(90)
            drawer.pendown()
            drawer.width(3)
            drawer.forward(40)
        
        elif item["type"] == "tree":
            # Dark Brown Trunk
            drawer.penup()
            drawer.goto(item["x"]-4, item["y"]-20)
            drawer.color("#4a2e1b")
            drawer.begin_fill()
            for _ in range(2):
                drawer.forward(8)
                drawer.left(90)
                drawer.forward(20)
                drawer.left(90)
            drawer.end_fill()
            # Layered Dark Green Leaves Triangles
            drawer.color("#113f30")
            for layer in range(3):
                drawer.penup()
                drawer.goto(item["x"], item["y"] + (layer * 12))
                drawer.setheading(0)
                drawer.begin_fill()
                drawer.circle(16 - (layer*3), steps=3) # Cone shape
                drawer.end_fill()
                
        elif item["type"] == "pole":
            # Vertical Street Light Pole with Horizontal Extension Arm
            drawer.penup()
            drawer.color("#64748b")
            drawer.width(3)
            drawer.goto(item["x"], item["y"]-30)
            drawer.pendown()
            drawer.goto(item["x"], item["y"]+20) # Upward pole vector
            drawer.goto(item["x"]+20, item["y"]+20) # Arm stretching to road
            # Glowing Neon Yellow Bulb Point
            drawer.penup()
            drawer.goto(item["x"]+20, item["y"]+20)
            drawer.dot(10, "#ffeb3b")

# 4. PLAYER CHARACTER: Real Toyota Land Cruiser LC300 Blueprint
lc300 = turtle.Turtle()
lc300.speed(0)
lc300.hideturtle()
lc300.penup()
lc300_x = 0
lc300_y = -220

def draw_lc300(x, y):
    lc300.clear()
    
    # 1. Base Dark Profile Ground Shadow
    lc300.penup()
    lc300.goto(x - 24, y - 42)
    lc300.color("#0a0f18")
    lc300.begin_fill()
    for _ in range(2):
        lc300.forward(48)
        lc300.left(90)
        lc300.forward(84)
        lc300.left(90)
    lc300.end_fill()

    # 2. Main Prestige Pearl White Premium Body Shell
    lc300.penup()
    lc300.goto(x - 22, y - 40)
    lc300.color("#f8fafc")
    lc300.begin_fill()
    for _ in range(2):
        lc300.forward(44)
        lc300.left(90)
        lc300.forward(80)
        lc300.left(90)
    lc300.end_fill()
    
    # Outer body border lining
    lc300.width(2)
    lc300.color("#94a3b8")
    lc300.pendown()
    for _ in range(2):
        lc300.forward(44)
        lc300.left(90)
        lc300.forward(80)
        lc300.left(90)
    lc300.penup()

    # 3. Massive Front Bumper Matte-Black Mesh & Grill Bars
    lc300.goto(x - 18, y + 34)
    lc300.color("#111622")
    lc300.begin_fill()
    for _ in range(2):
        lc300.forward(36)
        lc300.left(90)
        lc300.forward(6)
        lc300.left(90)
    lc300.end_fill()
    
    # Inner Horizontal Chrome Accent
    lc300.goto(x - 14, y + 37)
    lc300.color("#cbd5e1")
    lc300.width(2)
    lc300.pendown()
    lc300.forward(28)
    lc300.penup()

    # 4. REAL GOL (CIRCULAR) LED PROJECTOR HEADLIGHT LAMPS
    lc300.goto(x - 16, y + 36)
    lc300.dot(9, "#ffffff") # Left Bright beam
    lc300.dot(6, "#00f0ff") # Cyan inner lens ring
    lc300.goto(x + 16, y + 36)
    lc300.dot(9, "#ffffff") # Right beam
    lc300.dot(6, "#00f0ff")

    # 5. Distinctive Executive VIP Side Mirrors Layout
    lc300.color("#f8fafc")
    lc300.width(4)
    lc300.goto(x - 22, y + 14)
    lc300.pendown()
    lc300.goto(x - 28, y + 16)
    lc300.penup()
    lc300.goto(x + 22, y + 14)
    lc300.pendown()
    lc300.goto(x + 28, y + 16)
    lc300.penup()

    # 6. Dark Panoramic Cabin Greenhouse Windows
    lc300.goto(x - 16, y - 24)
    lc300.color("#0f172a")
    lc300.begin_fill()
    for _ in range(2):
        lc300.forward(32)
        lc300.left(90)
        lc300.forward(45)
        lc300.left(90)
    lc300.end_fill()

# 5. HUD Live Cockpit Text Display
hud_text = turtle.Turtle()
hud_text.speed(0)
hud_text.color("white")
hud_text.penup()
hud_text.hideturtle()
hud_text.goto(0, 310)

def update_hud():
    hud_text.clear()
    if road_speed > 0:
        hud_text.write(f"TOYOTA LC300 V6 • GEAR: DRIVE • SPEED: {int(road_speed * 26)} KM/H", align="center", font=("Courier", 14, "bold"))
    else:
        hud_text.write("TOYOTA LC300 V6 • GEAR: NEUTRAL • HOLD UP ARROW KEY", align="center", font=("Courier", 14, "bold"))

# 6. Keyboard Control Actions Engine
def drive_forward():
    global road_speed
    road_speed = min(road_speed + 0.4, 12) # Instant throttle power acceleration

def brake_or_reverse():
    global road_speed
    road_speed = max(road_speed - 0.6, 0) # Smooth brake mechanics

def steer_left():
    global lc300_x
    if lc300_x > -210: # Asphalt barrier constraints
        lc300_x -= 15

def steer_right():
    global lc300_x
    if lc300_x < 210:
        lc300_x += 15

screen.listen()
screen.onkeypress(drive_forward, "Up")
screen.onkeypress(brake_or_reverse, "Down")
screen.onkeypress(steer_left, "Left")
screen.onkeypress(steer_right, "Right")

# ─── MAIN SIMULATION LOOP ENGINE ───
draw_static_highway()

while True:
    # Applying smooth automatic regenerative friction slowdown
    if road_speed > 0:
        road_speed = max(0, road_speed - 0.1)

    # Move environment down dynamically to generate shifting road animation speed
    for item in moving_items:
        item["y"] -= road_speed
        if item["y"] < -360:
            item["y"] = 360 # Respawns loops smoothly back over top horizon boundary

    # Trigger fresh frame renders
    draw_scenery()
    draw_lc300(lc300_x, lc300_y)
    update_hud()
    screen.update()

