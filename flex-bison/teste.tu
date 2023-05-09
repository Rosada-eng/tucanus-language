declare x = 2
declare y = 3 - 2 + 1 - 2 / 4 * 5 + x

declare z = x + y

a = X > Y
b = X < Y
c = X >= Y
d = X <= Y
e = X == Y

se (X == 3) {
    declare x = 2
    declare y = 3 - 2 + 1 - 2 / 4 * 5 + x

} ainda se (Y == 3) {
    imprima("faz algo")
} senao {
    imprima("buuu")
}

se ((a && b) || (c && d)) {
    imprima("faz algo")
} senao {
    imprima("faz nada")
}

se (((a<3) && (b>3)) || ((c<3) && (d>3))) {
    imprima("faz algo")
} senao {
    imprima("faz nada")
}


enquanto for (x < 10) {
    imprima("faz algo")
}

defina funcao (x, y) {
    imprima("faz algo")
}

funcao (x, y)

defina funcao_muito_louca123(x, 123, "abc") {
    imprima("faz algo muito louco")

    retorne 123, "abc", x
}

funcao_muito_louca123(aueieie, 24, "abc")


"tudo azul -- PARSING VÁLIDO"