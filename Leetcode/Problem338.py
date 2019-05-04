class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # (a + bi)(c + di) = ac - bd + adi + bci
        
        real, img = a.split("+")
        real_two, img_two = b.split("+")
        real, img, real_two, img_two = int(real), int(img[:-1]), int(real_two), int(img_two[:-1])
        
        real_out = real*real_two - img*img_two
        img_out = real * img_two + img * real_two 
        return str(real_out) + "+" + str(img_out) + "i"
