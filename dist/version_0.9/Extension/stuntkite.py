import math

class KiteParameters(object):

    def __init__(self, kite_name, date_time,
                 end_of_spine, nose_cut_width, tail_cut_width, upper_center, lower_center, end_of_leading_edge, end_of_leading_edge_height, wingspan,
                 standoff_pos_1, standoff_len_1, standoff_offset_1,
                 standoff_pos_2, standoff_len_2, standoff_offset_2,
                 le_ctrlpt1_x, le_ctrlpt1_y, le_ctrlpt2_x, le_ctrlpt2_y, te_ctrlpt_inner, te_ctrlpt_outer):
        self.kite_name = kite_name
        self.date_time = date_time        
        self.end_of_spine = end_of_spine
        self.nose_cut_width = nose_cut_width
        self.tail_cut_width = tail_cut_width
        self.end_of_spine = end_of_spine        
        self.upper_center = upper_center
        self.lower_center = lower_center
        self.end_of_leading_edge = end_of_leading_edge
        self.end_of_leading_edge_height = end_of_leading_edge_height
        self.wingspan = wingspan
        self.standoff_pos_1 = standoff_pos_1
        self.standoff_len_1 = standoff_len_1
        self.standoff_offset_1 = standoff_offset_1
        self.standoff_pos_2 = standoff_pos_2
        self.standoff_len_2 = standoff_len_2
        self.standoff_offset_2 = standoff_offset_2
        self.le_ctrlpt1_x = le_ctrlpt1_x
        self.le_ctrlpt1_y = le_ctrlpt1_y
        self.le_ctrlpt2_x = le_ctrlpt2_x
        self.le_ctrlpt2_y = le_ctrlpt2_y
        self.te_ctrlpt_inner = te_ctrlpt_inner
        self.te_ctrlpt_outer = te_ctrlpt_outer

class KiteValues(object):

    def __init__(self):
        total_height = None
        nose_angle = None
        inner_angle = None
        upper_spreader_lenght = None
        upper_spreader_percent = None
        lower_spreader_length = None
        lower_spreader_percent = None
        le_part1 = None
        le_part2 = None
        le_part3 = None
        spine_part1 = None
        spine_part2 = None
        spine_part3 = None
        radius1 = None
        radius2 = None
        nose_cut = None
        tail_cut = None
        spine = None
        leading_edge = None
        leading_edge_height = None
        area = None
        area_plan = None
        centroid_x = None
        centroid_y = None
        centroid_x_plan = None
        centroid_y_plan = None

class Point3D(object):

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, factor):
        return Point3D(self.x * factor, self.y * factor, self.z * factor)

    def __div__(self, factor):
        return Point3D(self.x / factor, self.y / factor, self.z / factor)

    def __repr__(self):
        return 'Point(%s, %s, %s)' % (self.x, self.y, self.z)
        #return 'Point(%d, %d, %d)' % (self.x, self.y, self.z)

    def copy(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

    def distance(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y) + (self.z - other.z) * (self.z - other.z))

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def unit_vector (self):
        return Point3D(self.x,self.y,self.z) / self.length()

    def angle (self, other):
        return math.acos((self.x * other.x + self.y * other.y + self.z * other.z) / (self.length() * other.length()))

    def normal_vector(self, other):
        nv = Point3D()
        nv.x = self.y * other.z - self.z * other.y
        nv.y = self.z * other.x - self.x * other.z
        nv.z = self.x * other.y - self.y * other.x
        return nv

    def rotate(self, axis, angle):
        u = axis.unit_vector()
        r = Point3D()
        r.x = self.x * (u.x * u.x * (1.0 - math.cos(angle)) + math.cos(angle)) + self.y * (u.x * u.y * (1.0 - math.cos(angle)) - u.z * math.sin(angle)) + self.z * (u.x * u.z * (1.0 - math.cos(angle)) + u.y * math.sin(angle))
        r.y = self.x * (u.y * u.x * (1.0 - math.cos(angle)) + u.z * math.sin(angle)) + self.y * (u.y * u.y * (1.0 - math.cos(angle)) + math.cos(angle)) + self.z * (u.y * u.z * (1.0 - math.cos(angle)) - u.x * math.sin(angle))
        r.z = self.x * (u.z * u.x * (1.0 - math.cos(angle)) - u.y * math.sin(angle)) + self.y * (u.y * u.z * (1.0 - math.cos(angle)) + u.x * math.sin(angle)) + self.z * (u.z * u.z * (1.0 - math.cos(angle)) + math.cos(angle))
        return r

class Bezier:
    def __init__(self, p0, p1, p2, p3):
        self.nose = p0
        self.upper_spreader_begin = p1
        self.lower_spreader_begin = p2
        self.tail = p3

    def value(self, t = 0.0):
        q0 = self.nose + (self.upper_spreader_begin - self.nose) * t
        q1 = self.upper_spreader_begin + (self.lower_spreader_begin - self.upper_spreader_begin) * t
        q2 = self.lower_spreader_begin + (self.tail - self.lower_spreader_begin) * t
        r0 = q0 + (q1 - q0) * t
        r1 = q1 + (q2 - q1) * t
        return r0 + (r1 - r0) * t

class Stuntkite(object):

    def __init__(self, Parameters):
        self.Parameters = Parameters
        self.Values = KiteValues()

        self.nose = Point3D()
        self.upper_spreader_begin = Point3D()
        self.upper_spreader_segm1 = Point3D()
        self.upper_spreader_segm2 = Point3D()
        self.upper_spreader_end = Point3D()
        self.lower_spreader_begin = Point3D()
        self.lower_spreader_segm1 = Point3D()
        self.lower_spreader_segm2 = Point3D()
        self.lower_spreader_end = Point3D()
        self.tail = Point3D()
        self.inner_standoff = Point3D()
        self.outer_standoff = Point3D()
        self.wingtip_le = Point3D()
        self.wingtip_te = Point3D()
        self.standoff2LE = Point3D()

        self.nose_plan = Point3D()
        self.upper_spreader_begin_plan = Point3D()
        self.upper_spreader_segm1_plan = Point3D()
        self.upper_spreader_segm2_plan = Point3D()
        self.lower_spreader_begin_plan = Point3D()
        self.lower_spreader_segm1_plan = Point3D()
        self.lower_spreader_segm2_plan = Point3D()
        self.tail_plan = Point3D()
        self.inner_standoff_plan = Point3D()
        self.outer_standoff_plan = Point3D()
        self.wingtip_le_plan = Point3D()
        self.wingtip_te_plan = Point3D()
        self.lower_spreader_end_plan = Point3D()
        self.upper_spreader_end_plan = Point3D()
        self.standoff2LE_plan = Point3D()
        self.le1_plan = Point3D()
        self.le2_plan = Point3D()
        self.te1_plan = Point3D()
        self.te2_plan = Point3D()
        
        self.le = [Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D()]
        self.te = [Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D()]
        self.le_plan = [Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D()]
        self.te_plan = [Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D(), Point3D()]

        self.Paths = { 'Spine': [self.nose, self.tail],
                       'Nose_Standoff1': [self.nose, self.inner_standoff],
                       'Nose_Standoff2': [self.nose, self.outer_standoff],
                       'LeadingEdgeSecant': [self.nose, self.wingtip_le],
                       'LeadingEdge': [self.le[0], self.le[1], self.le[2], self.le[3], self.le[4], self.le[5], self.le[6], self.le[7], self.le[8], self.le[9], self.le[10], self.le[11], self.le[12], self.le[13], self.le[14], self.le[15], self.le[16], self.le[17], self.le[18], self.le[19], self.le[20]],
                       #'Standoff2_LE': [self.outer_standoff, self.standoff2LE],
                       'TrailingEdgeSimplified': [self.tail, self.inner_standoff, self.outer_standoff, self.wingtip_te, self.wingtip_le],
                       'TrailingEdge': [self.te[0], self.te[1], self.te[2], self.te[3], self.te[4], self.te[5], self.te[6], self.te[7], self.te[8], self.te[9], self.te[10], self.te[11], self.te[12], self.te[13], self.te[14], self.te[15], self.te[16], self.te[17], self.te[18], self.te[19], self.te[20], self.te[21]],
                       'UpperSpreader': [self.upper_spreader_begin, self.upper_spreader_end],
                       'LowerSpreader': [self.lower_spreader_begin, self.lower_spreader_end],
                       #'UpperSpreaderShadow': [self.upper_spreader_begin, self.upper_spreader_segm1, self.upper_spreader_segm2, self.upper_spreader_end],
                       #'LowerSpreaderShadow': [self.lower_spreader_begin, self.lower_spreader_segm1, self.lower_spreader_segm2, self.lower_spreader_end],
                       'Wingtip': [self.wingtip_le, self.wingtip_te]}

        self.points = [self.nose, self.te[0], self.te[1], self.te[2], self.te[3], self.te[4], self.te[5], self.te[6], self.te[7], self.te[8], self.te[9], self.te[10], self.te[11], self.te[12], self.te[13], self.te[14], self.te[15], self.te[16], self.te[17], self.te[18], self.te[19], self.te[20], self.te[21], self.le[20], self.le[19], self.le[18], self.le[17], self.le[16], self.le[15], self.le[14], self.le[13], self.le[12], self.le[11], self.le[10], self.le[9], self.le[8], self.le[7], self.le[6], self.le[5], self.le[4], self.le[3], self.le[2], self.le[1], self.le[0], self.nose]
        # self.points = [self.nose, self.tail, self.wingtip_le, self.nose]

        self.Paths_plan = { 'Spine': [self.nose_plan, self.tail_plan],
                            'Nose_Standoff1': [self.nose_plan, self.inner_standoff_plan],
                            'Nose_Standoff2': [self.nose_plan, self.outer_standoff_plan],
                            'LeadingEdgeSecant': [self.nose_plan, self.wingtip_le_plan],
                            'TrailingEdgeCtrlPts': [self.te1_plan, self.te2_plan],
                            #'BezierTest1':[self.te1_plan, self.inner_standoff_plan, self.outer_standoff_plan, self.te2_plan],
                            'LeadingEdge': [self.le_plan[0], self.le_plan[1], self.le_plan[2], self.le_plan[3], self.le_plan[4], self.le_plan[5], self.le_plan[6], self.le_plan[7], self.le_plan[8], self.le_plan[9], self.le_plan[10], self.le_plan[11], self.le_plan[12], self.le_plan[13], self.le_plan[14], self.le_plan[15], self.le_plan[16], self.le_plan[17], self.le_plan[18], self.le_plan[19], self.le_plan[20]],
                            #'Standoff2_LE': [self.outer_standoff_plan, self.standoff2LE_plan],
                            #'TrailingEdgeSimplified': [self.tail_plan, self.inner_standoff_plan, self.outer_standoff_plan, self.wingtip_te_plan, self.wingtip_le_plan],
                            'TrailingEdge': [self.te_plan[0], self.te_plan[1], self.te_plan[2], self.te_plan[3], self.te_plan[4], self.te_plan[5], self.te_plan[6], self.te_plan[7], self.te_plan[8], self.te_plan[9], self.te_plan[10], self.te_plan[11], self.te_plan[12], self.te_plan[13], self.te_plan[14], self.te_plan[15], self.te_plan[16], self.te_plan[17], self.te_plan[18], self.te_plan[19], self.te_plan[20], self.te_plan[21]],
                            'UpperSpreaderShadow': [self.upper_spreader_begin_plan, self.upper_spreader_segm1_plan, self.upper_spreader_segm2_plan, self.upper_spreader_end_plan],
                            'LowerSpreaderShadow': [self.lower_spreader_begin_plan, self.lower_spreader_segm1_plan, self.lower_spreader_segm2_plan, self.lower_spreader_end_plan],
                            'Wingtip': [self.wingtip_le_plan, self.wingtip_te_plan]}
                            
        self.points_plan = [self.nose_plan, self.te_plan[0], self.te_plan[1], self.te_plan[2], self.te_plan[3], self.te_plan[4], self.te_plan[5], self.te_plan[6], self.te_plan[7], self.te_plan[8], self.te_plan[9], self.te_plan[10], self.te_plan[11], self.te_plan[12], self.te_plan[13], self.te_plan[14], self.te_plan[15], self.te_plan[16], self.te_plan[17], self.te_plan[18], self.te_plan[19], self.te_plan[20], self.te_plan[21], self.le_plan[20], self.le_plan[19], self.le_plan[18], self.le_plan[17], self.le_plan[16], self.le_plan[15], self.le_plan[14], self.le_plan[13], self.le_plan[12], self.le_plan[11], self.le_plan[10], self.le_plan[9], self.le_plan[8], self.le_plan[7], self.le_plan[6], self.le_plan[5], self.le_plan[4], self.le_plan[3], self.le_plan[2], self.le_plan[1], self.le_plan[0], self.nose_plan]

        self.calculate()
        
    def calculate(self):
        round = lambda x: int(x + 0.5)
        par = self.Parameters
        val = self.Values
        width = par.wingspan / 2.0
        height = math.sqrt(par.end_of_leading_edge ** 2 - width ** 2)

        # calculated values
        val.total_height = round(height if par.end_of_spine < height else par.end_of_spine)
        val.nose_angle = round((180 / math.pi) * 2 * math.atan((1.0 * width) / height))
        val.inner_angle = 180 - round((180 / math.pi) * 2 * math.atan((1.0 * par.standoff_len_1) / par.standoff_pos_1))
        val.upper_spreader_lenght = round(2 * par.upper_center / height * width)
        val.upper_spreader_percent = round(100 * par.upper_center / par.end_of_spine)
        val.lower_spreader_length = round(par.lower_center / height * width)
        val.lower_spreader_percent = round(100 * par.lower_center / par.end_of_spine)
        val.le_part1 = math.sqrt(par.upper_center ** 2 + (val.upper_spreader_lenght/2.0) ** 2)
        val.le_part2 = math.sqrt(par.lower_center ** 2 + val.lower_spreader_length ** 2) - val.le_part1
        val.le_part3 = par.end_of_leading_edge - val.le_part2 - val.le_part1
        val.spine_part1 = par.upper_center
        val.spine_part2 = par.lower_center - par.upper_center
        val.spine_part3 = par.end_of_spine - par.lower_center

        # calculate the 3D model
        self.upper_spreader_begin.y = par.upper_center

        self.lower_spreader_begin.y = par.lower_center

        self.tail.y = par.end_of_spine

        self.inner_standoff.x = par.standoff_pos_1
        self.inner_standoff.y = par.lower_center + par.standoff_offset_1
        self.inner_standoff.z = par.standoff_len_1

        self.outer_standoff.x = par.standoff_pos_2
        self.outer_standoff.y = par.lower_center + par.standoff_offset_2
        self.outer_standoff.z = par.standoff_len_2

        self.wingtip_le.x = round(width)
        self.wingtip_le.y = round(height)
        self.wingtip_le.z = par.end_of_leading_edge_height

        # subdivide spreaders into segments
        self.upper_spreader_segm1.x = self.upper_spreader_begin.y * self.inner_standoff.x / self.inner_standoff.y
        self.upper_spreader_segm1.y = self.upper_spreader_begin.y
        self.upper_spreader_segm1.z = self.upper_spreader_begin.y * self.inner_standoff.z / self.inner_standoff.y

        self.upper_spreader_segm2.x = self.upper_spreader_begin.y * self.outer_standoff.x / self.outer_standoff.y
        self.upper_spreader_segm2.y = self.upper_spreader_begin.y
        self.upper_spreader_segm2.z = self.upper_spreader_begin.y * self.outer_standoff.z / self.outer_standoff.y

        self.lower_spreader_segm1.x = self.lower_spreader_begin.y * self.inner_standoff.x / self.inner_standoff.y
        self.lower_spreader_segm1.y = self.lower_spreader_begin.y
        self.lower_spreader_segm1.z = self.lower_spreader_begin.y * self.inner_standoff.z / self.inner_standoff.y

        self.lower_spreader_segm2.x = self.lower_spreader_begin.y * self.outer_standoff.x / self.outer_standoff.y
        self.lower_spreader_segm2.y = self.lower_spreader_begin.y
        self.lower_spreader_segm2.z = self.lower_spreader_begin.y * self.outer_standoff.z / self.outer_standoff.y

        # vector from outer standoff to leading edge
        standoff2LE_length = (self.outer_standoff.x * self.wingtip_le.x + self.outer_standoff.y * self.wingtip_le.y + self.outer_standoff.z * self.wingtip_le.z) / self.wingtip_le.length()
        self.standoff2LE.copy(self.wingtip_le * standoff2LE_length / par.end_of_leading_edge)

        # leading edge
        bp0 = Point3D(0.0, 0.0, 0.0)
        bp1 = Point3D(1.0 * par.le_ctrlpt1_x, par.le_ctrlpt1_y, 0.0)
        bp2 = Point3D(1.0 * par.le_ctrlpt2_x, par.le_ctrlpt2_y, 0.0)
        bp3 = Point3D(100.0, 0.0, 0.0)
        bezier = Bezier(bp0, bp1, bp2, bp3)
        standoff2LE_unit = (self.standoff2LE - self.outer_standoff) * (1.0 / self.outer_standoff.distance(self.standoff2LE))
        le_len = self.wingtip_le.length()
        val.leading_edge_height = 0.0
        for i in range(21):
            bv = bezier.value(i/20.0) / 100
            self.le[i].copy(self.wingtip_le * bv.x + standoff2LE_unit * bv.y * le_len )
            if (bv.y * le_len) > val.leading_edge_height:
                val.leading_edge_height = bv.y * le_len

        # wingtip - trailing egde
        self.wingtip_te.copy(self.wingtip_le - standoff2LE_unit * 25)

        # upper/lower spreader length
        for i in range(20):
            if (self.le[i].y < self.upper_spreader_begin.y) and (self.upper_spreader_begin.y < self.le[i+1].y):
                le_part = self.le[i+1] - self.le[i]
                le_part = le_part * ((self.upper_spreader_begin.y - self.le[i].y) / (self.le[i+1].y - self.le[i].y))
                self.upper_spreader_end.copy(self.le[i] + le_part)
                val.upper_spreader_lenght = self.upper_spreader_begin.distance(self.upper_spreader_end) * 2
            if (self.le[i].y < self.lower_spreader_begin.y) and (self.lower_spreader_begin.y < self.le[i+1].y):
                le_part = self.le[i+1] - self.le[i]
                le_part = le_part * ((self.lower_spreader_begin.y - self.le[i].y) / (self.le[i+1].y - self.le[i].y))
                self.lower_spreader_end.copy(self.le[i] + le_part)
                val.lower_spreader_length = self.lower_spreader_begin.distance(self.lower_spreader_end)

        # calculate the (2D) plan
        self.nose_plan.copy(self.nose)
        self.upper_spreader_begin_plan.copy(self.upper_spreader_begin)
        self.lower_spreader_begin_plan.copy(self.lower_spreader_begin)
        self.tail_plan.copy(self.tail)

         # angle of rotation - spine
        alpha1 = math.atan((1.0 * par.standoff_len_1) / par.standoff_pos_1)

         # angle of rotation - inner standoff
        n1 = self.tail.normal_vector(self.inner_standoff)
        n2 = self.inner_standoff.normal_vector(self.outer_standoff)
        alpha2 = - n1.angle(n2)

        # angle of rotation - outer standoff
        n1 = self.inner_standoff.normal_vector(self.outer_standoff)
        n2 = self.outer_standoff.normal_vector(self.wingtip_le)
        alpha3 = - n1.angle(n2)

        self.inner_standoff_plan.copy(self.inner_standoff.rotate(self.tail_plan, alpha1))
        self.upper_spreader_segm1_plan.copy(self.upper_spreader_segm1.rotate(self.tail_plan, alpha1))
        self.lower_spreader_segm1_plan.copy(self.lower_spreader_segm1.rotate(self.tail_plan, alpha1))
        self.outer_standoff_plan.copy(self.outer_standoff.rotate(self.tail_plan, alpha1).rotate(self.inner_standoff_plan, alpha2))
        self.upper_spreader_segm2_plan.copy(self.upper_spreader_segm2.rotate(self.tail_plan, alpha1).rotate(self.inner_standoff_plan, alpha2))
        self.lower_spreader_segm2_plan.copy(self.lower_spreader_segm2.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2))
        self.wingtip_le_plan.copy(self.wingtip_le.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))
        self.wingtip_te_plan.copy(self.wingtip_te.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))
        self.lower_spreader_end_plan.copy(self.lower_spreader_end.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))
        self.upper_spreader_end_plan.copy(self.upper_spreader_end.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))
        self.standoff2LE_plan.copy(self.standoff2LE.rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))

        # leading edge - polygon from 3D model
        for i in range(21):
            self.le_plan[i].copy(self.le[i].rotate(self.tail_plan,alpha1).rotate(self.inner_standoff_plan,alpha2).rotate(self.outer_standoff_plan,alpha3))

        # leading edge - bezier instead of polygon
        pn = Point3D(self.wingtip_le_plan.y, -self.wingtip_le_plan.x, self.wingtip_le_plan.z)
        self.le1_plan.copy((self.wingtip_le_plan * par.le_ctrlpt1_x + pn * par.le_ctrlpt1_y) / 100)
        self.le2_plan.copy((self.wingtip_le_plan * par.le_ctrlpt2_x + pn * par.le_ctrlpt2_y) / 100)

        # trailing edge
        p = self.outer_standoff_plan - self.inner_standoff_plan
        unit_vector_inner = p.unit_vector() * -1.0
        unit_vector_outer = p.unit_vector()

        # x1 = 100%, law of sines
        beta = self.tail_plan.angle(self.inner_standoff_plan)
        gamma = self.tail_plan.angle(unit_vector_inner)
        x1 = self.inner_standoff_plan.length() * math.sin(beta) / math.sin(gamma)
        bp0 = self.tail
        bp1 = self.tail
        bp2 = self.inner_standoff_plan + unit_vector_inner * x1 * (par.te_ctrlpt_inner / 100.0)
        bp3 = self.inner_standoff_plan
        bezier = Bezier(bp0, bp1, bp2, bp3)
        for i in range(0, 11):
            self.te_plan[i].copy(bezier.value(i/10.0))
        self.te1_plan.copy(bp2)

        # x1 = 100%, law of sines
        beta = self.wingtip_le_plan.angle(self.outer_standoff_plan)
        gamma = self.wingtip_le_plan.angle(unit_vector_outer)
        x1 = self.outer_standoff_plan.length() * math.sin(beta) / math.sin(gamma)
        bp0 = self.outer_standoff_plan
        bp1 = self.outer_standoff_plan + unit_vector_outer * x1 * (par.te_ctrlpt_outer / 100.0)
        bp2 = self.wingtip_te_plan
        bp3 = self.wingtip_te_plan
        bezier = Bezier(bp0, bp1, bp2, bp3)
        for i in range(11, 22):
            self.te_plan[i].copy(bezier.value((i-11)/10.0))
        self.te2_plan.copy(bp1)

        # build trailing edge of 3D model - inner segment
        for i in range(0, 11):
            self.te[i].copy(self.te_plan[i].rotate(self.tail_plan,-alpha1))
            
        # build trailing edge of 3D model - outer segment
        for i in range(11, 22):
            self.te[i].copy(self.te_plan[i].rotate(self.outer_standoff_plan,-alpha3).rotate(self.inner_standoff_plan,-alpha2).rotate(self.tail_plan,-alpha1))

        # tail cut at xx mm width
        tail_width = par.tail_cut_width / 2.0
        lt = tail_width * math.sqrt((self.te_plan[1].y - self.tail_plan.y) ** 2 + (self.te_plan[1].x - self.tail_plan.x) ** 2) / self.te_plan[1].x
        val.tail_cut = math.sqrt(lt ** 2 - tail_width ** 2)

        # nose cut at xx mm width
        nose_width = par.nose_cut_width / 2.0
        ln = nose_width * math.sqrt((self.le_plan[1].y - self.nose_plan.y) ** 2 + (self.le_plan[1].x - self.nose_plan.x) ** 2) / self.le_plan[1].x
        val.nose_cut = math.sqrt(ln ** 2 - nose_width ** 2)

        # cutted spine
        val.spine = self.tail_plan.y - val.nose_cut - val.tail_cut

        # leading edge length
        val.leading_edge = 0
        for i in range(0,20):
            le_segment = self.le_plan[i+1]-self.le_plan[i]
            val.leading_edge += le_segment.length()
        val.leading_edge -= ln
        
        # area of sail projection
        val.area = 0.0
        for i in  range(len(self.points)-1):
            val.area =  val.area + (self.points[i].x + self.points[i+1].x) * (self.points[i].y - self.points[i+1].y)
        if val.area > 0.0:
            val.area = val.area/100.0
        else:
            val.area= -val.area/100.0
            
        # centroid of sail projection
        val.centroid_x = 0.0
        val.centroid_y = 0.0
        for i in  range(len(self.points)-1): 
            f2 = self.points[i].x * self.points[i+1].y - self.points[i+1].x * self.points[i].y
            val.centroid_x = val.centroid_x + (self.points[i].x + self.points[i+1].x) * f2
            val.centroid_y = val.centroid_y + (self.points[i].y + self.points[i+1].y) * f2
        val.centroid_x = - val.centroid_x / (300.0 *  val.area)
        val.centroid_y = - val.centroid_y / (300.0 *  val.area)
            
       # area of sail plan
        val.area_plan = 0.0
        for i in  range(len(self.points_plan)-1):
            val.area_plan =  val.area_plan + (self.points_plan[i].x + self.points_plan[i+1].x) * (self.points_plan[i].y - self.points_plan[i+1].y)
        if val.area_plan > 0.0:
            val.area_plan = val.area_plan/100.0
        else:
            val.area_plan= -val.area_plan/100.0
            
        # centroid of sail plan
        val.centroid_x_plan = 0.0
        val.centroid_y_plan = 0.0
        for i in  range(len(self.points_plan)-1): 
            f2 = self.points_plan[i].x * self.points_plan[i+1].y - self.points_plan[i+1].x * self.points_plan[i].y
            val.centroid_x_plan = val.centroid_x_plan + (self.points_plan[i].x + self.points_plan[i+1].x) * f2
            val.centroid_y_plan = val.centroid_y_plan + (self.points_plan[i].y + self.points_plan[i+1].y) * f2
        val.centroid_x_plan = - val.centroid_x_plan / (300.0 *  val.area_plan)
        val.centroid_y_plan = - val.centroid_y_plan / (300.0 *  val.area_plan)
