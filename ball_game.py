import pygame,sys,random
class Game():
    def main(self):
        #initial speed
        Xspeed =5
        Yspeed =5
        livesinit=5

        paddle_speed=30
        points=0
        bgcolor=0,0,0 #background color is black
        size=width,height=500,500

        #initialize pygame engine
        pygame.init()
        screen=pygame.display.set_mode(size)



        #objects
        paddle=pygame.image.load('blue_paddle.png')
        paddle_rect=paddle.get_rect()

        ball=pygame.image.load('ball.png')
        ball_rect=ball.get_rect()

        bg=pygame.image.load('black.png')

        #arrange_variable
        paddle_rect=paddle_rect.move((width/2)-(paddle_rect.right/2),(height-20))
        ball_rect=ball_rect.move((width/2),(height/2))
        xspeed=Xspeed
        yspeed=Yspeed
        lives=livesinit     
        clock=pygame.time.Clock()
        pygame.key.set_repeat(1,30)

        #Loop
        while True:
            clock.tick(40) #fps


            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        paddle_rect=paddle_rect.move(-paddle_speed,0)
                        if paddle_rect.left<0:
                            paddle_rect.left=0
                    if event.key == pygame.K_RIGHT:
                        paddle_rect=paddle_rect.move(paddle_speed,0)
                        if paddle_rect.right>width:
                            paddle_rect.right=width



            #check if paddle check the ball
            if (ball_rect.bottom>=paddle_rect.top) and (ball_rect.bottom<=paddle_rect.bottom) and \
                (ball_rect.right>=paddle_rect.left) and(ball_rect.left<=paddle_rect.right):
                    yspeed=-yspeed
                    # xspeed=-xspeed
                    points+=1
            #move ball
            ball_rect=ball_rect.move(xspeed,yspeed)
            if ball_rect.left<0 or  ball_rect.right>width:
                xspeed=-xspeed
            if ball_rect.top<0 :
                yspeed=-yspeed
            #lose
            if ball_rect.top>height:
                lives-=1
                #start new game
                xspeed=Xspeed 
                rand=random.random()
                if rand>.5:
                    xspeed=-xspeed
                yspeed=Yspeed
                ball_rect.center=width*random.random(), height/3.5

                #end game
                if lives==0:
                    msg=pygame.font.Font(None,70).render("Game Over",True,(0,255,255),bgcolor)
                    msgrect=msg.get_rect()
                    msgrect=msgrect.move(width/2-(msgrect.center[0]),height/3)
                    screen.blit(bg,(500,500))
                    screen.blit(msg,msgrect)
                    pygame.display.flip()
                    
                    #game restart and quit event loop
                    while True:
                        restart=False
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type ==pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    sys.exit()
                                if not(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                                    restart = True
                        if restart:
                            screen.fill(bgcolor)
                            lives=livesinit
                            points=0
                            break

            # update
            screen.fill(bgcolor)
            screen.blit(bg,(0,0))

            scoretext= pygame.font.Font(None,40).render(str(points),True,(0,255,255 ),(0, 0, 255))
            scoretext_rect=scoretext.get_rect()
            scoretext_rect=scoretext_rect.move(width-  scoretext_rect.right,0)
            screen.blit(scoretext,scoretext_rect)
            screen.blit(ball,ball_rect)
            screen.blit(paddle,paddle_rect)

            pygame.display.flip()

if __name__ == '__main__':
    br=Game()
    br.main()

                

