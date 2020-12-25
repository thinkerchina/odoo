# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

# status_selection = {"cancel","ok","ready","runing","finished","checked",}
class Work(models.Model): 
    _name = 'testsocial.work'
    _description = '测试用工-基础表'

    # _register = False
    # _auto = False
    # _table = False

    _id = 0
    _id_pre = ""
    _status = 0
        
    value2 = 0

    @property
    def ID(self):
        pre_temp = str(datetime.now().date())+str(datetime.now().hour)
        if Work._id_pre == pre_temp:
            Work._id += 1
            value2 = Work._id
        else:
            Work._id = 1
            Work._id_pre = pre_temp
        return (Work._id_pre + str(Work._id))

    @property
    def Status(self, **paralist):
        """
        状态信息：
        动作执行前的条件
        动作执行后的结果
        """
        pass
        return self._status
        
    
    def Offer(self,**paralist):
        """
        主动1：发单
        价值预期
        """
        pass
        return

    def Reserve(self,**parameter_list):
        """
        被动2：抢单
        成本预期
        """
        pass

    def Declare(self,**parameter_list):
        """
        主动3：报单
        """
        pass

    def Order(self,**parameter_list):
        """
        被动4：订单
        """
        pass

    def Entrust(self,**parameter_list):
        """
        主动5：委托
        """
        pass

    def Deal(self,**parameter_list):
        """
        被动6：执行
        """
        pass

    def Submit(self,**parameter_list):
        """
        被动7：提交
        """
        pass

    def Accept(self,**parameter_list):
        """
        被动8：接受
        """
        pass

    def Push(self,**parameter_list):
        """
        主动9：推进
        """
        pass

    def Check(self,**parameter_list):
        """
        被动a：核查
        """
        pass



class Requirement(Work):
    _name = 'testsocial.requirement'
    _description = '测试用工-工需单'

    work_sn = fields.Char(string="需求单号",default="RS0000") #需求单以SH..开头
    #sheet_id = fields.Char(string="需求单号",readonly="True") #需求单以SH..开头
    name = fields.Char(string="需求名称",Default="请填入需求名称",requied="True")     

    #client_response = fields.Boolean(string="响应",Default="0") #Thinker：临时用做服务器与客户不单交互
    
    #work_status = fields.Integer(string="需求状态",default=0) 
    work_status = fields.Selection([("0","草稿"),("8","放弃"),("1","允许抢单"),("2","已收单"),
        ("3","正在施工"),("4","已完工"),("5","交付中"),("6","已验收",),("9","完成")],
        default="0",string="工作状态",)
    #工单进展状态："0开始","1发单/","2收单","3开工","4完工","5交付","6验收","7前阶段","8后阶段","9完成"
    #工单进展状态：0，放弃，1创建，2发单，3收单，4施工，5验收，9结束
    # sheet_status = fields.Selection(string="需求状态",default="ready") #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束

    description = fields.Text(string="需求描述")
    task_time = fields.Float(string="需求预计工时") #工时
    budget = fields.Float(string="业主预算") #金融字段，需求方预算
    #host_budget = fields.Monetary(string="需求预算",currency_field=fields.Default) #金融字段，需求方预算
    address = fields.Char(string="需求地址")
    date_start = fields.Date(string="期望开工") #工作期望起止时间，可以为空
    date_end = fields.Date(string="期望完工")
    
    #辅助程序执行字段
    active = fields.Boolean(string="有效",default=True) #是否有效
    modifiable = fields.Boolean(string="可修改",requied="True") #是否可更改

    #聚合其他表格的字段，工需单由多个工程单满足施工要求    
    #工作关系，上层工作：无，下层工作：工程单
    upwork_id = fields.Integer(default=0,string="无上层工作")
    downwork_ids = fields.One2many("testsocial.project","upwork_id",string="下层工作：工程列表")
    #责任人
    host_id = fields.Many2one('res.users',ondelete='set null', index=True,string="雇主")

    @api.onchange("name")
    def change_work_status(self):       
        #if (self.work_sn == "RS0000"):
        #    self.work_sn = "RS" + Work.ID
        #self.write({"work_status":8}) 
        pass
        
#        if (self["work_status"] == 0):
#            self.write({"work_status":1}) 
#            return {'string':'发单成功'}
#        else:
#            return {'string':'发单失败'} 


    #def offer_sheet(self, cr, uid, ids, context=None):
    def offer_sheet(self):
        self.work_status = "1" 
        
        
    def back_sheet(self):
        i=0
        for rec in self.downwork_ids:
            i+=1
        if i==0:
            self.work_status = "0"

    def reserve_sheet(self):
        self.env['testsocial.project'].create({
            'name':"请尽快处理需求："+self.name,
            'upwork_id':self.id,
            'work_status':"0"
        })
        

class Project(Work):
    _name = 'testsocial.project'
    _description = '测试用工-工程单'

    work_sn = fields.Char(string="工程单号") # readonly="True") #工程单号以PS..开头
    name = fields.Char(string="工程名称",requied="True")
    work_status = fields.Selection([("0","准备中"),("8","投标失败"),("1","已投标"),("2","已收标"),
        ("3","正在施工"),("4","已完工"),("5","交付中"),("6","已验收",),("9","完成")],
        default="0",string="工作状态",)
    #work_status = fields.Integer(string="工程状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束 
    #sheet_status = fields.Selection(string="工程状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束 
    
    description = fields.Text(string="工程描述")
    task_time = fields.Float(string="工程工时") #工时
    budget = fields.Float(string="工程预算") #fields.Monetary(string="工程预算") #工程方预算金额    
    address = fields.Char(string="工程地址")
    date_start = fields.Date(string="预计开工") #工作期望起止时间，可以为空
    date_end = fields.Date(string="预计交工")    

    #辅助程序执行字段
    active = fields.Boolean(string="有效",default=True) #是否有效
    modifiable = fields.Boolean(string="可修改",requied="True") #是否可更改

    #聚合其他表格的字段
    #工作关系，上层工作：工需单，下层工作：工包单
    upwork_id = fields.Many2one("testsocial.requirement",ondelete='set null',string="上层工作：需求列表") #工程单来源于需求单
    downwork_ids = fields.One2many("testsocial.bargain","upwork_id",string="下层工作：工包列表") #工程单后续有工包单，测试用工承包   
    #责任人
    head_id = fields.Many2one('res.users',ondelete='set null', index=True,string="工程工长") #工长id，与创建订单的用户合并

    def declare_sheet(self):
        self.work_status = "1" 
        

    def back_sheet(self):
        self.work_status = "0" 

    def order_sheet(self):
        self.work_status = "2" 
        
    

class Bargain(Work):
    _name = 'testsocial.bargain'
    _description = '测试用工-工包单' #工包单把工作分配给不同的工人，工作单把工人的工作落实到时段

    work_sn = fields.Char(string="工包单号") #,readonly="True")    #工包单号以BS..开头
    name = fields.Char(string="工包名称",requied="True")
    work_status = fields.Selection([("0","准备中"),("8","分包失败"),("1","已发包"),("2","已承包"),
        ("3","工作中"),("4","已完工"),("5","交付中"),("6","已验收",),("9","完成")],
        default="0",string="工作状态",)
    #work_status = fields.Integer(string="工包状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束    
    #sheet_status = fields.Selection(string="工包状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束    

    description = fields.Text(string="工包描述")    
    task_time = fields.Float(string="工包工时") #工时
    budget = fields.Float(string="工包预算") #fields.Monetary(string="工包预算") #预算金额
    address = fields.Char(string="工包地址")
    date_start = fields.Date(string="预计开工") #工作期望起止时间，可以为空
    date_end = fields.Date(string="预计交工")

    #验收
    datetime_check = fields.Datetime(string="验收时间") #验收时间
    
    #关联其他表格的字段
    #工作关系，上层工作：工程单，下层工作：工作单
    upwork_id = fields.Many2one("testsocial.project",ondelete='set null',string="上层工作：工程列表") #工包单来自工程单
    downwork_ids = fields.One2many("testsocial.task","upwork_id",string="下层工作：任务列表") #工包单后续有工作单来施工
    #负责人
    worker_id = fields.Many2one('res.users',ondelete='set null', index=True,string="工程工长") #工长id，与创建订单的用户合并   

    def offer_sheet(self):
        self.work_status = "1" 
        
        
    def back_sheet(self):
        i=0
        for rec in self.downwork_ids:
            i+=1
        if i==0:
            self.work_status = "0"

    def reserve_sheet(self):        
        self.env['testsocial.task'].create({
            'name':"请尽快完善任务内容：" + self.name,
            'upwork_id':self.id,
            'work_status':"0"
        })
     

class Task(Work):
    _name = 'testsocial.task'
    _description = '测试用工-工作单' #工包单把工作分配给不同的工人，工作单把工人的工作落实到时段

    work_sn = fields.Char(string="工作单号") #,readonly="True")    #工作单号WS..
    name = fields.Char(string="工作名称",requied="True")
    work_status = fields.Selection([("0","准备计划"),("8","工作失败"),("1","提交任务计划"),("2","授权工作"),
        ("3","正在施工"),("4","已完工"),("5","交付中"),("6","已验收",),("9","完成")],
        default="0",string="工作状态",)
    #work_status = fields.Integer(string="工作状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束    
    #sheet_status = fields.Selection(string="工作状态",default=1) #工单进展状态：0，放弃，1创建，2招标，3施工，4验收，5，结束    

    description = fields.Text(string="工作说明")
    task_time = fields.Float(string="工时") #工时
    budget = fields.Float(string="工资预算") #fields.Monetary(string="工资") #工资金额，通常由系统规则自动填写
    address = fields.Char(string="工作地址")
    datetime_start = fields.Datetime(string="开工时间") #工作期望起止时间，可以为空
    datetime_end = fields.Datetime(string="交工时间")
    
    #验收
    datetime_check = fields.Datetime(string="验收时间") #验收时间

    #关联其他表格的字段
    #工作关系，上层工作：工包单，下层工作：无
    upwork_id = fields.Many2one("testsocial.bargain",ondelete='set null',string="上层工作：工包列表") #任务单来源于工包单
    downwork_ids =fields.Integer(string="无下层工作")

    #负责人
    worker_id = fields.Many2one('res.users',ondelete='set null', index=True,string="施工工人") #工人id，与创建订单的用户合并

    def declare_sheet(self):
        self.work_status = "1" 
        

    def back_sheet(self):
        self.work_status = "0" 

    def order_sheet(self):
        self.work_status = "2" 
    
    def push_sheet(self):
        self.work_status = "3"

    def deal_sheet(self):
        self.work_status = "4"

    def submit_sheet(self):
        self.work_status = "5"
    def check_sheet(self):
        self.work_status = "9"

class Check(Work):
    _name = 'testsocial.check'
    _description = '测试用工-工收单' #工包单把工作分配给不同的工人，工作单把工人的工作落实到时段
