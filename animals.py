import pygame
import os


class Cow:
    def __init__(self, WINDOW_WIDTH):
        """
            self.image_dir: папка, в которой хранятся анимации
            self.width: длинна спрайта
            self.height: высота спрайта
            self.size: размеры спрайта
            self.image_files: список анимаций
            self.images: список анимаций pygame
            self.current_image_index: номер текущей анимации
            self.is_press: разрешает/запрещает проигрывать анимацию
            self.x: координата спрайта по X
            self.y: координата спрайта по Y
            self.cnt: отвечает за повторное проигрывание анимаций.
                      Если все анимации были проиграны, то возвращаемся
                      к первой анимации (self.current_image_index = 0)
        """

        self.image_dir = "cows"

        self.width = 100
        self.height = 90
        self.size = (self.width, self.height)

        self.image_files = sorted(os.listdir(self.image_dir))
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(self.image_dir, filename)).convert_alpha(), self.size) for filename in
                       sorted(self.image_files, key=len)]
        self.current_image_index = 0
        self.is_press = False
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.x = 830
        self.y = 0
        self.cnt = len(self.image_files) - 1

    def load_win(self):
        if self.current_image_index < self.cnt:
            self.current_image_index += 1
        else:
            self.current_image_index = 0
            self.is_press = False

        return self.is_press, self.current_image_index

    def update(self, window):
        if self.is_press:
            self.load_win()
        window.blit(self.images[self.current_image_index], (self.x, self.y))


class Bull(Cow):
    def __init__(self, WINDOW_WIDTH):
        """
            self.image_dir: папка, в которой хранятся анимации
            self.width: длинна спрайта
            self.height: высота спрайта
            self.size: размеры спрайта
            self.image_files: список анимаций
            self.images: список анимаций pygame
            self.current_image_index: номер текущей анимации
            self.is_press: разрешает/запрещает проигрывать анимацию
            self.x: координата спрайта по X
            self.y: координата спрайта по Y
            self.cnt: отвечает за повторное проигрывание анимаций.
                      Если все анимации были проиграны, то возвращаемся
                      к первой анимации (self.current_image_index = 0)
        """

        super().__init__(Cow)
        self.image_dir = "bulls"

        self.width = 100
        self.height = 80
        self.size = (self.width, self.height)

        self.image_files = sorted(os.listdir(self.image_dir))
        self.images = [pygame.transform.scale(pygame.image.load(os.path.join(self.image_dir, filename)).convert_alpha(), self.size) for filename in
                       sorted(self.image_files, key=len)]
        self.current_image_index = 0
        self.is_press = False
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.x = 85
        self.y = 6
        self.cnt = len(self.images) - 1