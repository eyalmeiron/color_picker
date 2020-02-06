import cv2
import numpy as np


class ColorRange:
    def __init__(self):
        self.image = None
        self._lower_green = 0
        self._upper_green = 255
        self._lower_red = 0
        self._upper_red = 255
        self._lower_blue = 0
        self._upper_blue = 255

        cv2.namedWindow('edges')

        cv2.createTrackbar('Lower red', 'edges', self._lower_red, 255, self.onchange_lower_red)
        cv2.createTrackbar('Upper red', 'edges', self._upper_red, 255, self.onchange_upper_red)
        cv2.createTrackbar('Lower green', 'edges', self._lower_green, 255, self.onchange_lower_green)
        cv2.createTrackbar('Upper green', 'edges', self._upper_green, 255, self.onchange_upper_green)
        cv2.createTrackbar('lower Blue', 'edges', self._lower_blue, 255, self.onchange_lower_blue)
        cv2.createTrackbar('Upper Blue', 'edges', self._upper_blue, 255, self.onchange_upper_blue)

    def onchange_lower_red(self, pos):
        self._lower_red = pos

    def onchange_upper_red(self, pos):
        self._upper_red = pos

    def onchange_lower_blue(self, pos):
        self._lower_blue = pos

    def onchange_upper_blue(self, pos):
        self._upper_blue = pos

    def onchange_lower_green(self, pos):
        self._lower_green = pos

    def onchange_upper_green(self, pos):
        self._upper_green = pos

    def _render(self):
        lower_color = np.array([self._lower_red, self._lower_green, self._lower_blue])
        upper_color = np.array([self._upper_red, self._upper_green, self._upper_blue])
        mask = cv2.inRange(self.image, lower_color, upper_color)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        vertical_images = np.concatenate((self.image, mask), axis=1)
        cv2.imshow('edges', vertical_images)

    def set_image(self, image):
        self.image = image
        self._render()

    def run(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if frame is None:
                continue

            # cv2.setMouseCallback("edges", click_and_crop)

            frame = cv2.resize(frame, (600, 400))
            self.set_image(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    ColorRange().run()
