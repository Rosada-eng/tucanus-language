
defina eh_par(x) {
    declare v = x / 2
    declare ultima_div = v

    enquanto for (v != 0) {
        ultima_div = v
        v = v / 2
    }

    se (ultima_div == 1) {
        imprima("É par!")
        retorne 1
    } senao {
        imprima("É ímpar!")
        retorne 0
    }
    
}

eh_par(10)

