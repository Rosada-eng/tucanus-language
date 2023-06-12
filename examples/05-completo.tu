
defina eh_par(x) {

    enquanto for (x >= 2) {
        x = x-2
    }

    se (x == 0) {
        imprima("É par!")
        retorne 1
    } senao {
        imprima("É ímpar!")
        retorne 0
    }
    
}

eh_par(10)

