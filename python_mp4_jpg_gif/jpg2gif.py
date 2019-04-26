import imageio
import os

images = []

def create_gif(inpath,image_list, gif_name):

    lag = 0.01666666
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(inpath + image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = lag)
 
    return
 
def main():
    speed = 8 #1:lowest speed
    image_list = []
    path = os.getcwd()
    inpath = path + '/output'
    choose_list = list(reversed(range(24,41,speed))) #maximum: 57
    list1 = list(range(24,41,speed))
    choose_list.extend(list1)
    for i in choose_list:
        filename =  ("/%#05d.jpg" % (i+1))
        image_list.append(filename)

    gif_name = 'created_gif.gif'
    create_gif(inpath, image_list, gif_name)
    print("DONE!")

if __name__ == "__main__":
    main()
