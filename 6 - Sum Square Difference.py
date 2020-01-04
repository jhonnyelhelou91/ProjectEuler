#(a + b + c + d + e + f + g + h + i + j)(a + b + c + d + e + f + g + h + i + j) = squares + 
# ab + ac + ad + ae + af + ag + ah + ai + aj +
# ba + bc + bd + be + bf + bg + bh + bi + bj +
# ca + cb + cd + ce + cf + cg + ch + ci + cj +
# da + db + dc + de + df + dg + dh + di + dj +
# ea + eb + ec + ed + ef + eg + eh + ei + ej +
# fa + fb + fc + fd + fe + fg + fh + fi + fj +
# ga + gb + gc + gd + ge + gf + gh + gi + gj +
# ha + hb + hc + hd + he + hf + hg + hi + hj +
# ia + ib + ic + id + ie + if + ig + ih + ij +
# ja + jb + jc + jd + je + jf + jg + jh + ji =
# 2ab + 2ac + 2ad + 2ae + 2af + 2ag + 2ah + 2ai + 2aj
# squares + 2 sum(ai * aj) where i <> j

max = 100
_range = range(1, max + 1)
squares = 0
sumSquared = 0
# simple computation is faster since it O(n) instead of O(n2) for sum (ai * aj)
for x in _range:
    squares += pow(x, 2)
    sumSquared += x

sumSquared = pow(sumSquared, 2)
print(sumSquared - squares)