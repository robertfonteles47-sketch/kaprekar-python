# Programa: Rotina de Kaprekar (constante 6174)
# autor: Robert Fonteles Martins
# ig: robinqzz
# disciplina: Programação de Computadores
# Objetivo: Encontrar a constante 6174
print("Processo de Kaprekar para números de 4 dígitos")
print("Informe um valor entre 0000 e 9999 (inteiro positivo)")

numero = int(input("Número: "))

# -------- VALIDAÇÃO INICIAL --------
if numero < 0:
    print("Erro: valor negativo não é permitido.")

elif numero > 9999:
    print("Erro: o número deve ter no máximo 4 dígitos.")

else:
    milhar = numero // 1000
    centena = (numero // 100) % 10
    dezena = (numero // 10) % 10
    unidade = numero % 10

    if (milhar == centena == dezena) or \
       (milhar == centena == unidade) or \
       (milhar == dezena == unidade) or \
       (centena == dezena == unidade):

        print("Erro: o número possui muitos dígitos iguais.")

    else:
        print("")
        print("Valor inicial:", numero)

        passos = 0

        # -------- PROCESSO --------
        while numero != 6174:

            milhar = numero // 1000
            centena = (numero // 100) % 10
            dezena = (numero // 10) % 10
            unidade = numero % 10

            # Crescente
            a = milhar
            b = centena
            c = dezena
            d = unidade

            if a > b: a, b = b, a
            if a > c: a, c = c, a
            if a > d: a, d = d, a
            if b > c: b, c = c, b
            if b > d: b, d = d, b
            if c > d: c, d = d, c

            menor = a * 1000 + b * 100 + c * 10 + d

            # Decrescente
            a = milhar
            b = centena
            c = dezena
            d = unidade

            if a < b: a, b = b, a
            if a < c: a, c = c, a
            if a < d: a, d = d, a
            if b < c: b, c = c, b
            if b < d: b, d = d, b
            if c < d: c, d = d, c

            maior = a * 1000 + b * 100 + c * 10 + d

            resultado = maior - menor
            passos = passos + 1

            # Separação para exibição
            m1 = maior // 1000
            m2 = (maior // 100) % 10
            m3 = (maior // 10) % 10
            m4 = maior % 10

            n1 = menor // 1000
            n2 = (menor // 100) % 10
            n3 = (menor // 10) % 10
            n4 = menor % 10

            r1 = resultado // 1000
            r2 = (resultado // 100) % 10
            r3 = (resultado // 10) % 10
            r4 = resultado % 10

            print("Passo", passos, ":", m1, m2, m3, m4, "-", n1, n2, n3, n4, "=", r1, r2, r3, r4)

            numero = resultado

            # -------- REVALIDAÇÃO --------
            if numero != 6174:

                if numero < 0 or numero > 9999:
                    print("Erro: valor fora do intervalo.")
                    break

                milhar = numero // 1000
                centena = (numero // 100) % 10
                dezena = (numero // 10) % 10
                unidade = numero % 10

                if (milhar == centena == dezena) or \
                   (milhar == centena == unidade) or \
                   (milhar == dezena == unidade) or \
                   (centena == dezena == unidade):

                    print("Erro: repetição excessiva de dígitos.")
                    break

        print("")

        if numero == 6174:
            print("Constante 6174 alcançada em", passos, "passos.")