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

declare resposta1 = maior_que_vinte(25)
imprima(resposta1)

declare resposta2 = maior_que_vinte(15)
imprima(resposta2)
