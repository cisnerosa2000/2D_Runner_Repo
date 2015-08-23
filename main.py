from Tkinter import *
import random
from collections import defaultdict


root = Tk()

screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
root.attributes("-topmost",1)
root.attributes("-alpha",.9)
root.geometry("%dx%d+0+0" % (screen_w, screen_h))
root.title("Runner")


canvas = Canvas()
canvas.config(width=screen_w,height=screen_h )









class Display(object):
    def __init__(self):
        self.ground = canvas.create_rectangle(0,screen_h-200,screen_w,screen_h,fill="black")
        self.ceiling = canvas.create_rectangle(0,0,screen_w,100,fill="black")
        
        
        
        
class Enemy(object):
        def __init__(self):
            self.rectangle = canvas.create_rectangle(1400,screen_h-200,1410,screen_h-200-random.randint(10,90),fill="black",tags="enemy")
            player.enemy_list.append(self.rectangle)
            
           
          
            
    
class Player(object):
    def __init__(self):
        self.sprite_index = 0
        self.avatar = canvas.create_image(50,screen_h-225,image=sprites.images[self.sprite_index])
        self.jumping = False
        self.fall_speed = 1
        self.jump_speed = 1
        self.enemy_list = []
        self.difficulty = 900
        self.marker_list = []
        self.alive = True
        self.score = 0
        self.fulfilled = False
        self.speed = 8
        self.distance = 0
        
        
        self.time_loop()
        self.update_loop()
    def update_loop(self):
        self.coords = [canvas.coords(self.avatar)[0],canvas.coords(self.avatar)[1]]
        
        
        
        
        #collision
        self.bbox = canvas.bbox(self.avatar)
        self.overlapping = canvas.find_overlapping(*self.bbox)
        for enemy in self.overlapping:
            if "enemy" in canvas.gettags(enemy) and self.alive:
                self.alive = False
                self.rip()
                canvas.move(self.avatar,0,-100)
              
                
        
        
        
        #collision
        
        
        
        #jumping and gravity
        if canvas.coords(self.avatar)[1] <= screen_h-225 or self.alive == False:
            canvas.move(self.avatar,0,self.fall_speed)
            self.fall_speed += .5
            
            if self.fall_speed > 12.5:
                self.fall_speed = 12.5
            

        if self.jumping == True and self.jump_speed > 0 and self.alive:
            canvas.move(self.avatar,0,-self.jump_speed)
            self.jump_speed -= .5
        elif self.alive:
            canvas.coords(self.avatar,self.coords[0],544)
            
        
            
        #best x coordinate is 544
            
            
            
        if canvas.coords(self.avatar)[0] <= 500 and self.alive and self.fulfilled == False:
            canvas.move(self.avatar,int(1),0)
            if self.coords[0] == 500:
                self.fulfilled  = True
        
        
            
        
            
            
            
            
        #jumping and gravity
        
        
        #spawning enemies
    
        self.chance = random.randint(0,20)
        self.distance_list = []
        self.distanced = False
        
        
        
        
        
        
        for instance in self.enemy_list:
            a = canvas.coords(instance)[0]
            self.distance_list.append(a)
        
        if self.distance_list:
            
            if max(self.distance_list) <= self.difficulty:
                self.distanced = True
        if not self.distance_list:
            self.distanced = True
        
        
        
        if self.chance == 5 and self.distanced == True and self.alive:
            enemy = Enemy()
            if self.difficulty < 1100 and self.alive:
                self.difficulty += 80
        
        #spawning enemies
        
        #moving and dealing with enemies
        for enemy_instance in self.enemy_list:
            if self.alive:
                canvas.move(enemy_instance,-int(self.speed),0)
            if canvas.coords(enemy_instance)[0] <= 0:
                canvas.delete(enemy_instance)
                self.enemy_list.remove(enemy_instance)
                if self.alive:
                    self.score += 1
                    try:
                        canvas.delete(self.score_)
                    except AttributeError:
                        pass
                    
                    
        
        
        #moving and dealing with enemies
        
        
        #create a trail 
        
        
        if self.alive:
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]-14,self.coords[0],self.coords[1]-10,fill="gray1",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]-10,self.coords[0],self.coords[1]-6,fill="gray20",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]-6,self.coords[0],self.coords[1]-2,fill="gray30",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]-2,self.coords[0],self.coords[1]+2,fill="gray40",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]+2,self.coords[0],self.coords[1]+6,fill="gray50",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]+6,self.coords[0],self.coords[1]+10,fill="gray60",outline="")
            self.marker_list.append(self.marker)
            self.marker = canvas.create_rectangle(self.coords[0]-11,self.coords[1]+10,self.coords[0],self.coords[1]+14,fill="gray70",outline="")
            self.marker_list.append(self.marker)
            
        
        
            canvas.lift(self.avatar)
        
        for marker in self.marker_list:
            
            if self.alive:
                canvas.move(marker,-int(self.speed),0)
                
            if canvas.coords(marker)[0] <= random.randint(0,400) and self.alive:
                canvas.delete(marker)
                self.marker_list.remove(marker)
           
            
            
        
        #create a trail 
        
        
        
        root.after(1,self.update_loop)
    def time_loop(self): 
        
        if self.sprite_index != 3:
            self.sprite_index += 1
            
        elif self.sprite_index == 3:
            self.sprite_index = 0
        
        canvas.itemconfig(self.avatar,image=sprites.images[self.sprite_index])
        
        if self.alive:
            self.distance += 1
        self.score_ = Label(root,text="Score: %s, Distance(m):%s," % (int(self.score),int(self.distance)),font=("","30"),bg="black",fg="white")
        self.score_.place(x=50,y=600)
        
        #scoreboard
        
        
        #scoreboard
        root.after(100,self.time_loop)
        
        
        
    def jump(self,event):
        if canvas.coords(self.avatar)[1] >= screen_h-230 and self.alive:
            self.jumping = True
            self.jump_speed = 15
            self.fall_speed = 0

        
            
        
        
        
    def rip(self):
        died = Toplevel()
        died.title("You Died!")
        died.geometry("600x300+350+150")
        died.attributes("-topmost",1)
        died.attributes("-alpha",.7)
        
        label = Label(died,text="YOU DIED! YOUR SCORE IS %s" % int(self.score),font=("Helvetica","30"))
        label.pack(pady=95)
        
        



class Spritesheet(object):
    def __init__(self):

        self.spritesheet = PhotoImage(file="Ninja-Spritesheet.gif")
        self.num_sprintes = 4
        self.last_img = None
        self.images = [self.subimage(39*i, 0, 39*(i+1), 54) for i in range(self.num_sprintes)]
    

    def subimage(self, l, t, r, b):
        dst = PhotoImage()
        root.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    
        
        




sprites = Spritesheet()

sprites = Spritesheet()
display = Display()
player = Player()

root.bind("<space>",player.jump)
root.bind("<Up>",player.jump)

 

canvas.pack()
root.mainloop()