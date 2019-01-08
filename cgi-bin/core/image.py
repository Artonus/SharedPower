import base64
import os
import uuid

class image:

    def encode(self, image):   
        with open(image, "rb") as imageByte:
            return base64.b64encode(imageByte.read())


    def decode(self, image):
        self.__image = "{0}/temp/{2}.png".format(os.curdir, uuid.uuid4().hex)
        self.tempImage = open(self.__image, "wb")
        self.tempImage.write(base64.b64decode(image))
        self.tempImage.close
        return self.__image
