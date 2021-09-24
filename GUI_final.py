from tkinter import *
from PIL import Image,ImageTk,ImageEnhance
# import Tkinter
import cv2 as cv
import numpy as np

class Window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

        self.img1 =  None
        self.img2 =None
        self.img3 = None
        self.img4 = None
        self.img5 = None
        self.img1_1 = None
        self.img1_2 = None
        self.img1_3 = None
        self.img1_4 = None
        self.img1_5 = None
        self.img2_1 = None
        self.img2_2 = None
        self.img2_3 = None
        self.img2_4 = None
        self.img2_5 = None

    def init_window(self):
        self.master.title("office图片处理功能实现----尚华峰&刘香怡")
        self.pack(fill=BOTH,expand=1)

        # 实例化一个Menu对象，在窗体添加一个菜单
        menu = Menu(self.master)
        # menu.add_command(label='Show Image',command=self.showImg)
        # 锐化/柔化
        menu.add_command(label='锐化/柔化', command=self.showSharpenImg)
        # 对比度/亮度
        menu.add_command(label='亮度/对比度',command=self.contrast_ratio_brightness)
        # 色彩饱和度

        menu.add_command(label='色彩饱和度', command=self.saturability)
        # 色调
        # 重新着色
        menu.add_command(label='重新着色', command=self.rest_img)
        self.master.config(menu=menu)


    def client_exit(self):
        exit()
    def showImg(self):
        load = Image.open('lena.jpg') # 放置图片路径

        load_xg = load.resize((128, 128))

        render = ImageTk.PhotoImage(load_xg)

        self.img1 = Label(self,image=render)
        self.img1.image=render
        self.img1.place(x=0,y=0)

    def showText(self):
        text = Label(self,text='作者:')
        text.pack()

    # 显示柔化/锐化
    def showSharpenImg(self):
        self.initCom_showSharpenImg()
        img = Image.open("lena.jpg")
        rh = ImageEnhance.Sharpness(img)
        # 负数是柔化 正数是锐化
        rh_img_1 = rh.enhance(-4.0)
        # 放置5张图片  横着放5个
       # load1 = Image.open('1.png')
        load_xg1 = rh_img_1.resize((256, 256))
        render1 = ImageTk.PhotoImage(load_xg1)
        self.img1 = Label(self, image=render1)
        self.img1.image = render1
        self.img1.place(x=0, y=0)

        rh_img_2 = rh.enhance(-2.0)
       # load2 = Image.open('lena.jpg')
        load_xg2 = rh_img_2.resize((256, 256))
        render2 = ImageTk.PhotoImage(load_xg2)
        self.img2 = Label(self, image=render2)
        self.img2.image = render2
        self.img2.place(x=256, y=0)

        # 正常
        load3 = Image.open('lena.jpg')
        load_xg3 = load3.resize((256, 256))
        render3 = ImageTk.PhotoImage(load_xg3)
        self.img3 = Label(self, image=render3)
        self.img3.image = render3
        self.img3.place(x=256+256, y=0)

        # 锐化
        sharp_img1 = rh.enhance(4.0)
        load_xg4 = sharp_img1.resize((256, 256))
        render4 = ImageTk.PhotoImage(load_xg4)
        self.img4 = Label(self, image=render4)
        self.img4.image = render4
        self.img4.place(x=256 + 256+256, y=0)
        # print(type(img))
        sharp_img2 = rh.enhance(7.0)
        load_xg5 = sharp_img2.resize((256, 256))
        render5 = ImageTk.PhotoImage(load_xg5)
        self.img5 = Label(self, image=render5)
        self.img5.image = render5
        self.img5.place(x=256 + 256 + 256+256, y=0)


        pass
    def initCom_showSharpenImg(self):
        if self.img1 != None:
            self.img1.place_forget()
        if self.img2 != None:
            self.img2.place_forget()
        if self.img3 != None:
            self.img3.place_forget()
        if self.img4 != None:
            self.img4.place_forget()
        if self.img5 != None:
            self.img5.place_forget()

    # 对比度/亮度
    """
        g(x,y) = a*f(x,y)+b
        f(x,y)代表源图像x行，y列的像素点的c通道的数值 g(x,y)代表目
        标图像x行，y列的像素点的c通道的数值
        a参数（a>0）表示放大的倍数（一般在0.0~3.0之间）
        b参数一般称为偏置，用来调节亮度
        """
    def contrast_ratio_brightness(self):
        self.initCom_contrast_ratio_brightness()
        # 竖向 亮度不变 对比度发生变换
        # 横向 对比度不变 亮度发生变换
        img = cv.imread("lena.jpg")
        rows, cols, channel = img.shape

        imgList = ['lena1_1.jpg','lena1_2.jpg','lena1_3.jpg','lena1_4.jpg','lena1_5.jpg',
                   'lena2_1.jpg','lena2_2.jpg','lena2_3.jpg','lena2_4.jpg','lena2_5.jpg']

        import os
        # os.path.exists('xxx/xxx/filename')  # True/False
        dst1_1 = img.copy()
        if os.path.exists(imgList[0]):
            pil_img1_1 = Image.open("lena1_1.jpg")
            load_xg1_1 = pil_img1_1.resize((256, 256))
            render1_1 = ImageTk.PhotoImage(load_xg1_1)
            self.img1_1 = Label(self, image=render1_1)
            self.img1_1.image = render1_1
            self.img1_1.place(x=0, y=0)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst1_1[i, j][c] * 1.0 - 100
                        if color > 255:
                            dst1_1[i, j][c] = 255
                        elif color < 0:
                            dst1_1[i, j][c] = 0
                        else:
                            dst1_1[i, j][c] = color

            cv.imwrite('lena1_1.jpg',dst1_1)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img1_1 = Image.open("lena1_1.jpg")
            load_xg1_1 = pil_img1_1.resize((256, 256))
            render1_1 = ImageTk.PhotoImage(load_xg1_1)
            self.img1_1 = Label(self, image=render1_1)
            self.img1_1.image = render1_1
            self.img1_1.place(x=0, y=0)

        dst1_2 = img.copy()
        if os.path.exists(imgList[1]):
            pil_img1_2 = Image.open("lena1_2.jpg")
            load_xg1_2 = pil_img1_2.resize((256, 256))
            render1_2 = ImageTk.PhotoImage(load_xg1_2)
            self.img1_2 = Label(self, image=render1_2)
            self.img1_2.image = render1_2
            self.img1_2.place(x=256, y=0)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst1_2[i, j][c] * 1.0 - 50
                        if color > 255:
                            dst1_2[i, j][c] = 255
                        elif color < 0:
                            dst1_2[i, j][c] = 0
                        else:
                            dst1_2[i, j][c] = color

            cv.imwrite('lena1_2.jpg', dst1_2)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img1_2 = Image.open("lena1_2.jpg")
            load_xg1_2 = pil_img1_2.resize((256, 256))
            render1_2 = ImageTk.PhotoImage(load_xg1_2)
            self.img1_2 = Label(self, image=render1_2)
            self.img1_2.image = render1_2
            self.img1_2.place(x=256, y=0)

        dst1_3 = img.copy()
        if os.path.exists(imgList[2]):
            pil_img1_3 = Image.open("lena1_3.jpg")
            load_xg1_3 = pil_img1_3.resize((256, 256))
            render1_3 = ImageTk.PhotoImage(load_xg1_3)
            self.img1_3 = Label(self, image=render1_3)
            self.img1_3.image = render1_3
            self.img1_3.place(x=256 + 256, y=0)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst1_3[i, j][c] * 1.0 - 0
                        if color > 255:
                            dst1_3[i, j][c] = 255
                        elif color < 0:
                            dst1_3[i, j][c] = 0
                        else:
                            dst1_3[i, j][c] = color

            cv.imwrite('lena1_3.jpg', dst1_3)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img1_3 = Image.open("lena1_3.jpg")
            load_xg1_3 = pil_img1_3.resize((256, 256))
            render1_3 = ImageTk.PhotoImage(load_xg1_3)
            self.img1_3 = Label(self, image=render1_3)
            self.img1_3.image = render1_3
            self.img1_3.place(x=256+256, y=0)

        dst1_4 = img.copy()
        if os.path.exists(imgList[3]):
            pil_img1_4 = Image.open("lena1_4.jpg")
            load_xg1_4 = pil_img1_4.resize((256, 256))
            render1_4 = ImageTk.PhotoImage(load_xg1_4)
            self.img1_4 = Label(self, image=render1_4)
            self.img1_4.image = render1_4
            self.img1_4.place(x=256 + 256 + 256, y=0)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst1_4[i, j][c] * 1.0 + 50
                        if color > 255:
                            dst1_4[i, j][c] = 255
                        elif color < 0:
                            dst1_4[i, j][c] = 0
                        else:
                            dst1_4[i, j][c] = color

            cv.imwrite('lena1_4.jpg', dst1_4)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img1_4 = Image.open("lena1_4.jpg")
            load_xg1_4 = pil_img1_4.resize((256, 256))
            render1_4 = ImageTk.PhotoImage(load_xg1_4)
            self.img1_4 = Label(self, image=render1_4)
            self.img1_4.image = render1_4
            self.img1_4.place(x=256 + 256+256, y=0)

        dst1_5 = img.copy()
        if os.path.exists(imgList[4]):
            pil_img1_5 = Image.open("lena1_5.jpg")
            load_xg1_5 = pil_img1_5.resize((256, 256))
            render1_5 = ImageTk.PhotoImage(load_xg1_5)
            self.img1_5 = Label(self, image=render1_5)
            self.img1_5.image = render1_5
            self.img1_5.place(x=256 + 256 + 256 + 256, y=0)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst1_5[i, j][c] * 1.0 + 100
                        if color > 255:
                            dst1_5[i, j][c] = 255
                        elif color < 0:
                            dst1_5[i, j][c] = 0
                        else:
                            dst1_5[i, j][c] = color

            cv.imwrite('lena1_5.jpg', dst1_5)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img1_5 = Image.open("lena1_5.jpg")
            load_xg1_5 = pil_img1_5.resize((256, 256))
            render1_5 = ImageTk.PhotoImage(load_xg1_5)
            self.img1_5 = Label(self, image=render1_5)
            self.img1_5.image = render1_5
            self.img1_5.place(x=256 + 256 + 256+256, y=0)

        # 加深对比度
        dst2_1 = img.copy()
        if os.path.exists(imgList[5]):
            pil_img2_1 = Image.open("lena2_1.jpg")
            load_xg2_1 = pil_img2_1.resize((256, 256))
            render2_1 = ImageTk.PhotoImage(load_xg2_1)
            self.img2_1 = Label(self, image=render2_1)
            self.img2_1.image = render2_1
            self.img2_1.place(x=0, y=256)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst2_1[i, j][c] * 2.0 - 100
                        if color > 255:
                            dst2_1[i, j][c] = 255
                        elif color < 0:
                            dst2_1[i, j][c] = 0
                        else:
                            dst2_1[i, j][c] = color

            cv.imwrite('lena2_1.jpg', dst2_1)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img2_1 = Image.open("lena2_1.jpg")
            load_xg2_1 = pil_img2_1.resize((256, 256))
            render2_1 = ImageTk.PhotoImage(load_xg2_1)
            self.img2_1 = Label(self, image=render2_1)
            self.img2_1.image = render2_1
            self.img2_1.place(x=0, y=256)

        dst2_2 = img.copy()
        if os.path.exists(imgList[6]):
            pil_img2_2 = Image.open("lena2_2.jpg")
            load_xg2_2 = pil_img2_2.resize((256, 256))
            render2_2 = ImageTk.PhotoImage(load_xg2_2)
            self.img2_2 = Label(self, image=render2_2)
            self.img2_2.image = render2_2
            self.img2_2.place(x=256, y=256)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst2_2[i, j][c] * 2.0 - 50
                        if color > 255:
                            dst2_2[i, j][c] = 255
                        elif color < 0:
                            dst2_2[i, j][c] = 0
                        else:
                            dst2_2[i, j][c] = color

            cv.imwrite('lena2_2.jpg', dst2_2)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img2_2 = Image.open("lena2_2.jpg")
            load_xg2_2 = pil_img2_2.resize((256, 256))
            render2_2 = ImageTk.PhotoImage(load_xg2_2)
            self.img2_2 = Label(self, image=render2_2)
            self.img2_2.image = render2_2
            self.img2_2.place(x=256, y=256)

        dst2_3 = img.copy()
        if os.path.exists(imgList[7]):
            pil_img2_3 = Image.open("lena2_3.jpg")
            load_xg2_3 = pil_img2_3.resize((256, 256))
            render2_3 = ImageTk.PhotoImage(load_xg2_3)
            self.img2_3 = Label(self, image=render2_3)
            self.img2_3.image = render2_3
            self.img2_3.place(x=256 + 256, y=256)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst2_3[i, j][c] * 2.0 - 0
                        if color > 255:
                            dst2_3[i, j][c] = 255
                        elif color < 0:
                            dst2_3[i, j][c] = 0
                        else:
                            dst2_3[i, j][c] = color

            cv.imwrite('lena2_3.jpg', dst2_3)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img2_3 = Image.open("lena2_3.jpg")
            load_xg2_3 = pil_img2_3.resize((256, 256))
            render2_3 = ImageTk.PhotoImage(load_xg2_3)
            self.img2_3 = Label(self, image=render2_3)
            self.img2_3.image = render2_3
            self.img2_3.place(x=256+256, y=256)

        dst2_4 = img.copy()
        if os.path.exists(imgList[8]):
            pil_img2_4 = Image.open("lena2_4.jpg")
            load_xg2_4 = pil_img2_4.resize((256, 256))
            render2_4 = ImageTk.PhotoImage(load_xg2_4)
            self.img2_4 = Label(self, image=render2_4)
            self.img2_4.image = render2_4
            self.img2_4.place(x=256 + 256 + 256, y=256)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst2_4[i, j][c] * 2.0 + 50
                        if color > 255:
                            dst2_4[i, j][c] = 255
                        elif color < 0:
                            dst2_4[i, j][c] = 0
                        else:
                            dst2_4[i, j][c] = color

            cv.imwrite('lena2_4.jpg', dst2_4)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img2_4 = Image.open("lena2_4.jpg")
            load_xg2_4 = pil_img2_4.resize((256, 256))
            render2_4 = ImageTk.PhotoImage(load_xg2_4)
            self.img2_4 = Label(self, image=render2_4)
            self.img2_4.image = render2_4
            self.img2_4.place(x=256+256+256, y=256)

        dst2_5 = img.copy()
        if os.path.exists(imgList[9]):
            pil_img2_5 = Image.open("lena2_5.jpg")
            load_xg2_5 = pil_img2_5.resize((256, 256))
            render2_5 = ImageTk.PhotoImage(load_xg2_5)
            self.img2_5 = Label(self, image=render2_5)
            self.img2_5.image = render2_5
            self.img2_5.place(x=256 + 256 + 256 + 256, y=256)
        else:
            for i in range(rows):
                for j in range(cols):
                    for c in range(3):
                        color = color = dst2_5[i, j][c] * 2.0 + 100
                        if color > 255:
                            dst2_5[i, j][c] = 255
                        elif color < 0:
                            dst2_5[i, j][c] = 0
                        else:
                            dst2_5[i, j][c] = color

            cv.imwrite('lena2_5.jpg', dst2_5)
            # pil_img1_1 = Image.fromarray(np.uint8(dst1_1))
            pil_img2_5 = Image.open("lena2_5.jpg")
            load_xg2_5 = pil_img2_5.resize((256, 256))
            render2_5 = ImageTk.PhotoImage(load_xg2_5)
            self.img2_5 = Label(self, image=render2_5)
            self.img2_5.image = render2_5
            self.img2_5.place(x=256+256+256+256, y=256)

        pass
    def initCom_contrast_ratio_brightness(self):
        if self.img1_1 != None:
            self.img1_1.place_forget()
        if self.img1_2 != None:
            self.img1_2.place_forget()
        if self.img1_3 != None:
            self.img1_3.place_forget()
        if self.img1_4 != None:
            self.img1_4.place_forget()
        if self.img1_5 != None:
            self.img1_5.place_forget()
        if self.img2_1 != None:
            self.img2_1.place_forget()
        if self.img2_2 != None:
            self.img2_2.place_forget()
        if self.img2_3 != None:
            self.img2_3.place_forget()
        if self.img2_4 != None:
            self.img2_4.place_forget()
        if self.img2_5 != None:
            self.img2_5.place_forget()
    # 饱和度
    def saturability(self):
        self.initCom_contrast_ratio_brightness()
        img = Image.open("lena.jpg")
        enh_col = ImageEnhance.Color(img)
        image_colored = enh_col.enhance(0.0)
        # image_colored.show()
        load_xg1 = image_colored.resize((256, 256))
        render1 = ImageTk.PhotoImage(load_xg1)
        self.img1 = Label(self, image=render1)
        self.img1.image = render1
        self.img1.place(x=0, y=0)

        image_colored1_2 = enh_col.enhance(0.5)
        load_xg1_2 = image_colored1_2.resize((256, 256))
        render1_2 = ImageTk.PhotoImage(load_xg1_2)
        self.img1_2 = Label(self, image=render1_2)
        self.img1_2.image = render1_2
        self.img1_2.place(x=256, y=0)

        image_colored1_3 = enh_col.enhance(1.0)
        load_xg1_3 = image_colored1_3.resize((256, 256))
        render1_3 = ImageTk.PhotoImage(load_xg1_3)
        self.img1_3 = Label(self, image=render1_3)
        self.img1_3.image = render1_3
        self.img1_3.place(x=256+256, y=0)

        image_colored1_4 = enh_col.enhance(2.0)
        load_xg1_4 = image_colored1_4.resize((256, 256))
        render1_4 = ImageTk.PhotoImage(load_xg1_4)
        self.img1_4 = Label(self, image=render1_4)
        self.img1_4.image = render1_4
        self.img1_4.place(x=256 + 256+256, y=0)

        image_colored1_5 = enh_col.enhance(3.0)
        load_xg1_5 = image_colored1_5.resize((256, 256))
        render1_5 = ImageTk.PhotoImage(load_xg1_5)
        self.img1_5 = Label(self, image=render1_5)
        self.img1_5.image = render1_5
        self.img1_5.place(x=256 + 256 + 256+256, y=0)
        # self.initCom_saturability()
        pass
    def initCom_saturability(self):
        self.img1_1.place_forget()
        self.img1_2.place_forget()
        self.img1_3.place_forget()
        self.img1_4.place_forget()
        self.img1_5.place_forget()
    # 重新着色
    def rest_img(self):
        # 原图
        self.initCom_contrast_ratio_brightness()
        img = Image.open("lena.jpg")

        # 放置5张图片  横着放5个
        # load1 = Image.open('1.png')
        load_xg1_1 = img.resize((256, 256))
        render1_1 = ImageTk.PhotoImage(load_xg1_1)
        self.img1_1 = Label(self, image=render1_1)
        self.img1_1.image = render1_1
        self.img1_1.place(x=0, y=0)

        # 模式L为灰色图像

        Img1_2 = img.convert('L')
        load_xg1_2 = Img1_2.resize((256, 256))
        render1_2 = ImageTk.PhotoImage(load_xg1_2)
        self.img1_2 = Label(self, image=render1_2)
        self.img1_2.image = render1_2
        self.img1_2.place(x=256, y=0)
        # 自定义灰度界限，大于这个值为黑色

        img = Image.open("lena.jpg")
        Img = img.convert('L')

        # 自定义灰度界限，大于这个值为黑色
        threshold = 100

        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 图片二值化
        photo = Img.point(table, '1')
        photo.save("lenaRes1_3.jpg")

        img1_3 = Image.open("lenaRes1_3.jpg")
        load_xg1_3 = img1_3.resize((256, 256))
        render1_3 = ImageTk.PhotoImage(load_xg1_3)
        self.img1_3 = Label(self, image=render1_3)
        self.img1_3.image = render1_3
        self.img1_3.place(x=256+256, y=0)

        # 自定义灰度界限，大于这个值为黑色
        threshold = 200

        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 图片二值化
        photo4 = Img.point(table, '1')
        photo4.save("lenaRes1_4.jpg")

        img1_4 = Image.open("lenaRes1_4.jpg")
        load_xg1_4 = img1_4.resize((256, 256))
        render1_4 = ImageTk.PhotoImage(load_xg1_4)
        self.img1_4 = Label(self, image=render1_4)
        self.img1_4.image = render1_4
        self.img1_4.place(x=256 + 256+256, y=0)

        import colorsys

        # 输入文件
        filename = 'lena.jpg'
        # 目标色值
        target_hue = 0

        # 读入图片，转化为 RGB 色值
        image = Image.open(filename).convert('RGB')

        # 将 RGB 色值分离
        image.load()
        r, g, b = image.split()
        result_r, result_g, result_b = [], [], []
        # 依次对每个像素点进行处理
        for pixel_r, pixel_g, pixel_b in zip(r.getdata(), g.getdata(), b.getdata()):
            # 转为 HSV 色值
            h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
            # 转回 RGB 色系
            rgb = colorsys.hsv_to_rgb(target_hue, s, v)
            pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
            # 每个像素点结果保存
            result_r.append(pixel_r)
            result_g.append(pixel_g)
            result_b.append(pixel_b)

        r.putdata(result_r)
        g.putdata(result_g)
        b.putdata(result_b)

        # 合并图片
        image = Image.merge('RGB', (r, g, b))
        # 输出图片
        image.save('res5.png')

        img1_5 = Image.open("res5.png")
        load_xg1_5 = img1_5.resize((256, 256))
        render1_5 = ImageTk.PhotoImage(load_xg1_5)
        self.img1_5 = Label(self, image=render1_5)
        self.img1_5.image = render1_5
        self.img1_5.place(x=256 + 256 + 256+256, y=0)
        # self.initCom_saturability()

        pass

    def bin_img(self):
        pass
    def test_fuc(self):
        text = Label(self, text='GUI图形编程')
        text.pack()
        pass

    # init 初始化控件
    def initCom(self):
        self.img1.place_forget()
        self.img1_1.place_forget()
        self.img1_2.place_forget()
        self.img1_3.place_forget()
        self.img1_4.place_forget()
        self.img1_5.place_forget()

        self.img2.place_forget()
        self.img2_1.place_forget()
        self.img2_2.place_forget()
        self.img2_3.place_forget()
        self.img2_4.place_forget()
        self.img2_5.place_forget()


        self.img3.place_forget()
        self.img4.place_forget()
        self.img5.place_forget()



root = Tk()
root.geometry("800x300")
app = Window(root)
root.mainloop()


