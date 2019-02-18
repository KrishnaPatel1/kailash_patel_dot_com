#Block ={'red, white', '(empty, full)', '(left, right, up, down)'}
class Block: 
    def __init__(self, color='', dot='', half=''):
        self.color = color
        self.dot = dot
        self.half = half

    def __str__(self):
        #return "half-card: " + self.color + ", " + self.dot + ", other half: " + self.half
        if self.color == '' or self.dot == '' or self.half == '':
            nfs = "[---]"
        else:
            nfs = "[" + self.color[0] + self.dot[0] + self.half[0] + "]"
        return nfs.upper()
