def getParams(self,paramList):
    valuesList=[None]*len(paramList)

    for index, paramName in enumerate(paramList):
        try:
            value=self.params[paramName][0]
            valuesList[index]=value
        except:
            msg="Parameter " + paramName + " is missing"
            self.sendContent("fail", msg)
            return [False] + valuesList

    return [True] + valuesList

def multiplication(self):
    ok,a,b = getParams(self,["a","b"])
    if not ok: return

    try:
        a=float(a)
        b=float(b)
        result=a*b

        reponseData={"a":a,
                     "b":b,
                     "result": result}

        self.sendContent("success", reponseData)
    except:
        self.sendContent("error", "Error during computation")

def addition(self):
    ok,a,b = getParams(self,["a","b"])
    if not ok: return

    try:
        a=float(a)
        b=float(b)
        result=a+b

        reponseData={"a":a,
                     "b":b,
                     "result": result}

        self.sendContent("success", reponseData)
    except:
        self.sendContent("error", "Error during computation")

def racine(self):
    ok,a,b,c = getParams(self,["a","b","c"])
    if not ok: return

    try:
        a=float(a)
        b=float(b)
        c=float(c)
        delta=b*b-4*a*c

        if delta > 0:
            x1=(-b-delta**0.5)/(2*a)
            x2=(-b+delta**0.5)/(2*a)
            reponseData={"Nombres de racines":2,
                         "x1":x1,
                         "x2":x2}
        if delta == 0:
            x=-b/(2*a)
            reponseData={"Nombres de racines":1,
                         "x":x}
        else:
            reponseData={"Nombres de racines dans R":0}

        self.sendContent("success", reponseData)
    except:
        self.sendContent("error", "Error during computation")