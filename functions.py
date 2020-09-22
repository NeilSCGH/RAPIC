def multiplication(self):
    try:
        p="a"
        a=self.params["a"][0]

        p="b"
        b=self.params["b"][0]
    except:
        self.sendContent("fail", "Parameter " + p + " is missing")
        return

    try:
        a=float(a)
        b=float(b)
        result=a*b

        self.sendContent("success", {"result": result})
        return
    except:
        self.sendContent("error", "Error during computation")
        return

def addition(self):
    try:
        p="a"
        a=self.params["a"][0]

        p="b"
        b=self.params["b"][0]
    except:
        self.sendContent("fail", "Parameter " + p + " is missing")
        return

    try:
        a=float(a)
        b=float(b)
        result=a+b

        self.sendContent("success", {"result": result})
        return
    except:
        self.sendContent("error", "Error during computation")
        return
