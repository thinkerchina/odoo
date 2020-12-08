# -*- coding: utf-8 -*-

from datetime import timedelta #事件可以记录显示到日历中
from odoo import models, fields, api, exceptions,_

     # Thinker:这里模仿developer案例
     # 模型model对应的就是表table或者form
     # 多行多列的基础表以及多对一、一对多的键值关联

     #1，Course课程模型


class Course(models.Model):
     _name = 'testoar.course'
     _description = 'TestOAR Courses'
     #上述两行可以理解为表头

     name = fields.Char(string="标题Title",required=True)
     description = fields.Text() #"这是描述字段啊，description"

     # 增加课程中多对一外键，虚拟部分与Session中多对一呼应
     responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
     
     # 增加一对多外键
     session_ids = fields.One2many(
        'testoar.session', 'course_id', string="Sessions")     
     
     # 复制课程对象，在避免课程名称具有唯一属性unique情况下
     def copy(self, default=None):
          default = dict(default or {})

          copied_count = self.search_count(
               [('name', '=like', u"Copy of {}%".format(self.name))])
          if not copied_count:
              #new_name = u"Copy of {}".format(self.name)              
               new_name = _(u"Copy of {}").format(self.name)
               #上面为多语言而改造
          else:
              #new_name = u"Copy of {} ({})".format(self.name, copied_count)
              new_name = _(u"Copy of {} ({})").format(self.name, copied_count)
              #上面为多语言而改造
          default['name'] = new_name
          return super(Course, self).copy(default)     

    
     # 增加模型约束sql约束核查
     _sql_constraints = [
          ('name_description_check',
          'CHECK(name != description)',
          "The title of the course should not be the description"),

          ('name_unique',
          'UNIQUE(name)',
          "The course title must be unique"),
     ]

     #2，课时模型，后半段定义中有外键关系

class Session(models.Model):
     _name = 'testoar.session'
     _description = "TestOAR Sessions"

     name = fields.Char(required=True)     
     start_date = fields.Date(default=fields.Date.today) #增加起始的默认时间设置
     duration = fields.Float(digits=(6, 2), help="Duration in days")
     seats = fields.Integer(string="Number of seats")
     active = fields.Boolean(default=True) #课时是否可选
     color = fields.Integer() #为看板视图准备的

     
     # 课程外键，课时需要的多对一的外键关联，即该段课时安排的是什么课程
     instructor_id = fields.Many2one('res.partner', string="Instructor",
          domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])     
      #domain增加导师是否可选的过滤
          #domain=[('instructor','=',True)])
      
     course_id = fields.Many2one('testoar.course',
          ondelete='cascade', string="Course", required=True) 
      # instructor_id，导师，course_id，课程

     # 多对多例子，一次课时参加人员
     attendee_ids = fields.Many2many('res.partner', string="Attendees")

     # 数据依赖，数据完整性处理
     taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
     end_date = fields.Date(string="End Date", store=True,
          compute='_get_end_date', inverse='_set_end_date')     # 增加截止日期，方便后续日历处理

     # 增加图标视图显示
     attendees_count = fields.Integer(
          string="Attendees count", compute='_get_attendees_count', store=True)

     # 数据依赖，数据完整性处理
     @api.depends('seats', 'attendee_ids')
     def _taken_seats(self):
          for r in self:
               if not r.seats:
                    r.taken_seats = 0.0
               else:
                    r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
     
     # 数据输入时动态处理，onchange回调函数
     @api.onchange('seats', 'attendee_ids')
     def _verify_valid_seats(self):
          if self.seats < 0:
               return {
                    'warning': {
                         'title': _("Incorrect 'seats' value"),
                         'message': _("The number of available seats may not be negative"),
                    },
               }
          if self.seats < len(self.attendee_ids):
               return {
                    'warning': {
                         'title': _("Too many attendees"),
                         'message': _("Increase seats or remove excess attendees"),
                    },
               }
     # 增加课时的日历显示
     @api.depends('start_date', 'duration')
     def _get_end_date(self):
          for r in self:
               if not (r.start_date and r.duration):
                    r.end_date = r.start_date
                    continue

               # Add duration to start_date, but: Monday + 5 days = Saturday, so
               # subtract one second to get on Friday instead
               duration = timedelta(days=r.duration, seconds=-1)
               r.end_date = r.start_date + duration

     def _set_end_date(self):
          for r in self:
               if not (r.start_date and r.end_date):
                    continue

               # Compute the difference between dates, but: Friday - Monday = 4 days,
               # so add one day to get 5 days instead
               r.duration = (r.end_date - r.start_date).days + 1
     
     # 增加图表视图显示
     @api.depends('attendee_ids')
     def _get_attendees_count(self):
          for r in self:
               r.attendees_count = len(r.attendee_ids)

     # 增加模型python约束的处理
     @api.constrains('instructor_id', 'attendee_ids')
     def _check_instructor_not_in_attendees(self):
          for r in self:
               if r.instructor_id and r.instructor_id in r.attendee_ids:
                    raise exceptions.ValidationError(_("A session's instructor can't be an attendee"))

     
          