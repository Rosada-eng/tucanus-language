defina maior_que_vinte(x) {
    declare z
    se (x > 20) {
        imprima("Maior que 20")
        z = 1
    } senao {
        imprima("Menor que 20")
        z = 0
    }

    retorne z
}

declare resposta1 = maior_que_vinte(25) # output: 'Maior que 20'
imprima(resposta1) # output: 1

declare resposta2 = maior_que_vinte(15) # output: 'Menor que 20'
imprima(resposta2) # output: 0
