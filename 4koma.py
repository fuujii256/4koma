import sys
import random
import cv2
import numpy as np
import pygame
 

def main(): # メイン

    img_bg = [ pygame.image.load('image/TITLE.png'),
                  pygame.image.load('image/P1.png'),
                  pygame.image.load('image/P2.png'),
                  pygame.image.load('image/P3.png'),
                  pygame.image.load('image/P4.png'),
                  pygame.image.load('image/P5.png'),
                  pygame.image.load('image/ENDROLL.png')] 

    scn_time = [30,30,30,30,30,30,30]
    scn_type = [0,0,0,0,0,0,0]
            
              
    pygame.init()
    pygame.display.set_caption("4コママンガ")
    screen = pygame.display.set_mode((2732, 1536) , pygame.FULLSCREEN)
    
    #透明を有効にしたsurface
    scr =pygame.Surface((2732,1536),flags=pygame.SRCALPHA)

    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    scene = 0       
    scene_max = 6
    counter = 0
    
#        screen.fill((0,0,0))
        
#    while True: 
    for scene in img_bg:

        while counter < scn_time[scene]:
                if scn_type[scene] == 0:
                    screen.blit(img_bg[scene], [0,0]) 
 
 #   pygame.quit()
 #   sys.exit()

                #このシーンの動きの初期化
            


        #カウンタ表示                
        #text1 = font1.render("TMR:"+str(tmr)+" TTMR:"+str(ttmr)+" AC:"+str(ac), True, (255,0,0))
        #screen.blit(text1, (0,0))
        
        #ウィンドクローズで強制終了
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((1280, 980), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((1280, 980))

        # 星のスクロール

        pygame.display.update()
        clock.tick(50)

if __name__ == '__main__':
    main()



