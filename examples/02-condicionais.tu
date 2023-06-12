# Exemplo simples: Se / senao

declare x = 3

se (x == 3) {
    imprima("x é igual a 3")
} senao {
    imprima("x é diferente de 3")
}

# Exemplo simples: Se / ainda se / senao

declare y = 7

se ( y > 10 ) {
    imprima("y é maior que 10")
} ainda se ( y > 5) {
    imprima("y é maior que 5 e menor que 10")
} senao {
    imprima("y é menor que 5")
}

# Exemplo completo: Condicional com operadores lógicos entre expressões

se ((x + y < 10) && (x + y > 5)) {
    imprima("x + y está entre 5 e 10")
} senao {
    imprima("x + y não está entre 5 e 10")
}
