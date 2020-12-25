
import datetime

# status_selection = {"cancel","ok","ready","runing","finished","checked",}
class Work(): 
    _name = 'testsocial.work'
    _description = '测试用工-'

    _register = False
    _auto =False

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

