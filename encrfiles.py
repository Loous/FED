import sys
import os
import os.path
import pathlib
import base64
import binascii


class EncrFiles:
    def __init__(self):
        
        self.__data = []
        self._encLevel = []
        self._path = ""
        self._option = ""
        
    def encrb64enc(self, option):
        
        c = 0
        
        for n in range(option):
            for n2 in self._encLevel:
            
                n2 = bytes(n2, "utf-8")
                n3 = base64.b64encode(n2)
                
                self._encLevel[c] = str(self.changeSt(n3), "utf-8")
                
                if c == len(self._encLevel) - 1:
                    c = 0
                    
                else:  
                    c += 1
                
            
        self.wrResult()
        
        print("File encrypted!")
        
        
    def encrb64dec(self):
        
        c = 0
        
        while True:
            x = self._encLevel[c]
            
            try:
                d = self.changeSt(x)
                self._encLevel[c] = str(base64.b64decode(d), "utf-8")
                
            except binascii.Error:
                if c == len(self._encLevel) - 1:
                    print("File decrypted!")
                    break
                
                else:
                    c += 1
                    
        self.wrResult()
            
            
    def fileV(self):
        if os.path.exists(self._path) and pathlib.PurePath(self._path).name.endswith(".txt"):
            if os.path.getsize(self._path) < 2:
                print("The path is empty or have few characters, please get into a file with content")
                
            else:
                return True
            
        else:
            print("The path is wrong or the file doesn't exists")
            
            
    def fileData(self):
        
        if self.fileV():
            with open(self._path, "r") as archivo:
                for n in archivo:
                    self._encLevel.append(n.strip())
                
            return True
        
        
    def innPV(self):
        path = sys.argv
        
        if len(path) == 3:
            self._path = path[1]
            self._option = path[2]
            
            return True
        
        else:
            return False
        
    def wrResult(self):
        with open(self._path, "w") as archivo:
            for n in self._encLevel:
                archivo.writelines(f"{n}\n")
                
                
    def changeSt(self, datastr):
        x = len(datastr)
            
        c = int(x / 2)
        k = datastr[0: c]
        k2 = datastr[c: x]
        
        return (k2 + k)[::-1]
            
            
            
    def MenuEn(self):
        
        if self.innPV():
            if self.fileData():
            
                if self._option == "-e":
                    self.encrb64enc(1)
                    
                elif self._option == "-d":
                    self.encrb64dec()
                    
                else:
                    print("The option entered is not valid")
                    
                    
    
if __name__ == "__main__":
    EncrFiles().MenuEn()
                    
        
                
        
        
        
        
        