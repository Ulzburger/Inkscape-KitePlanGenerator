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
import sys
import datetime
import stuntkite

class KitePlan(inkex.GenerateExtension):

    def add_arguments(self, pars):
        pars.add_argument("--tab", default="model")        
        pars.add_argument("--kite_name", action="store", dest="kite_name", default="Kite", help="command line help")
        pars.add_argument("--end_of_spine", action="store", type=int, dest="end_of_spine", default=0, help="command line help")
        pars.add_argument("--nose_cut_width", action="store", type=int, dest="nose_cut_width", default=0, help="command line help")
        pars.add_argument("--tail_cut_width", action="store", type=int, dest="tail_cut_width", default=0, help="command line help")
        pars.add_argument("--upper_center", action="store", type=int, dest="upper_center", default=0, help="command line help")
        pars.add_argument("--lower_center", action="store", type=int, dest="lower_center", default=0, help="command line help")
        pars.add_argument("--end_of_leading_edge", action="store", type=int, dest="end_of_leading_edge", default=0, help="command line help")
        pars.add_argument("--end_of_leading_edge_height", action="store", type=int, dest="end_of_leading_edge_height", default=0, help="command line help")
        pars.add_argument("--wingspan", action="store", type=int, dest="wingspan", default=0, help="command line help")
        pars.add_argument("--standoff_pos_1", action="store", type=int, dest="standoff_pos_1", default=0, help="command line help")
        pars.add_argument("--standoff_len_1", action="store", type=int, dest="standoff_len_1", default=0, help="command line help")
        pars.add_argument("--standoff_offset_1", action="store", type=float, dest="standoff_offset_1", default=0, help="command line help")
        pars.add_argument("--standoff_pos_2", action="store", type=int, dest="standoff_pos_2", default=0, help="command line help")
        pars.add_argument("--standoff_len_2", action="store", type=int, dest="standoff_len_2", default=0, help="command line help")
        pars.add_argument("--standoff_offset_2", action="store", type=float, dest="standoff_offset_2", default=0, help="command line help")
        pars.add_argument("--le_ctrlpt1_x", action="store", type=int, dest="le_ctrlpt1_x", default=0, help="command line help")
        pars.add_argument("--le_ctrlpt1_y", action="store", type=float, dest="le_ctrlpt1_y", default=0, help="command line help")
        pars.add_argument("--le_ctrlpt2_x", action="store", type=int, dest="le_ctrlpt2_x", default=0, help="command line help")
        pars.add_argument("--le_ctrlpt2_y", action="store", type=float, dest="le_ctrlpt2_y", default=0, help="command line help")
        pars.add_argument("--te_ctrlpt_inner", action="store", type=int, dest="te_ctrlpt_inner", default=0, help="command line help")
        pars.add_argument("--te_ctrlpt_outer", action="store", type=int, dest="te_ctrlpt_outer", default=0, help="command line help")
        pars.add_argument("--active-tab", action="store", dest="active_tab", default='title', help="Active tab.")
        pars.add_argument("--render_type", action="store", dest="render_type", default='overview', help="command line help")

    def add_description (self, layer, kite):
        svg = self.document.getroot()
        from lxml import etree
        doc_left = self.svg.unittouu(svg.get('width'))        
        doc_1mm = self.svg.unittouu("1mm")
        font_size = 2.75 * doc_1mm

        x0 = doc_left - 293 * doc_1mm
        y0 = 10 * doc_1mm

        flowRoot=etree.SubElement(layer,inkex.addNS('flowRoot','svg'),{inkex.addNS('space','xml'):'preserve'})
        flowRoot.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size)+';text-anchor:start;text-align:justify;')
        flowRegion=etree.SubElement(flowRoot,inkex.addNS('flowRegion','svg'))
        rattribs = {'x':str(x0),'y':str(y0),'width':str(100*doc_1mm),'height':str(80*doc_1mm)}
        rect=etree.SubElement(flowRegion,inkex.addNS('rect','svg'),rattribs)
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "parameters"
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "end of spine line.................... %4d mm" % kite.Parameters.end_of_spine
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "nose cut width....................... %4d mm" % kite.Parameters.nose_cut_width
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "tail cut width....................... %4d mm" % kite.Parameters.tail_cut_width
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "position of upper spreader........... %4d mm" % kite.Parameters.upper_center
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "position of lower spreader........... %4d mm" % kite.Parameters.lower_center
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "end of leading edge.................. %4d mm" % kite.Parameters.end_of_leading_edge
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "end of leading edge, height.......... %4d mm" % kite.Parameters.end_of_leading_edge_height
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "span width........................... %4d mm" % kite.Parameters.wingspan
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "position of inner standoff........... %4d mm" % kite.Parameters.standoff_pos_1
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "height of inner standoff............. %4d mm" % kite.Parameters.standoff_len_1
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "offset of inner standoff, sail....... %4.1f mm" % kite.Parameters.standoff_offset_1
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "position of outer standoff........... %4d mm" % kite.Parameters.standoff_pos_2
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "height of outer standoff............. %4d mm" % kite.Parameters.standoff_len_2
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "offset of outer standoff, sail....... %4.1f mm" % kite.Parameters.standoff_offset_2
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, upper control point X.. %4d %%" % kite.Parameters.le_ctrlpt1_x
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, upper control point Y.. %4.1f %%" % kite.Parameters.le_ctrlpt1_y
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, lower control point X.. %4d %%" % kite.Parameters.le_ctrlpt2_x
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, lower control point Y.. %4.1f %%" % kite.Parameters.le_ctrlpt2_y
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "trailing edge, inner control point... %4d %%" % kite.Parameters.te_ctrlpt_inner
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "trailing edge, outer control point... %4d %%" % kite.Parameters.te_ctrlpt_outer

        x0 = doc_left - 293 * doc_1mm       
        y0 = 85 * doc_1mm

        flowRoot=etree.SubElement(layer,inkex.addNS('flowRoot','svg'),{inkex.addNS('space','xml'):'preserve'})
        flowRoot.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        flowRegion=etree.SubElement(flowRoot,inkex.addNS('flowRegion','svg'))
        rattribs = {'x':str(x0),'y':str(y0),'width':str(100*doc_1mm),'height':str(80*doc_1mm)}
        rect=etree.SubElement(flowRegion,inkex.addNS('rect','svg'),rattribs)
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "calculated values"
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "total height................ %4d mm" % kite.Values.total_height
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "nose angle.................. %4d deg" % kite.Values.nose_angle
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "inner angle................. %4d deg" % kite.Values.inner_angle
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "upper spreader.............. %4d mm" % kite.Values.upper_spreader_lenght
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "lower spreader.............. %4d mm" % kite.Values.lower_spreader_length
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, upper part.... %4d mm" % kite.Values.le_part1
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, middle part... %4d mm" % kite.Values.le_part2
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge, lower part.... %4d mm" % kite.Values.le_part3
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "spine, upper part........... %4d mm" % kite.Values.spine_part1
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "spine, middle part.......... %4d mm" % kite.Values.spine_part2
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "spine, lower part........... %4d mm" % kite.Values.spine_part3
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "nose cut.................... %4d mm" % kite.Values.nose_cut
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "tail cut.................... %4d mm" % kite.Values.tail_cut
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "cut spine................... %4d mm" % kite.Values.spine
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "cut leading edge............ %4d mm" % kite.Values.leading_edge
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "leading edge height......... %4d mm" % kite.Values.leading_edge_height
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "sail area (projection)...... %4d cm2" % kite.Values.area
        para = etree.SubElement(flowRoot,inkex.addNS('flowPara','svg'))
        para.text = "sail area (plan)............ %4d cm2" % kite.Values.area_plan

        x0 = doc_left - 293 * doc_1mm
        y0 = 7.5 * doc_1mm
        font_size = 5.5 * doc_1mm

        text = etree.SubElement(layer,inkex.addNS('text','svg'))
        text.set('x', str(x0))
        text.set('y', str(y0))
        text.set('style', '-inkscape-font-specification:\'Courier New, Bold\';font-family:\'Courier New\';font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:'+ str(font_size) +';text-anchor:start;text-align:justify;')
        text.text = kite.Parameters.kite_name

    def add_views(self, layer, kite):
        svg = self.document.getroot()
        doc_left = self.svg.unittouu(svg.get('width'))
        doc_1mm = self.svg.unittouu('1mm')
        doc_01mm = doc_1mm / 10.0

        # top view
        x0 = doc_left - 140 * doc_1mm
        y0 = 90 * doc_1mm
        for name, plist in kite.Paths.items():
            color = '#000000'
            if (name in ["LeadingEdgeSecant", "TrailingEdgeSimplified"]):
                continue
            pstr = ''
            for p in plist:
                pstr += ' ' + str(x0 + p.x * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
            self.draw_path(layer, color, 0.3, pstr, name)
            pstr = ''
            for p in plist:
                pstr += ' ' + str(x0 - p.x * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
            self.draw_path(layer, color, 0.3, pstr, name)

        # centroid
        color = '#c4c4c4'
        pstr = ' ' + str(x0 + kite.Values.centroid_x * doc_01mm) + ',' + str(y0 + (kite.Values.centroid_y+5) * doc_01mm) +\
                    ' ' + str(x0 + (kite.Values.centroid_x-5) * doc_01mm) + ',' + str(y0 + kite.Values.centroid_y * doc_01mm) +\
                    ' ' + str(x0 + kite.Values.centroid_x * doc_01mm) + ',' + str(y0 + (kite.Values.centroid_y-5) * doc_01mm) +\
                    ' ' + str(x0 + (kite.Values.centroid_x+5) * doc_01mm) + ',' + str(y0 + kite.Values.centroid_y * doc_01mm) + ' Z '
        self.draw_path(layer, color, 0.3, pstr, 'centroid')

        # front view
        x0 = doc_left - 140 * doc_1mm
        y0 = 205 * doc_1mm
        color = '#000000'
        for name, plist in kite.Paths.items():
            if (name in ['LeadingEdgeSecant', 'TrailingEdgeSimplified', 'UpperSpreader', 'LowerSpreader']):
               continue
            pstr = ''
            for p in plist:
                pstr += ' ' + str(x0 + p.x * doc_01mm) + ',' + str(y0 - p.z * doc_01mm)
            self.draw_path(layer, color, 0.3, pstr, name)
            pstr = ''
            for p in plist:
                pstr += ' ' + str(x0 - p.x * doc_01mm) + ',' + str(y0 - p.z * doc_01mm)
            self.draw_path(layer, color, 0.3, pstr, name)

        # side view
        x0 = doc_left - 5 * doc_1mm
        y0 = 90 * doc_1mm
        color = '#000000'
        for name, plist in kite.Paths.items():
            if (name in ['LeadingEdgeSecant', 'TrailingEdgeSimplified']):
                continue
            pstr = ''
            for p in plist:
                pstr += ' ' + str(x0 - p.z * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
            self.draw_path(layer, color, 0.3, pstr, name)

        # leading edge detail
        x0 = doc_left - 205 * doc_1mm
        y0 = 10 * doc_1mm
        color = '#c4c4c4'
        upper = kite.Values.le_part1 * 2000.0 / kite.Parameters.end_of_leading_edge
        lower = (kite.Values.le_part1 + kite.Values.le_part2) * 2000.0 / kite.Parameters.end_of_leading_edge
        pstr = ' ' + str(x0 + 0 * doc_01mm) + ',' + str(y0 + 0 * doc_01mm) + ' ' + str(x0 + 2000 * doc_01mm) + ',' + str(y0 + 0 * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdge1")
        pstr = ' ' + str(x0 + upper * doc_01mm) + ',' + str(y0 + 0 * doc_01mm) + ' ' + str(x0 + upper * doc_01mm) + ',' + str(y0 + 20 * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdge1")
        pstr = ' ' + str(x0 + lower * doc_01mm) + ',' + str(y0 + 0 * doc_01mm) + ' ' + str(x0 + lower * doc_01mm) + ',' + str(y0 + 20 * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdge1")

        color = '#000000'
        pstr = ' ' + str(x0 - 0 * doc_01mm) + ',' + str(y0 + 0 * doc_01mm) + \
               ' C ' + str(x0 + kite.Parameters.le_ctrlpt1_x  * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt1_y * 20 * doc_01mm) + \
               ' ' + str(x0 + kite.Parameters.le_ctrlpt2_x * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt2_y * 20 * doc_01mm) + \
               ' ' + str(x0 + 2000 * doc_01mm) + ',' + str(y0 + 0 * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdge2")
        color = '#c4c4c4'
        pstr = ' ' + str(x0 + kite.Parameters.le_ctrlpt1_x * 20 * doc_01mm) + ',' + str(y0 - (kite.Parameters.le_ctrlpt1_y+0.25) * 20 * doc_01mm) + \
                ' ' + str(x0 + (kite.Parameters.le_ctrlpt1_x-0.25) * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt1_y * 20 * doc_01mm) + \
                ' ' + str(x0 + kite.Parameters.le_ctrlpt1_x * 20 * doc_01mm) + ',' + str(y0 - (kite.Parameters.le_ctrlpt1_y-0.25) * 20 * doc_01mm) + \
                ' ' + str(x0 + (kite.Parameters.le_ctrlpt1_x+0.25) * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt1_y * 20 * doc_01mm) + ' Z '
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdgeCP1")
        pstr = ' ' + str(x0 + kite.Parameters.le_ctrlpt2_x * 20 * doc_01mm) + ',' + str(y0 - (kite.Parameters.le_ctrlpt2_y+0.25) * 20 * doc_01mm) + \
                ' ' + str(x0 + (kite.Parameters.le_ctrlpt2_x-0.25) * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt2_y * 20 * doc_01mm) + \
                ' ' + str(x0 + kite.Parameters.le_ctrlpt2_x * 20 * doc_01mm) + ',' + str(y0 - (kite.Parameters.le_ctrlpt2_y-0.25) * 20 * doc_01mm) + \
                ' ' + str(x0 + (kite.Parameters.le_ctrlpt2_x+0.25) * 20 * doc_01mm) + ',' + str(y0 - kite.Parameters.le_ctrlpt2_y * 20 * doc_01mm) + ' Z '
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdgeCP1")

        # plan
        x0 = doc_left - 195 * doc_1mm
        y0 = 15 * doc_1mm
        for name, plist in kite.Paths_plan.items():
            if not( name in ['LeadingEdge', 'TrailingEdge'] ):
                if name in ['UpperSpreaderShadow', 'LowerSpreaderShadow', 'LeadingEdgeSecant', 'Nose_Standoff1', 'Nose_Standoff2', 'TrailingEdgeCtrlPts']:
                    color = '#c4c4c4'
                else:
                    color = '#000000'
                pstr = ''
                for p in plist:
                    pstr += ' ' + str(x0 + p.x * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
                self.draw_path(layer, color, 0.3, pstr, name)

        # leading edge
        color = '#000000'
        pstr = ' ' + str(x0 + kite.nose_plan.x * doc_01mm) + ',' + str(y0 + kite.nose_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.le1_plan.x * doc_01mm) + ',' + str(y0 + kite.le1_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.le2_plan.x * doc_01mm) + ',' + str(y0 + kite.le2_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_le_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_le_plan.y * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "LeadingEdge")

        # trailing edge
        pstr = ' ' + str(x0 + kite.tail_plan.x * doc_01mm) + ',' + str(y0 + kite.tail_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.tail_plan.x * doc_01mm) + ',' + str(y0 + kite.tail_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.te1_plan.x * doc_01mm) + ' ' + str(y0 + kite.te1_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.inner_standoff_plan.x * doc_01mm) + ' ' + str(y0 + kite.inner_standoff_plan.y * doc_01mm) + \
               ' L ' + str(x0 + kite.outer_standoff_plan.x * doc_01mm) + ' ' + str(y0 + kite.outer_standoff_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.te2_plan.x * doc_01mm) + ' ' + str(y0 + kite.te2_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "TrailingEdge")

        # nose cut
        color = '#000000'
        pstr = ''
        pstr += ' ' + str(x0 + (kite.nose_plan.x - 5.0) * doc_01mm) + ',' + str(y0 + (kite.nose_plan.y + kite.Values.nose_cut) * doc_01mm)
        pstr += ' ' + str(x0 + (kite.nose_plan.x + kite.Parameters.nose_cut_width / 2.0 + 10.0) * doc_01mm) + ',' + str(y0 + (kite.nose_plan.y + kite.Values.nose_cut) * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "NoseCut")

        # tail cut
        color = '#000000'
        pstr = ''
        pstr += ' ' + str(x0 + (kite.tail_plan.x - 5.0) * doc_01mm) + ',' + str(y0 + (kite.tail_plan.y - kite.Values.tail_cut) * doc_01mm)
        pstr += ' ' + str(x0 + (kite.tail_plan.x + kite.Parameters.tail_cut_width / 2.0 + 10.0) * doc_01mm) + ',' + str(y0 + (kite.tail_plan.y - kite.Values.tail_cut) * doc_01mm)
        self.draw_path(layer, color, 0.3, pstr, "TailCut")

        # centroid
        color = '#c4c4c4'
        pstr = ' ' + str(x0 + kite.Values.centroid_x_plan * doc_01mm) + ',' + str(y0 + (kite.Values.centroid_y_plan+5) * doc_01mm) +\
                    ' ' + str(x0 + (kite.Values.centroid_x_plan-5) * doc_01mm) + ',' + str(y0 + kite.Values.centroid_y_plan * doc_01mm) +\
                    ' ' + str(x0 + kite.Values.centroid_x_plan * doc_01mm) + ',' + str(y0 + (kite.Values.centroid_y_plan-5) * doc_01mm) +\
                    ' ' + str(x0 + (kite.Values.centroid_x_plan+5) * doc_01mm) + ',' + str(y0 + kite.Values.centroid_y_plan * doc_01mm) + ' Z '
        self.draw_path(layer, color, 0.3, pstr, 'Centroid')

    def add_plan (self, layer, kite):
        svg = self.document.getroot()
        doc_1mm = self.svg.unittouu('1mm')
        
        x0 = 20 * doc_1mm
        y0 = self.svg.unittouu(svg.attrib['height']) - (kite.Parameters.end_of_spine + 10) * doc_1mm
        
        for name, plist in kite.Paths_plan.items():
            if not( name in ['LeadingEdgeSecant', 'TrailingEdgeCtrlPts', 'LeadingEdge', 'TrailingEdge'] ):                
                if name in ['UpperSpreaderShadow', 'LowerSpreaderShadow', 'Nose_Standoff1', 'Nose_Standoff2']:
                    color = '#c4c4c4'
                else:
                    color = '#000000'
                pstr = ''
                for p in plist:
                    pstr += ' ' + str(x0 + p.x * doc_1mm) + ',' + str(y0 + p.y * doc_1mm)
                self.draw_path(layer, color, 0.5, pstr, name)

        # leading edge
        color = '#000000'
        pstr = ' ' + str(x0 + kite.nose_plan.x * doc_1mm) + ',' + str(y0 + kite.nose_plan.y * doc_1mm) + \
               ' C ' + str(x0 + kite.le1_plan.x * doc_1mm) + ',' + str(y0 + kite.le1_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.le2_plan.x * doc_1mm) + ',' + str(y0 + kite.le2_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.wingtip_le_plan.x * doc_1mm) + ',' + str(y0 + kite.wingtip_le_plan.y * doc_1mm)
        self.draw_path(layer, color, 0.5, pstr, "LeadingEdge")

        # trailing edge
        pstr = ' ' + str(x0 + kite.tail_plan.x * doc_1mm) + ',' + str(y0 + kite.tail_plan.y * doc_1mm) + \
               ' C ' + str(x0 + kite.tail_plan.x * doc_1mm) + ',' + str(y0 + kite.tail_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.te1_plan.x * doc_1mm) + ' ' + str(y0 + kite.te1_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.inner_standoff_plan.x * doc_1mm) + ' ' + str(y0 + kite.inner_standoff_plan.y * doc_1mm) + \
               ' L ' + str(x0 + kite.outer_standoff_plan.x * doc_1mm) + ' ' + str(y0 + kite.outer_standoff_plan.y * doc_1mm) + \
               ' C ' + str(x0 + kite.te2_plan.x * doc_1mm) + ' ' + str(y0 + kite.te2_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_1mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_1mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_1mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_1mm)
        self.draw_path(layer, color, 0.5, pstr, "TrailingEdge")

        # nose cut
        color = '#000000'
        pstr = ''
        pstr += ' ' + str(x0 + (kite.nose_plan.x - 5.0) * doc_1mm) + ',' + str(y0 + (kite.nose_plan.y + kite.Values.nose_cut) * doc_1mm)
        pstr += ' ' + str(x0 + (kite.nose_plan.x + kite.Parameters.nose_cut_width / 2.0 + 10.0) * doc_1mm) + ',' + str(y0 + (kite.nose_plan.y + kite.Values.nose_cut) * doc_1mm)
        self.draw_path(layer, color, 0.5, pstr, "NoseCut")

        # tail cut
        color = '#000000'
        pstr = ''
        pstr += ' ' + str(x0 + (kite.tail_plan.x - 5.0) * doc_1mm) + ',' + str(y0 + (kite.tail_plan.y - kite.Values.tail_cut) * doc_1mm)
        pstr += ' ' + str(x0 + (kite.tail_plan.x + kite.Parameters.tail_cut_width / 2.0 + 10.0) * doc_1mm) + ',' + str(y0 + (kite.tail_plan.y - kite.Values.tail_cut) * doc_1mm)
        self.draw_path(layer, color, 0.5, pstr, "TailCut")

    def add_texture (self, layer, kite):
        svg = self.document.getroot()
        doc_1mm = self.svg.unittouu('1mm')
        doc_01mm = doc_1mm / 10.0

        x0 = 50 * doc_01mm
        y0 = self.svg.unittouu(svg.attrib['height']) - 1650 * doc_01mm

        # red texture box
        color = '#FF0000'
        pstr = ' ' + str(x0 -   25 * doc_01mm) + ',' + str(y0 -   25 * doc_01mm) + \
               ' ' + str(x0 + 1575 * doc_01mm) + ',' + str(y0 -   25 * doc_01mm) + \
               ' ' + str(x0 + 1575 * doc_01mm) + ',' + str(y0 + 1575 * doc_01mm) + \
               ' ' + str(x0 -   25 * doc_01mm) + ',' + str(y0 + 1575 * doc_01mm) + \
               ' ' + str(x0 -   25 * doc_01mm) + ',' + str(y0 -   25 * doc_01mm)
        self.draw_path_filled(layer, '#FF0000', '#999999', 0.2, pstr, "TextureBox")     
    
        # black leading edge
        color = '#000000'
        pstr = ' ' + str(x0 + kite.nose_plan.x * doc_01mm) + ',' + str(y0 + kite.nose_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.le1_plan.x * doc_01mm) + ',' + str(y0 + kite.le1_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.le2_plan.x * doc_01mm) + ',' + str(y0 + kite.le2_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_le_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_le_plan.y * doc_01mm)
        self.draw_path(layer, color, 5, pstr, "LeadingEdge")

        # black trailing edge
        pstr = ' ' + str(x0 + kite.tail_plan.x * doc_01mm) + ',' + str(y0 + kite.tail_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.tail_plan.x * doc_01mm) + ',' + str(y0 + kite.tail_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.te1_plan.x * doc_01mm) + ' ' + str(y0 + kite.te1_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.inner_standoff_plan.x * doc_01mm) + ' ' + str(y0 + kite.inner_standoff_plan.y * doc_01mm) + \
               ' L ' + str(x0 + kite.outer_standoff_plan.x * doc_01mm) + ' ' + str(y0 + kite.outer_standoff_plan.y * doc_01mm) + \
               ' C ' + str(x0 + kite.te2_plan.x * doc_01mm) + ' ' + str(y0 + kite.te2_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_01mm) + \
               ' ' + str(x0 + kite.wingtip_te_plan.x * doc_01mm) + ',' + str(y0 + kite.wingtip_te_plan.y * doc_01mm)
        self.draw_path(layer, color, 2.5, pstr, "TrailingEdge")  

        # grey shape
        for name, plist in kite.Paths_plan.items():
            if not( name in ['LeadingEdgeSecant', 'TrailingEdgeCtrlPts', 'UpperSpreaderShadow', 'LowerSpreaderShadow', 'Nose_Standoff1', 'Nose_Standoff2'] ):    
                color = '#CCCCCC'
                pstr = ''
                for p in plist:
                    pstr += ' ' + str(x0 + p.x * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
                self.draw_path(layer, color, 0.2, pstr, name)  

        # grey additional lines
        for name, plist in kite.Paths_plan.items():
            if name in ['UpperSpreaderShadow', 'LowerSpreaderShadow', 'Nose_Standoff1', 'Nose_Standoff2']:    
                color = '#CCCCCC'
                pstr = ''
                for p in plist:
                    pstr += ' ' + str(x0 + p.x * doc_01mm) + ',' + str(y0 + p.y * doc_01mm)
                self.draw_path(layer, color, 0.2, pstr, name)    
              
    def write_file(self, kite):
        
        file_out = open( kite.Parameters.kite_name + '.mtl','w')
        text = ''
        text += 'newmtl sail-left\n'
        text += 'Ns 25.0000\n'
        text += 'Ni 1.5000\n'
        text += 'Tr 0.0000\n'
        text += 'Tf 1.0000 1.0000 1.0000\n'
        text += 'illum 2\n'
        text += 'Ka 0.9000 0.9000 0.9000\n'
        text += 'Kd 0.9000 0.9000 0.9000\n'
        text += 'Ks 0.1350 0.1350 0.1350\n'
        text += 'Ke 0.0000 0.0000 0.0000\n'
        text += 'map_Kd ' + kite.Parameters.kite_name + '.png\n'
        text += '\n'
        text += 'newmtl sail-right\n'
        text += 'Ns 25.0000\n'
        text += 'Ni 1.5000\n'
        text += 'Tr 0.0000\n'
        text += 'Tf 1.0000 1.0000 1.0000\n'
        text += 'illum 2\n'
        text += 'Ka 0.9000 0.9000 0.9000\n'
        text += 'Kd 0.9000 0.9000 0.9000\n'
        text += 'Ks 0.1350 0.1350 0.1350\n'
        text += 'Ke 0.0000 0.0000 0.0000\n'
        text += 'map_Kd ' + kite.Parameters.kite_name + '.png\n'
        text += '\n'
        text += 'newmtl carbon\n'
        text += 'Ns 25.0000\n'
        text += 'Ni 1.5000\n'
        text += 'Tr 0.0000\n'
        text += 'Tf 1.0000 1.0000 1.0000\n'
        text += 'illum 2\n'
        text += 'Ka 0.1000 0.1000 0.1000\n'
        text += 'Kd 0.1000 0.1000 0.1000\n'
        text += 'Ks 0.1350 0.1350 0.1350\n'
        text += 'Ke 0.0000 0.0000 0.0000\n'
        file_out.write(text)
        file_out.close()

        file_out = open( kite.Parameters.kite_name + '.obj','w')

        h =  kite.Values.total_height
        v_output = 'v %8.2f %8.2f %8.2f\n'
        text = ''

        text += '# parameters:\n'
        text += '# end of spine line.................... %4d mm\n' % kite.Parameters.end_of_spine
        text += '# nose cut width....................... %4d mm\n' % kite.Parameters.nose_cut_width
        text += '# tail cut width....................... %4d mm\n' % kite.Parameters.tail_cut_width
        text += '# position of upper spreader........... %4d mm\n' % kite.Parameters.upper_center
        text += '# position of lower spreader........... %4d mm\n' % kite.Parameters.lower_center
        text += '# end of leading edge.................. %4d mm\n' % kite.Parameters.end_of_leading_edge
        text += '# end of leading edge, height.......... %4d mm\n' % kite.Parameters.end_of_leading_edge_height
        text += '# span width........................... %4d mm\n' % kite.Parameters.wingspan
        text += '# position of inner standoff........... %4d mm\n' % kite.Parameters.standoff_pos_1
        text += '# length of inner standoff............. %4d mm\n' % kite.Parameters.standoff_len_1
        text += '# offset of inner standoff, sail....... %4.1f mm\n' % kite.Parameters.standoff_offset_1
        text += '# position of outer standoff........... %4d mm\n' % kite.Parameters.standoff_pos_2
        text += '# length of outer standoff............. %4d mm\n' % kite.Parameters.standoff_len_2
        text += '# offset of outer standoff, sail....... %4.1f mm\n' % kite.Parameters.standoff_offset_2
        text += '# leading edge, upper control point X.. %4d %%\n' % kite.Parameters.le_ctrlpt1_x
        text += '# leading edge, upper control point Y.. %4.1f %%\n' % kite.Parameters.le_ctrlpt1_y
        text += '# leading edge, lower control point X.. %4d %%\n' % kite.Parameters.le_ctrlpt2_x
        text += '# leading edge, lower control point Y.. %4.1f %%\n' % kite.Parameters.le_ctrlpt2_y
        text += '# trailing edge, inner control point... %4d %%\n' % kite.Parameters.te_ctrlpt_inner
        text += '# trailing edge, outer control point... %4d %%\n' % kite.Parameters.te_ctrlpt_outer

        # text += 'mtllib ' + kite.Parameters.kite_name + '.mtl' + '\n'
        text += 'mtllib ' + kite.Parameters.kite_name + '.mtl\n'
        
        # left
        text += '# left wing\n'
        for i in range(len(kite.points)-1):
                v = kite.points[i]
                text += v_output % (-v.x, h-v.y, -v.z)
        # right
        text += '# right wing\n'
        for i in range(len(kite.points)-1):
                v = kite.points[i]
                text += v_output % (+v.x, h-v.y, -v.z)
        
        text += '# carbon rods\n'

        # upper spreader, center, left
        d = 1.5
        v = kite.upper_spreader_begin
        text += v_output % (-v.x, h-v.y-d, -v.z-d) # 89
        text += v_output % (-v.x, h-v.y-d, -v.z+d) # 90
        text += v_output % (-v.x, h-v.y+d, -v.z-d) # 91
        text += v_output % (-v.x, h-v.y+d, -v.z+d) # 92

        # upper spreader, segment 2, left
        d = 1.5
        v = kite.upper_spreader_segm2
        text += v_output % (-v.x, h-v.y-d, -kite.upper_spreader_begin.z-d) # 93
        text += v_output % (-v.x, h-v.y-d, -kite.upper_spreader_begin.z+d) # 94
        text += v_output % (-v.x, h-v.y+d, -kite.upper_spreader_begin.z-d) # 95
        text += v_output % (-v.x, h-v.y+d, -kite.upper_spreader_begin.z+d) # 96

        # upper spreader, end, left
        d = 1.5
        v = kite.upper_spreader_end
        text += v_output % (-v.x, h-v.y-d, -v.z-d) #  97
        text += v_output % (-v.x, h-v.y-d, -v.z+d) #  98
        text += v_output % (-v.x, h-v.y+d, -v.z-d) #  99
        text += v_output % (-v.x, h-v.y+d, -v.z+d) # 100

        # upper spreader, segment 2, right
        d = 1.5
        v = kite.upper_spreader_segm2
        text += v_output % ( v.x, h-v.y-d, -kite.upper_spreader_begin.z-d) # 101
        text += v_output % ( v.x, h-v.y-d, -kite.upper_spreader_begin.z+d) # 102
        text += v_output % ( v.x, h-v.y+d, -kite.upper_spreader_begin.z-d) # 103
        text += v_output % ( v.x, h-v.y+d, -kite.upper_spreader_begin.z+d) # 104

        # upper spreader, end, right
        d = 1.5
        v = kite.upper_spreader_end
        text += v_output % ( v.x, h-v.y-d, -v.z-d) # 105
        text += v_output % ( v.x, h-v.y-d, -v.z+d) # 106
        text += v_output % ( v.x, h-v.y+d, -v.z-d) # 107
        text += v_output % ( v.x, h-v.y+d, -v.z+d) # 108

        # lower spreader, center
        d = 2.4
        v = kite.lower_spreader_begin
        text += v_output % (-v.x, h-v.y-d, -v.z-d) # 109
        text += v_output % (-v.x, h-v.y-d, -v.z+d) # 110
        text += v_output % (-v.x, h-v.y+d, -v.z-d) # 111
        text += v_output % (-v.x, h-v.y+d, -v.z+d) # 112

        # lower spreader, segment 2, left
        d = 2.0
        text += v_output % (-kite.outer_standoff.x, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z-d) # 113
        text += v_output % (-kite.outer_standoff.x, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z+d) # 114
        text += v_output % (-kite.outer_standoff.x, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z-d) # 115
        text += v_output % (-kite.outer_standoff.x, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z+d) # 116

        # lower spreader, end, left
        d = 1.6
        v = kite.lower_spreader_end
        text += v_output % (-v.x, h-v.y-d, -v.z-d) # 117
        text += v_output % (-v.x, h-v.y-d, -v.z+d) # 118
        text += v_output % (-v.x, h-v.y+d, -v.z-d) # 119
        text += v_output % (-v.x, h-v.y+d, -v.z+d) # 120

        # lower spreader, segment 2, right
        d = 2.0
        text += v_output % ( kite.outer_standoff.x, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z-d) # 121
        text += v_output % ( kite.outer_standoff.x, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z+d) # 122
        text += v_output % ( kite.outer_standoff.x, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z-d) # 123
        text += v_output % ( kite.outer_standoff.x, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z+d) # 124

        # lower spreader, end, right
        d = 1.6
        v = kite.lower_spreader_end
        text += v_output % ( v.x, h-v.y-d, -v.z-d) # 125
        text += v_output % ( v.x, h-v.y-d, -v.z+d) # 126
        text += v_output % ( v.x, h-v.y+d, -v.z-d) # 127
        text += v_output % ( v.x, h-v.y+d, -v.z+d) # 128

        # standoff 1, left & right
        d = 1.0
        v = kite.inner_standoff
        text += v_output % (-v.x-d, h-v.y-d, -v.z) # 129
        text += v_output % (-v.x-d, h-v.y+d, -v.z) # 130
        text += v_output % (-v.x+d, h-v.y-d, -v.z) # 131
        text += v_output % (-v.x+d, h-v.y+d, -v.z) # 132

        d = 1.0
        text += v_output % (-kite.inner_standoff.x-d, h-kite.lower_spreader_segm1.y-d, -kite.lower_spreader_begin.z) # 133
        text += v_output % (-kite.inner_standoff.x-d, h-kite.lower_spreader_segm1.y+d, -kite.lower_spreader_begin.z) # 134
        text += v_output % (-kite.inner_standoff.x+d, h-kite.lower_spreader_segm1.y-d, -kite.lower_spreader_begin.z) # 135
        text += v_output % (-kite.inner_standoff.x+d, h-kite.lower_spreader_segm1.y+d, -kite.lower_spreader_begin.z) # 136
        
        d = 1.0
        v = kite.inner_standoff
        text += v_output % ( v.x-d, h-v.y-d, -v.z) # 137
        text += v_output % ( v.x-d, h-v.y+d, -v.z) # 138
        text += v_output % ( v.x+d, h-v.y-d, -v.z) # 139
        text += v_output % ( v.x+d, h-v.y+d, -v.z) # 140

        d = 1.0
        text += v_output % ( kite.inner_standoff.x-d, h-kite.lower_spreader_segm1.y-d, -kite.lower_spreader_begin.z) # 141
        text += v_output % ( kite.inner_standoff.x-d, h-kite.lower_spreader_segm1.y+d, -kite.lower_spreader_begin.z) # 142
        text += v_output % ( kite.inner_standoff.x+d, h-kite.lower_spreader_segm1.y-d, -kite.lower_spreader_begin.z) # 143
        text += v_output % ( kite.inner_standoff.x+d, h-kite.lower_spreader_segm1.y+d, -kite.lower_spreader_begin.z) # 144

        # standoff 2 / left & right
        d = 1.0
        v = kite.outer_standoff
        text += v_output % (-v.x-d, h-v.y-d, -v.z) # 145
        text += v_output % (-v.x-d, h-v.y+d, -v.z) # 146
        text += v_output % (-v.x+d, h-v.y-d, -v.z) # 147
        text += v_output % (-v.x+d, h-v.y+d, -v.z) # 148

        d = 1.0
        text += v_output % (-kite.outer_standoff.x-d, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z) # 149
        text += v_output % (-kite.outer_standoff.x-d, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z) # 150
        text += v_output % (-kite.outer_standoff.x+d, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z) # 151
        text += v_output % (-kite.outer_standoff.x+d, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z) # 152

        d = 1.0
        v = kite.outer_standoff
        text += v_output % ( v.x-d, h-v.y-d, -v.z) # 153
        text += v_output % ( v.x-d, h-v.y+d, -v.z) # 154
        text += v_output % ( v.x+d, h-v.y-d, -v.z) # 155
        text += v_output % ( v.x+d, h-v.y+d, -v.z) # 156

        d = 1.0
        text += v_output % ( kite.outer_standoff.x-d, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z) # 157
        text += v_output % ( kite.outer_standoff.x-d, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z) # 158
        text += v_output % ( kite.outer_standoff.x+d, h-kite.lower_spreader_segm2.y-d, -kite.lower_spreader_begin.z) # 159
        text += v_output % ( kite.outer_standoff.x+d, h-kite.lower_spreader_segm2.y+d, -kite.lower_spreader_begin.z) # 160
    
        # texture
        text += '# texture' + '\n'
        for i in range(len(kite.points_plan)-1):
                vt = kite.points_plan[i]
                text += 'vt %5.4f %5.4f\n' % ( (25+vt.x)/1600.0, (1575-vt.y)/1600.0 )

       # left - center, middle, outer
        text += '# left wing\n'
        text += 'usemtl sail-left\n'
        text += 'f 1/1 2/2 3/3 4/4 5/5 6/6 7/7 8/8 9/9 10/10 11/11 12/12 \n'       
        text += 'f 1/1 12/12 13/13\n'
        text += 'f 1/1 13/13 14/14 15/15 16/16 17/17 18/18 19/19 20/20 21/21 22/22 23/23 24/24 25/25 26/26 27/27 28/28 29/29 30/30 31/31 32/32 33/33 34/34 35/35 36/36 37/37 38/38 39/39 40/40 41/41 42/42 43/43\n'

        # right - center, middle, outer
        text += '# right wing\n'
        text += 'usemtl sail-right\n'
        text += 'f 45/1 46/2 47/3 48/4 49/5 50/6 51/7 52/8 53/9 54/10 55/11 56/12\n'
        text += 'f 1/1 56/12 57/13\n'
        text += 'f 1/1 57/13 58/14 59/15 60/16 61/17 62/18 63/19 64/20 65/21 66/22 67/23 68/24 69/25 70/26 71/27 72/28 73/29 74/30 75/31 76/32 77/33 78/34 79/35 80/36 81/37 82/38 83/39 84/40 85/41 86/42 87/43\n'

        text += '# carbon rods\n'
        text += 'usemtl carbon\n'
        text += 'f  89  93  94  90\n'
        text += 'f  91  95  96  92\n'
        text += 'f  89  93  95  91\n'
        text += 'f  90  94  96  92\n'
        
        text += 'f  93  97  98  94\n'
        text += 'f  95  99 100  96\n'
        text += 'f  93  97  99  95\n'
        text += 'f  94  98 100  96\n'

        text += 'f  89 101 102  90\n'
        text += 'f  91 103 104  92\n'
        text += 'f  89 101 103  91\n'
        text += 'f  90 102 104  92\n'

        text += 'f 101 105 106 102\n'
        text += 'f 103 107 108 104\n'
        text += 'f 101 105 107 103\n'
        text += 'f 102 106 108 104\n'

        text += 'f 109 113 114 110\n'
        text += 'f 111 115 116 112\n'
        text += 'f 109 113 115 111\n'
        text += 'f 110 114 116 112\n'

        text += 'f 113 117 118 114\n'
        text += 'f 115 119 120 116\n'
        text += 'f 113 117 119 115\n'
        text += 'f 114 118 120 116\n'

        text += 'f 109 121 122 110\n'
        text += 'f 111 123 124 112\n'
        text += 'f 109 121 123 111\n'
        text += 'f 110 122 124 112\n'

        text += 'f 121 125 126 122\n'
        text += 'f 123 127 128 124\n'
        text += 'f 121 125 127 123\n'
        text += 'f 122 126 128 124\n'

        text += 'f 129 133 134 130\n'
        text += 'f 131 135 136 132\n'
        text += 'f 129 133 135 131\n'
        text += 'f 130 134 136 132\n'

        text += 'f 137 141 142 138\n'
        text += 'f 139 143 144 140\n'
        text += 'f 137 141 143 139\n'
        text += 'f 138 142 144 140\n'

        text += 'f 145 149 150 146\n'
        text += 'f 147 151 152 148\n'
        text += 'f 145 149 151 147\n'
        text += 'f 146 150 152 148\n'

        text += 'f 153 157 158 154\n'
        text += 'f 155 159 160 156\n'
        text += 'f 153 157 159 155\n'
        text += 'f 154 158 160 156\n'

        file_out.write(text)
        file_out.close()

    def draw_path(self, parent, color, width, pstr, name ):
        stroke_width = width * self.svg.unittouu('1mm')
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : 'none' }
        line_attribs = {'style' : str(inkex.Style(line_style)), inkex.addNS('label','inkscape') : name, 'd' : 'M' + pstr }
        from lxml import etree
        line = etree.SubElement(parent, inkex.addNS('path','svg'), line_attribs )
        
    def draw_path_filled(self, parent, color, color_fill, width, pstr, name ):
        stroke_width = width * self.svg.unittouu('1mm')
        line_style = { 'stroke' : color, 'stroke-width' :  stroke_width , 'stroke-linecap' : 'round', 'fill' : color_fill }
        # line_attribs = {'style' : simplestyle.formatStyle(line_style), inkex.addNS('label','inkscape') : name, 'd' : 'M' + pstr }
        line_attribs = {'style' : str(inkex.Style(line_style)), inkex.addNS('label','inkscape') : name, 'd' : 'M' + pstr }        
        from lxml import etree
        line = etree.SubElement(parent, inkex.addNS('path','svg'), line_attribs )

    def effect(self):

        if self.options.standoff_pos_1 >= self.options.standoff_pos_2:
           inkex.errormsg("Position of inner standoffs must be lower equal to outer standoffs.")
        elif abs(self.options.standoff_pos_1 - self.options.standoff_pos_2) <= abs(self.options.standoff_offset_1 - self.options.standoff_offset_2):
           inkex.errormsg("Distance between standoffs must be greater than distance between the offsets of standoffs.")
        elif abs(self.options.standoff_pos_1 - self.options.standoff_pos_2) <= abs(self.options.standoff_len_1 - self.options.standoff_len_2):
           inkex.errormsg("Distance between standoffs must be greater than difference between the length of the standoffs.")
        else:
            Parameters = stuntkite.KiteParameters(self.options.kite_name, datetime.datetime.now().strftime('%Y%m%d %H%M%S'),
                                                  self.options.end_of_spine,
                                                  self.options.nose_cut_width,
                                                  self.options.tail_cut_width,
                                                  self.options.upper_center,
                                                  self.options.lower_center,
                                                  self.options.end_of_leading_edge,
                                                  self.options.end_of_leading_edge_height,
                                                  self.options.wingspan,
                                                  self.options.standoff_pos_1,
                                                  self.options.standoff_len_1,
                                                  self.options.standoff_offset_1,
                                                  self.options.standoff_pos_2,
                                                  self.options.standoff_len_2,
                                                  self.options.standoff_offset_2,
                                                  self.options.le_ctrlpt1_x,
                                                  self.options.le_ctrlpt1_y,
                                                  self.options.le_ctrlpt2_x,
                                                  self.options.le_ctrlpt2_y,
                                                  self.options.te_ctrlpt_inner,
                                                  self.options.te_ctrlpt_outer)

            kite = stuntkite.Stuntkite(Parameters)

            svg = self.document.getroot()
            from lxml import etree
            layer = etree.SubElement(svg, 'g')

            if self.options.render_type == 'overview':
                layer.set(inkex.addNS('label', 'inkscape'), kite.Parameters.kite_name + ' (' + kite.Parameters.date_time + ')' + ' - Overview')
                layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
                self.add_description(layer, kite)
                self.add_views(layer, kite)
                self.write_file(kite)
            
            if self.options.render_type == 'kiteplan':
                layer.set(inkex.addNS('label', 'inkscape'), kite.Parameters.kite_name + ' (' + kite.Parameters.date_time + ')' + ' - Plan')
                layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
                self.add_plan(layer, kite)

            if self.options.render_type == 'texture':
                layer.set(inkex.addNS('label', 'inkscape'), kite.Parameters.kite_name + ' (' + kite.Parameters.date_time + ')' + ' - Texture')
                layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
                self.add_texture(layer, kite)

if __name__ == '__main__':
    KitePlan().run()
