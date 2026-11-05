class Bifid:
    
    def __init__(self, n, s):
        if n < 2 or n > 10:
            raise AssertionError("er moet gelden dat 2 <= n <= 10")
        if n * n != len(s):
            raise AssertionError("aantal symbolen komt niet overeen met grootte van het rooster")
        self.sym = [[0] * n for _ in range(n)] 
        for i in range(n):
            for j in range(n):
                self.sym[i][j] = s[i * n + j]

    def symbool(self, rij, kolom):
        if rij >= len(self.sym) or kolom >= len(self.sym[0]) or rij < 0 or kolom < 0:
            raise AssertionError("ongeldige positie in rooster") 
        return self.sym[rij][kolom]

    def positie(self, symbool):
        if len(symbool) != 1:
            raise AssertionError("symbool moet uit 1 karakter bestaan")
        for i in range(len(self.sym)):
            for j in range(len(self.sym)):
                if self.sym[i][j] == symbool:
                    return (i, j)
        raise AssertionError(f"onbekend symbool: '{symbool}'")
    
    def codeer(self, tekst):
        res = ""
        Xs = []
        Ys = []
        for i in tekst:
            x, y = self.positie(i)
            Xs.append(x)
            Ys.append(y)
        Xs.extend(Ys)
        for i in range(0, len(Xs), 2):
            res += self.symbool(Xs[i], Xs[i + 1])
        return res

    def decodeer(self, code):
        res = "" 
        coor = []
        for i in code:
            x, y = self.positie(i)
            coor.append(x)
            coor.append(y)
        mid = len(coor) // 2
        for i in range(len(coor) // 2):
            res += self.symbool(coor[i], coor[mid + i])
        return res
