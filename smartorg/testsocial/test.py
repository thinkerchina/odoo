@api.multi
    def xk_btn(self):
        # --点击选课按钮,然后创建一笔学生课程资料
        res = self.env['res.users'].search([('id', '=', self.env.uid)])  # 获取当前用户的ID
        print(res.login)
        code = res.login  # 获取当前用户的学号
        res = self.env['xksystem.student'].search([('code', '=', code)])  # 以学号获取当前学生头表信息
        if res.id:
            # 检索是否已经选过此门课程
            res_course = self.env['xksystem.studentcourseline'].search(['&', ('student_id', '=', res.id),
                                                                        ('coursecode', '=', self.id)])
            if res_course:
                print('此门课程已被选过了,不能重复选择！')
                raise UserError(('你已经选过了这门课,不能重复选择！'))
            else:
                # 防止大量并发选课,每位学生随机停止0-1秒
                sleep_time = random.random()
                print(sleep_time)
                time.sleep(sleep_time)

                # 检索课程是否已经被选光
                l_sql = "select course_id,count(*) from xksystem_studentcourseline " \
                        "where course_id = %s group by course_id" % (self.id)
                self.env.cr.execute(l_sql)
                dicts = self.env.cr.dictfetchall()
                if len(dicts)==0:
                    havastudent_count = 0
                else:
                    havastudent_count = dicts[0]['count']

                if havastudent_count >= self.studentlimit:
                    raise UserError(('选课学生人数已经超过上限,请选择其他课程！'))

                # 合规,系统进行选课
                vals = {'linenumber': self.env['ir.sequence'].next_by_code('seq.test'), 'student_id': res.id,
                        'course_id': self.id, 'coursecode': self.code,'course_partner':[(6, 0, [2,3])]}       #course_partner字段通过操作many2many字段创建
                self.env['xksystem.studentcourseline'].sudo().create(vals)
        else:
            raise UserError(('此账户不是学生账户,不能选课！'))
        return True