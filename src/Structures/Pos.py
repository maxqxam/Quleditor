from pygame.math import Vector2


class Pos(Vector2) :

    @staticmethod
    def fromTuple( pos: tuple[float, float] ) :
        return Pos(pos[0], pos[1])


    def __init__( self, x: float, y: float ) :
        super().__init__(x, y)


    # def __str__( self ) :
    #     return "[PosObject : ({},{})]".format( self.x, self.y )


    def copy( self ) :
        return Pos(self.x, self.y)


    def reset( self, new_x: float = None, new_y: float = None, should_keep: bool = False ) :
        if should_keep :
            if new_x is None : new_x = self.x
            if new_y is None : new_y = self.y

            self.x, self.y = new_x, new_y
        else :
            if new_x is None : new_x = 0
            if new_y is None : new_y = 0

            self.x, self.y = new_x, new_y

        return self


    def reset_by_tuple( self, pos: tuple[float, float] ) :
        self.x, self.y = pos
        return self


    def get_tuple( self ) :
        return self.x, self.y


    def mult_transform( self, x_mult: float = 1, y_mult: float = 1 ) :
        self.x, self.y = self.x * x_mult, self.y * y_mult
        return self


    def get_mult_transform( self ) :
        return self.copy().mult_transform()

    def flip( self ):
        self.x *= -1
        self.y *= -1
        return self

    def get_flipped( self ):
        return self.copy().flip()

    # determines if both x and y are 0
    def is_origin( self ) -> bool:
        return self.x == 0 and self.y == 0

    def transform( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        if not sum_first :
            self.x *= mult
            self.x += Sum
            self.y *= mult
            self.y += Sum
        else :
            self.x += Sum
            self.x *= mult
            self.y += Sum
            self.y *= mult

        return self


    def get_scale( self ) :
        return Pos(self.x / self.x, self.y / self.x)


    def rescale( self, new_width=False, new_height=False ) :
        if new_width is False and new_height is False or \
                new_width is True and new_height is True:
            raise ValueError("Bad Input")

        if new_width:
            x_scale = new_width / self.x
            self.x, self.y = new_width, self.y * x_scale
        elif new_height:
            y_scale = new_height / self.y
            self.y, self.x = new_height, self.x * y_scale

        return self


    def get_rescaled( self, new_width=None, new_height=None ) :
        return self.copy().rescale(new_width, new_height)


    def get_transformed_pos( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return self.copy().transform(Sum, mult, sum_first)


    def get_transformed_tuple( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return self.copy().transform(Sum, mult, sum_first).get_tuple()


    def transform_max_size( self, max_size ) :
        A = self.copy()
        Max = max_size.copy()

        scale_x = Max.x / A.x
        B = Pos(Max.x,A.y*scale_x)

        if B.y > Max.y:
            scale_y = Max.y / A.y
            B = Pos(A.x*scale_y,Max.y)

        self.x,self.y = B.x,B.y

        return self


    def reverse( self ):
        self.x,self.y = self.y,self.x
        return self


    def join( self, pos ) :
        return Pos(self.x + pos.x, self.y + pos.y)