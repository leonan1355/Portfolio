document.addEventListener('DOMContentLoaded', () => {
    const botoes = document.querySelectorAll('#botoes button');
    let jogadorAtual = 'X';
    let vencedor = false;
    const tela = document.getElementById('tela');
    botoes.forEach((botao, index) => {
        if (index !== 0) {
            botao.addEventListener('click', () => {
                if (!vencedor && botao.textContent === '') {
                    botao.textContent = jogadorAtual;
                    botao.classList.add(jogadorAtual);
                    if (verificarVitoria(jogadorAtual)) {
                        tela.value = `${jogadorAtual} venceu!`;
                        vencedor = true;
                    } else if (verificarEmpate()) {
                        tela.value = 'Velha!';
                        vencedor = true
                    } else {
                        jogadorAtual = jogadorAtual === 'X' ? 'O' : 'X';
                        tela.value = `É a vez do jogador "${jogadorAtual}"`
                    }
                }
            });
        }
    });
    function verificarVitoria(jogador) {
        const padroesVitoria = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ];
        return padroesVitoria.some(padrao => {
            return padrao.every(indice => {
                return botoes[indice].textContent === jogador;
            });
        });
    }
    function verificarEmpate() {
        return [...botoes].every((botao, index) => {
            return index === 0 || botao.textContent !== '';
        });
    }

    function reiniciarJogo() {
        botoes.forEach((botao, index) => {
            if (index !==0) {
                botao.textContent = '';
                botao.classList.remove('X', 'O');
            }
        });
        jogadorAtual = jogadorAtual === 'X' ? 'O' : 'X';
        vencedor = false;
        tela.value = `O jogador "${jogadorAtual}" começa!`
    }
    document.querySelector('.J').addEventListener('click', reiniciarJogo);
});