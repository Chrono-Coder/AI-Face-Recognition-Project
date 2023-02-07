import xmltodict
import matplotlib.pyplot as plt

with open("annotations.xml") as file:
    file_data = file.read() # read file contents
    
    # parse data using package
    dict_data = xmltodict.parse(file_data)

image_list  =[]
items = dict_data["annotations"]["track"]["box"]
length = len(items)
image_list = [None] * 1000
for i in items:
    frame = int(i["@frame"])
    image_list[frame] = i



import matplotlib.pyplot as plt


def custom_crop(lis, i):
    filename = "images/frame_{:06}.PNG".format(i)
    image = plt.imread(filename)
    
    item = image_list[i]

    
    x0 = item['@xtl']
    x0 = int(float(x0))
    print(x0)
    y0 = item['@ytl']
    y0 = int(float(y0))
    print(y0)
    width = item['@xbr']
    width = int(float(width))
    print(width)
    height = item['@ybr']
    height = int(float(height))
    print(height)
    return image[y0:height , x0:width, :]

#%%
for i in range(0,length):

    # filename = "hi/images/frame_{:06}.PNG".format(i)
    try:
        print("trying for frame_{:06}".format(i))
        image = custom_crop(image_list, i)
        
        
    except:
        print("error for frame_{:06}".format(i))
    else:
        plt.imsave("out/frame_{:06}.PNG".format(i), image)
   