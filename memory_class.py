from unicodedata import name


class memory_sim():
    def __init__(self,parameter,parameter_type):
        self.mem={}
        self.keys=None
        self.width=None
        if isinstance(parameter_type,str)==False:
            raise TypeError("The parameter_type arguement should be either the strings 'list', 'tuple', or 'address width'")
        if parameter_type=="list" or parameter_type=="tuple":
            if isinstance(parameter,list)==False or isinstance(parameter,tuple)==False:
                raise ValueError("The parameter arguement must be a filled(eg not empty) list or tuple")
            elif parameter==[] or parameter==():
                raise ValueError("The parameter arguement must have elements")
            else:
                self.keys=parameter
                for named_key in parameter:
                    if isinstance(named_key,str)==False:
                        raise ValueError("The provided key/s in parameter arguement must be a string")
        elif parameter_type=="address width":
            if isinstance(parameter,int)==False:
                raise TypeError("The parameter arguement must be a positive interger")
            else:
                if parameter<=0:
                    raise ValueError("The parameter arguement must be a positive interger")
                else:
                    self.width=parameter
        else:
            raise ValueError("The parameter_type arguement should be either the strings 'list', 'tuple', or 'address width")
    def mem_write(self,data,target):
        pass