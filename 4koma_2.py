import sys
import random
import cv2
import numpy as np
import pygame
import time
 

def main(): # メイン

    img_bg = [ pygame.image.load('image/TITLE.png'),
                  pygame.image.load('image/P1.png'),
                  pygame.image.load('image/P2.png'),
                  pygame.image.load('image/P3.png'),
                  pygame.image.load('image/P4.png'),
                  pygame.image.load('image/P5.png'),
                  pygame.image.load('image/ENDROLL.png')] 
    
    
    scn_time = [6,3,3,6,6,6,6]  #各シーンの表示時間「ｓ」
    scn_type = [0,2,0,0,0,0,1]  #各シーンの表示方法　
            
              
    pygame.init()
    pygame.display.set_caption("4コママンガ")

    scn_width = 1920/2 
    scn_height = 1080/2
    
    screen = pygame.display.set_mode((scn_width, scn_height))
 #   pygame.display.set_mode((1720,1080))
 #   pygame.display.toggle_fullscreen
    
    #透明を有効にしたsurface
    scr =pygame.Surface((scn_width,scn_height),flags=pygame.SRCALPHA)

    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    scene = 0       
    scene_max = 6
    time_sta = time.perf_counter()
    counter = 0
    cn = 0
    
    pwidth = 1920 /2
    pheight = 1080 /2     #表示サイズの変更
 
    i = 0   
    while i < len(img_bg):
        image = img_bg[i]
        img_bg[i] = pygame.transform.scale(image,(pwidth , pheight))
        i += 1
    
    while True: 
        
        if scn_type[scene] == 0:
            screen.blit(img_bg[scene], [0,0])   #通常表示
            
        if scn_type[scene] == 1:
            screen.blit(img_bg[scene], [pwidth -cn,0])   #横からスクロールイン
            if cn < pwidth: 
                cn += 10
            else:
                cn = pwidth
                
        if scn_type[scene] == 2:
            screen.blit(img_bg[scene], [0,pheight -cn,])   #下からスクロールイン
            if cn < pheight: 
                cn += 10

        time_now = time.perf_counter()
        if time_now > time_sta + scn_time[scene]:            
                time_sta = time_now 
                scene = scene +1
                cn = 0
                if scene > scene_max: 
                        pygame.quit()
                        sys.exit()
                
#        counter =  counter +1 
#        if counter > scn_time[scene]:            
#                counter =0 
#                scene = scene +1
#                cn = 0
#                if scene > scene_max: 
#                        pygame.quit()
#                        sys.exit()

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
        clock.tick(60)

if __name__ == '__main__':
    main()



