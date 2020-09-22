import math

class Point2D(object):

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return Point2D(self.x * factor, self.y * factor)

    def __div__(self, factor):
        return Point2D(self.x / factor, self.y / factor)

    def __repr__(self):
        return 'Point(%s, %s)' % (self.x, self.y)

    def copy(self, other):
        self.x = other.x
        self.y = other.y

    def distance(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def unit_vector (self):
        return Point2D(self.x,self.y) / self.length()

    def angle (self, other):
        return math.acos((self.x * other.x + self.y * other.y) / (self.length() * other.length()))

    def normal_vector(self, other):
        nv = Point2D()
        nv.x = self.y * other.z - self.z * other.y
        nv.y = self.z * other.x - self.x * other.z
        return nv

class StuntkiteBridle(object):

    def __init__(self, distance_a, distance_b, distance_c, distance_d, length_i, length_u, length_o, length_i_new, length_u_new, length_o_new):

        self.distance_a = distance_a
        self.distance_b = distance_b
        self.distance_c = distance_c
        self.distance_d = distance_d

        self.length_i = length_i
        self.length_u = length_u
        self.length_o = length_o

        self.length_i_new = length_i_new
        self.length_u_new = length_u_new
        self.length_o_new = length_o_new
        
        self.point_a = Point2D()
        self.point_u = Point2D()
        self.point_i = Point2D()
        self.point_o = Point2D()
        
        self.calculate()

    def intersect2circles(selft, point_a, radius_a, point_b, radius_b):
        # A, B = [ x, y ]
        # return = [ Q1, Q2 ] or [ Q ] or [] 
        ABx = point_b.x - point_a.x
        ABy = point_b.y - point_a.y
        ABdist = math.sqrt( ABx * ABx + ABy* ABy )
        if (ABdist == 0):
            # no distance between centers
            return (None, None)
        x = (radius_a*radius_a + ABdist*ABdist - radius_b*radius_b) / (2*ABdist)
        y = radius_a*radius_a - x*x
        if (y < 0):
            # no intersection
            return (None, None)
        if (y > 0):
            y = math.sqrt( y )
            # compute unit vectors ex and ey
            ex0 = ABx / ABdist
            ex1 = ABy / ABdist
            ey0 = -ex1
            ey1 =  ex0
            Q1x = point_a.x + x * ex0
            Q1y = point_a.y + x * ex1
            if (y == 0):
                # one touch point
                return (Point2D(Q1x, Q1y), None)
            # two intersections
            Q2x = Q1x - y * ey0
            Q2y = Q1y - y * ey1
            Q1x += y * ey0
            Q1y += y * ey1
            return (Point2D(Q1x, Q1y), Point2D(Q2x, Q2y))
        
    def intersect2lines(self, P, r, Q, s ):
        # line1 = P + lambda1 * r
        # line2 = Q + lambda2 * s
        # r and s must be normalized (length = 1)
        # returns intersection point O of line1 with line2 = [ Ox, Oy ] 
        # returns null if lines do not intersect or are identical
        PQx = Q.x - P.x
        PQy = Q.y - P.y
        qx = PQx * r.x + PQy * r.y
        qy = PQy * r.x - PQx * r.y
        sx = s.x * r.x + s.y * r.y
        sy = s.y * r.x - s.x * r.y 
        # if lines are identical or do not cross...
        if (sy == 0):
            return null
        a = qx - qy * sx / sy
        return Point2D(P.x + a * r.x, P.y + a * r.y)

    def calculate(self):
        round = lambda x: int(x + 0.5)
        # val = self.Values

        self.point_a.x = 0
        self.point_a.y = 0

        self.point_i.x = 0
        self.point_i.y = self.distance_b

        self.point_u.x = self.distance_a
        self.point_u.y = 0

        self.point_o, self.point_oo = self.intersect2circles( self.point_i, self.distance_c, self.point_u, self.distance_d )

        self.point_io_1, self.point_io_2 = self.intersect2circles( self.point_i, self.length_i, self.point_o, self.length_o )
        self.point_uo_1, self.point_uo_2 = self.intersect2circles( self.point_u, self.length_u, self.point_o, self.length_o )
        vect_io = (self.point_io_1 - self.point_io_2) / self.point_io_1.distance(self.point_io_2)
        vect_uo = (self.point_uo_1 - self.point_uo_2) / self.point_uo_1.distance(self.point_uo_2)
        self.center = self.intersect2lines(self.point_io_1, vect_io, self.point_uo_1, vect_uo) 

        self.point_io_1_new, self.point_io_2_new = self.intersect2circles( self.point_i, self.length_i_new, self.point_o, self.length_o_new )
        self.point_uo_1_new, self.point_uo_2_new = self.intersect2circles( self.point_u, self.length_u_new, self.point_o, self.length_o_new )
        vect_io_new = (self.point_io_1 - self.point_io_2) / self.point_io_1.distance(self.point_io_2)
        vect_uo_new = (self.point_uo_1 - self.point_uo_2) / self.point_uo_1.distance(self.point_uo_2)
        self.center_new = self.intersect2lines(self.point_io_1_new, vect_io_new, self.point_uo_1_new, vect_uo_new)

        a2 = self.length_i * self.length_i
        b = self.point_i.distance(self.center)
        b2 = b * b
        c2 = a2 - b2
        self.center_dist = math.sqrt(c2)

        a2 = self.length_i_new * self.length_i_new
        b = self.point_i.distance(self.center_new)
        b2 = b * b
        c2 = a2 - b2
        self.center_dist_new = math.sqrt(c2)
        