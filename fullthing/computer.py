class comp:
    def __init__(self,c_drive_name="C") -> None:
        self.regs = [0,0,0,0,0,0,0,0]
        self.prgm = [9,0,72,0,9,1,101,0,9,2,108,0,9,3,111,0,10,0,0,0,8,0,0,0,10,0,1,0,8,0,0,0,10,0,2,0,8,0,0,0,8,0,0,0,10,0,3,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.CLEARRAM = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.ram = [
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        ]
        self.cd = c_drive_name + ".psh"
        f = open(self.cd,"a+")
        f.close()
    def loadPrgm(self):
        self.prgm = self.ram
    def dtb(self,d1:int):
        return f'{d1:08b}'
    def bitwiseAnd(self,b1:int,b2:int):
        db1 = self.dtb(b1)
        db2 = self.dtb(b2)
        ret = ""
        for i in range(len(db1)):
            if db1[i] == 1 == db2[i]:
                ret += "1"
            else:
                ret += "0"
        return int(ret,2)
    def bitwiseOr(self,b1:int,b2:int):
        db1 = self.dtb(b1)
        db2 = self.dtb(b2)
        ret = ""
        for i in range(len(db1)):
            if db1[i] == 1 or 1 == db2[i]:
                ret += "1"
            else:
                ret += "0"
        return int(ret,2)
    def bitwiseNot(self,b1:int):
        db1 = self.dtb(b1)
        ret = ""
        for i in db1:
            if i == "1":
                ret += "0"
            else:
                ret += "1"
        return int(ret,2)
    def bitwiseXor(self,b1:int,b2:int):
        db1 = self.dtb(b1)
        db2 = self.dtb(b2)
        ret = f'{int(db1)^int(db2)}'
        return int(ret,2)
    def runLine(self,i:int):
        opcode = self.dtb(self.prgm[i])
        if opcode[0] == "0":
            a1 = self.prgm[i+1]
        else:
            a1 = self.regs[self.prgm[i+1]]
        if opcode[1] == "0":
            a2 = self.prgm[i+2]
        else:
            a2 = self.regs[self.prgm[i+2]]
        a3 = self.prgm[i+3]
        cmd = int(opcode[2]+opcode[3]+opcode[4]+opcode[5]+opcode[6]+opcode[7],2)
        if cmd == 1:
            self.regs[a3]=a1+a2
        elif cmd == 2:
            self.regs[a3]=a1-a2
        elif cmd == 3:
            self.regs[a3]=self.bitwiseAnd(a1,a2)
        elif cmd == 4:
            self.regs[a3]=self.bitwiseOr(a1,a2)
        elif cmd == 5:
            self.regs[a3]=self.bitwiseNot(a1)
        elif cmd == 6:
            self.regs[a3]=self.bitwiseXor(a1,a2)
        elif cmd == 7:
            print(self.regs[a1])
        elif cmd == 8:
            print(chr(self.regs[a1]))
        elif cmd == 9:
            self.ram[a1]=a2
        elif cmd == 10:
            self.regs[a1] = self.ram[a2]
        elif cmd == 32 and a1 == a2:
            self.regs[6] = a3
        elif cmd == 33 and a1 != a2:
            self.regs[6] = a3
        elif cmd == 34 and a1 < a2:
            self.regs[6] = a3
        elif cmd == 35 and a1 <= a2:
            self.regs[6] = a3
        elif cmd == 36 and a1 > a2:
            self.regs[6] = a3
        elif cmd == 37 and a1 >= a2:
            self.regs[6] = a3
    def runPrgm(self):
        while self.regs[6] < len(self.prgm):
            i = self.regs[6]
            self.runLine(i)
            self.regs[6] += 4
class AsmInterpreter:
    def __init__(self) -> None:
        pass
    def _parseLine(self,line):
        tokens = []
        token = ""
        
        for i in line:
            if i == " ":
                tokens.append(tokens)
            else:
                token += i
        
        return tokens
    def runLine(self,line):
        tokens = self._parseLine(line)
        if tokens[0] == "MOVE":
            pass
myComp = comp()
myComp.runPrgm()
print(f"{myComp.regs}") # this is f-string for debugging purposes
#print("" if myComp.ram == myComp.CLEARRAM else myComp.ram,end="")