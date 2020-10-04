#!/usr/bin/env python
'''
Copyright (C) 2016 Ulzburger Kites

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex
import simplestyle
import sys
import datetime
import kitebridle

class KiteBridle(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("", "--kite_name", action="store", type="string", dest="kite_name", default="Kite", help="command line help")
        self.OptionParser.add_option("", "--dist_au", action="store", type="float", dest="dist_au", default=0, help="command line help")
        self.OptionParser.add_option("", "--dist_ai", action="store", type="float", dest="dist_ai", default=0, help="command line help")
        self.OptionParser.add_option("", "--dist_io", action="store", type="float", dest="dist_io", default=0, help="command line help")
        self.OptionParser.add_option("", "--dist_uo", action="store", type="float", dest="dist_uo", default=0, help="command line help")
        self.OptionParser.add_option("", "--inhaul_1", action="store", type="float", dest="inhaul_1", default=0, help="command line help")
        self.OptionParser.add_option("", "--upper_outhaul_1", action="store", type="float", dest="upper_outhaul_1", default=0, help="command line help")
        self.OptionParser.add_option("", "--lower_outhaul_1", action="store", type="float", dest="lower_outhaul_1", default=0, help="command line help")
        self.OptionParser.add_option("", "--inhaul_2", action="store", type="float", dest="inhaul_2", default=0, help="command line help")
        self.OptionParser.add_option("", "--upper_outhaul_2", action="store", type="float", dest="upper_outhaul_2", default=0, help="command line help")
        self.OptionParser.add_option("", "--lower_outhaul_2", action="store", type="float", dest="lower_outhaul_2", default=0, help="command line help")
        self.OptionParser.add_option("", "--active-tab", action="store", type="string", dest="active_tab", default='title', help="Active tab.")

    def add_drawing (self, layer, bridle):
        svg = self.document.getroot()
        doc_width = self.unittouu(svg.get('width'))
        self.doc_1mm = self.unittouu("1mm")
        doc_01mm = self.doc_1mm / 10.0
        color_cross  = '#000000' # black
        color_line = '#999999' # ligth grey
        color_bridle_1 = '#0000FF' # blue
        color_bridle_2 = '#FF0000' # red
        color_circle = '#999999' # ligth grey
        line_width = 0.25
        construction = False # or True
        self.point_0 = kitebridle.Point2D(50 * self.doc_1mm, 50 * self.doc_1mm)

        # basic geometry
        #
        #  A----U
        #  |   / \
        #  |  /   \
        #  | /     \
        #  I--------O
        #
        self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_a, self.point_0 + bridle.point_u, 'Line-AU')
        self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_a, self.point_0 + bridle.point_i, 'Line-AI')
        self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_i, self.point_0 + bridle.point_u, 'Line-IU')
        self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_u, self.point_0 + bridle.point_o, 'Line-UO')
        self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.point_i, 'Line-OI')

        if (construction):
            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_i, bridle.length_i, 'Circle-I' )
            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_u, bridle.length_u, 'Circle-U' )
            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_o, bridle.length_o, 'Circle-O' )
            self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_io_1, self.point_0 + bridle.point_io_2, 'Line-IU')
            self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_uo_1, self.point_0 + bridle.point_uo_2, 'Line-IU')              
            self.draw_bullet(layer, color_line, line_width, self.point_0 + bridle.point_io_1, 'Point-IO1')
            self.draw_bullet(layer, color_line, line_width, self.point_0 + bridle.point_uo_2, 'Point-UO2')

            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_i, bridle.length_i_new, 'Circle-I' )
            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_u, bridle.length_u_new, 'Circle-U' )
            self.draw_circle(layer, color_circle, line_width, self.point_0 + bridle.point_o, bridle.length_o_new, 'Circle-O' )
            self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_io_1_new, self.point_0 + bridle.point_io_2_new, 'Line-IU')
            self.draw_line(layer, color_line, line_width, self.point_0 + bridle.point_uo_1_new, self.point_0 + bridle.point_uo_2_new, 'Line-IU')              
            self.draw_bullet(layer, color_line, line_width, self.point_0 + bridle.point_io_1_new, 'Point-IO1')
            self.draw_bullet(layer, color_line, line_width, self.point_0 + bridle.point_uo_2_new, 'Point-UO2')
            
        # normal
        self.draw_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_i, self.point_0 + bridle.center, 'Line-IC')
        self.draw_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_u, self.point_0 + bridle.center, 'Line-UC')
        self.draw_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.center, 'Line-OC')
        self.draw_bullet(layer, color_bridle_1, line_width, self.point_0 + bridle.center, 'Center')

        # fade
        self.draw_dotted_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_i, self.point_0 + bridle.point_io_2, 'Line-I-Fade')
        self.draw_dotted_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.point_io_2, 'Line-O-Fade')
        self.draw_bullet(layer, color_bridle_1, line_width, self.point_0 + bridle.point_io_2, 'Point-IO2-Fade')

        # backflip
        self.draw_dotted_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_u, self.point_0 + bridle.point_uo_1, 'Line-U-Backflip')
        self.draw_dotted_line(layer, color_bridle_1, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.point_uo_1, 'Line-O-Backflip')
        self.draw_bullet(layer, color_bridle_1, line_width, self.point_0 + bridle.point_uo_1, 'Point-UO1-Backflip')

        # normal, new
        self.draw_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_i, self.point_0 + bridle.center_new, 'Line-IC-new')
        self.draw_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_u, self.point_0 + bridle.center_new, 'Line-UC-new')
        self.draw_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.center_new, 'Line-OC-new')
        self.draw_bullet(layer, color_bridle_2, line_width, self.point_0 + bridle.center_new, 'Center-new')

        # fade, new
        self.draw_dotted_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_i, self.point_0 + bridle.point_io_2_new, 'Line-I-Fade-new')
        self.draw_dotted_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.point_io_2_new, 'Line-O-Fade-new')
        self.draw_bullet(layer, color_bridle_2, line_width, self.point_0 + bridle.point_io_2_new, 'Point-IO2-Fade-new')

        # backflip, new
        self.draw_dotted_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_u, self.point_0 + bridle.point_uo_1_new, 'Line-U-Backflip-new')
        self.draw_dotted_line(layer, color_bridle_2, line_width, self.point_0 + bridle.point_o, self.point_0 + bridle.point_uo_1_new, 'Line-O-Backflip-new')
        self.draw_bullet(layer, color_bridle_2, line_width, self.point_0 + bridle.point_uo_1_new, 'Point-UO1-Backflip-new')

        # crosses
        self.draw_cross(layer, color_cross, line_width, self.point_0 + bridle.point_a, 'Point-A')
        self.draw_cross(layer, color_cross, line_width, self.point_0 + bridle.point_i, 'Point-I')
        self.draw_cross(layer, color_cross, line_width, self.point_0 + bridle.point_u, 'Point-U')
        self.draw_cross(layer, color_cross, line_width, self.point_0 + bridle.point_o, 'Point-O')

        # text
        self.draw_titel(layer, '#FFFFFF', self.point_0 + kitebridle.Point2D(0,-10), self.options.kite_name)
        self.draw_description(layer, '#FFFFFF', self.point_0, bridle)
        self.draw_text(layer, '#FFFFFF', self.point_0 + kitebridle.Point2D(0,60), bridle)

    def draw_path(self, parent, color, width, pstr, name ):
        stroke_width = width * self.unittouu('1mm')
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : 'none' }
        line_attribs = {'style' : simplestyle.formatStyle(line_style), inkex.addNS('label','inkscape') : name, 'd' : 'M' + pstr }
        line = inkex.etree.SubElement(parent, inkex.addNS('path','svg'), line_attribs )

    def draw_line(self, parent, color, width, point_from, point_to, name ):
        pstr = ' ' + str(point_from.x * self.doc_1mm) + ',' + str(point_from.y * self.doc_1mm) +\
               ' ' + str(point_to.x * self.doc_1mm) + ',' + str(point_to.y * self.doc_1mm)
        self.draw_path(parent, color, width, pstr, name)

    def draw_dotted_path(self, parent, color, width, pstr, name ):
        stroke_width = width * self.unittouu('1mm')
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : 'none', 'stroke-miterlimit' : 4, 'stroke-dasharray' : '1,0.5', 'stroke-dashoffset' : 0 }
        line_attribs = {'style' : simplestyle.formatStyle(line_style), inkex.addNS('label','inkscape') : name, 'd' : 'M' + pstr }
        line = inkex.etree.SubElement(parent, inkex.addNS('path','svg'), line_attribs )

    def draw_dotted_line(self, parent, color, width, point_from, point_to, name ):
        pstr = ' ' + str(point_from.x * self.doc_1mm) + ',' + str(point_from.y * self.doc_1mm) +\
               ' ' + str(point_to.x * self.doc_1mm) + ',' + str(point_to.y * self.doc_1mm)
        self.draw_dotted_path(parent, color, width, pstr, name)

    def draw_circle(self, parent, color, width, point, r, name ):
        stroke_width = width * self.unittouu('1mm')
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : 'none' }
        line_attribs = {'style' : simplestyle.formatStyle(line_style), inkex.addNS('label','inkscape') : name, 'cx' :  str(point.x), 'cy' : str(point.y), 'r' : str(r) }
        line = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), line_attribs )           

    def draw_bullet(self, parent, color, width, point, name ):
        stroke_width = 0 * self.unittouu('1mm')
        r = 4*width
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : color }
        line_attribs = {'style' : simplestyle.formatStyle(line_style), inkex.addNS('label','inkscape') : name, 'cx' :  str(point.x), 'cy' : str(point.y), 'r' : str(r) }
        line = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), line_attribs )           

    def draw_cross(self, parent, color, width, point, name):
        # Cross for Point O
        pstr = ' ' + str(( point.x - 10*width ) * self.doc_1mm) + ',' + str(point.y * self.doc_1mm) +\
               ' ' + str(( point.x + 10*width ) * self.doc_1mm) + ',' + str(point.y * self.doc_1mm)
        self.draw_path(parent, color, width, pstr, name)
        pstr = ' ' + str(point.x * self.doc_1mm) + ',' + str(( point.y - 10*width ) * self.doc_1mm) +\
               ' ' + str(point.x * self.doc_1mm) + ',' + str(( point.y + 10*width ) * self.doc_1mm)
        self.draw_path(parent, color, 0.2, pstr, name)

    def draw_description(self, parent, color, point, bridle):
        font_size = 3.5 * self.doc_1mm
        text = inkex.etree.SubElement(parent,inkex.addNS('text','svg'))
        text.set('x', str(point.x + self.doc_1mm * -3))
        text.set('y', str(point.y + self.doc_1mm * -1))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = 'A'
        text = inkex.etree.SubElement(parent,inkex.addNS('text','svg'))
        text.set('x', str(point.x + bridle.point_i.x + self.doc_1mm * -3))
        text.set('y', str(point.y + bridle.point_i.y + self.doc_1mm * -1))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = 'I'
        text = inkex.etree.SubElement(parent,inkex.addNS('text','svg'))
        text.set('x', str(point.x + bridle.point_u.x + self.doc_1mm * 1))
        text.set('y', str(point.y + bridle.point_u.y + self.doc_1mm * -1))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = 'U'
        text = inkex.etree.SubElement(parent,inkex.addNS('text','svg'))
        text.set('x', str(point.x + bridle.point_o.x + self.doc_1mm * 1))
        text.set('y', str(point.y + bridle.point_o.y + self.doc_1mm * -1))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = 'O'

    def draw_titel(self, parent, color, point, kite_name):
        font_size = 5.5 * self.doc_1mm
        text = inkex.etree.SubElement(parent,inkex.addNS('text','svg'))
        text.set('x', str(point.x))
        text.set('y', str(point.y))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = kite_name

    def draw_text(self, parent, color, point, bridle):
        font_size = 2.75 * self.doc_1mm
        flowRoot=inkex.etree.SubElement(parent,inkex.addNS('flowRoot','svg'),{inkex.addNS('space','xml'):'preserve'})
        flowRoot.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size)+';text-anchor:start;text-align:justify;')
        flowRegion=inkex.etree.SubElement(flowRoot,inkex.addNS('flowRegion','svg'))
        rattribs = {'x':str(point.x),'y':str(point.y),'width':str(100*self.doc_1mm),'height':str(80*self.doc_1mm)}
        rect=inkex.etree.SubElement(flowRegion,inkex.addNS('rect','svg'),rattribs)
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "bridle geometry"
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "A to U............ %4.1f cm" %  bridle.distance_a
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "A to I............ %4.1f cm" %  bridle.distance_b
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "I to O............ %4.1f cm" %  bridle.distance_c
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "U to O............ %4.1f cm" %  bridle.distance_d
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = ""
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "bridle legs (blue)"
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "inner............. %4.1f cm" %  bridle.length_i
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "upper............. %4.1f cm" %  bridle.length_u
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "outer............. %4.1f cm" %  bridle.length_o
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "distance.......... %4.1f cm" %  bridle.center_dist
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = ""
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "bridle legs (red)"
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "inner............. %4.1f cm" %  bridle.length_i_new
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "upper............. %4.1f cm" %  bridle.length_u_new
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "outer............. %4.1f cm" %  bridle.length_o_new
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "distance.......... %4.1f cm" %  bridle.center_dist_new
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = ""
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "changes of center"
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "center to spine... %4.1f cm" %  (bridle.center_new.x-bridle.center.x)
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "center to spreader %4.1f cm" %  (bridle.center.y-bridle.center_new.y)
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "distance.......... %4.1f cm" %  (bridle.center_dist_new-bridle.center_dist)
        para = inkex.etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))

    def effect(self):

        bridle = kitebridle.StuntkiteBridle(self.options.dist_au, 
                                            self.options.dist_ai, 
                                            self.options.dist_io, 
                                            self.options.dist_uo,
                                            self.options.inhaul_1, 
                                            self.options.upper_outhaul_1,
                                            self.options.lower_outhaul_1,
                                            self.options.inhaul_2, 
                                            self.options.upper_outhaul_2,
                                            self.options.lower_outhaul_2 )

        svg = self.document.getroot()
        layer = inkex.etree.SubElement(svg, 'g')

        layer.set(inkex.addNS('label', 'inkscape'), self.options.kite_name + ' (' + datetime.datetime.now().strftime('%Y%m%d %H%M%S') + ')' )
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
        self.add_drawing(layer, bridle)

if __name__ == '__main__':
    e = KiteBridle()
    e.affect()

