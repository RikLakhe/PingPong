# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos= [WIDTH/2,HEIGHT/2]
ball_vel= [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos= [WIDTH/2,HEIGHT/2];
    ball_vel=[random.randrange(60,180)/60,random.randrange(120,240) / 60]
    ball_vel[1] = -ball_vel[1]
    if direction == 'LEFT':
        ball_vel[0] = -ball_vel[0]
        
    if direction == 'RIGHT':
        ball_vel[0] = ball_vel[0]
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball('LEFT')
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,BALL_RADIUS,PAD_WIDTH
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # bounce off the top and bottom walls
    if ball_pos[1] == HEIGHT-BALL_RADIUS or ball_pos[1] == BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # check if ball touched the gutter
    if ball_pos[0] == WIDTH-PAD_WIDTH-BALL_RADIUS:
        spawn_ball('LEFT')
        
    if ball_pos[0] == PAD_WIDTH+BALL_RADIUS:
        spawn_ball('RIGHT')
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle((ball_pos[0],ball_pos[1]), BALL_RADIUS, 12, '','white')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos == 
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line((0, (paddle1_pos)-PAD_HEIGHT), (0,(paddle1_pos)+PAD_HEIGHT), PAD_WIDTH, 'WHITE')
    canvas.draw_line((WIDTH, (paddle2_pos)-PAD_HEIGHT), (WIDTH,(paddle2_pos)+PAD_HEIGHT), PAD_WIDTH, 'WHITE')
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 1
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 1
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 1
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += 1
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= 1


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('New game', new_game)


# start frame
new_game()
frame.start()
