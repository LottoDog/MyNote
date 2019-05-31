import random
TITLE = 'Flappy alien'
WIDTH = 700
HEIGHT = 708

music.play('bgm')
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3
color1 = 'white'
color2 = 'white'
pause = True
alien = Actor('alien', (75, 200))
alien.dead = False
alien.score = 0
alien.vy = 0

def reset_pipes():
    GAP = random.randint(250,350)
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes() # Set initial pipe positions.

def update_pipes():
    global SPEED
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED

    if pipe_top.right < 0:
        reset_pipes()
        if not alien.dead:
            alien.score += 1
            SPEED += 0.5

def update_alien():
    uy = alien.vy
    alien.vy += GRAVITY
    alien.y += (uy + alien.vy) / 2
    alien.x = 75

    if not alien.dead:
        alien.image = 'alien'

    if alien.colliderect(pipe_top) or alien.colliderect(pipe_bottom):
        alien.dead = True
        alien.image = 'alien_hurt'
        sounds.a.play()

    if not 0 < alien.y < 720:
        global SPEED
        alien.y = 200
        alien.dead = False
        alien.score = 0
        alien.vy = 0
        SPEED = 3
        reset_pipes()


def update():
    update_pipes()
    update_alien()

def on_key_down():
    global SPEED
    global pause
    if not alien.dead:
        if keyboard[keys.UP]:
            alien.vy = -FLAP_STRENGTH
            sounds.jiujiu.play()
        if keyboard[keys.LEFT]:
            alien.vy = -FLAP_STRENGTH
            sounds.jiujiu.play()
            SPEED -=0.5
        if keyboard[keys.RIGHT]:
            alien.vy = -FLAP_STRENGTH
            sounds.jiujiu.play()
            SPEED +=0.5
        if keyboard[keys.DOWN]:
            alien.vy = FLAP_STRENGTH
            sounds.jiujiu.play()
            SPEED +=0.5
        if keyboard[keys.SPACE]:
            if pause:
                music.pause()
                pause = False
            else:
                music.unpause()
                pause = True


def draw():
    screen.blit('bg',(-550,-350))
    pipe_top.draw()
    pipe_bottom.draw()
    alien.draw()
    global SPEED
    global color1
    if SPEED>7:
        color1='YELLOW'
    else:
        color1='white'
    if alien.score>7:
        color2='RED'
    else:
        color2='white'
    screen.draw.text(
        "SPEED:  "+str(SPEED),
        color=str(color1),
        midtop=(120,10),
        fontsize=60,
        shadow=(1,1)
    )
    screen.draw.text(
        "SCORE:  "+str(alien.score),
        color=color2,
        midtop=(WIDTH-120, 10),
        fontsize=60,
        shadow=(1, 1)
    )
    if alien.dead:
        screen.draw.text(
            "You died!",
            color='RED',
            midtop=(WIDTH//2, HEIGHT//2),
            fontsize=100,
            shadow=(1, 1)
        )