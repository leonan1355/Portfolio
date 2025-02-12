reiniciarJogo();

function exibirTexto(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function verificarChute() {
    let chute = document.querySelector('input').value;
    if (chute==numeroSecreto) {
        exibirTexto('.jogo_numero_secreto h1', 'Você acertou!');
        let singularPlural = tentativas > 1 ? 'tentativas' : 'tentativa';
        let mensagem = `Você descobriu o número secreto com ${tentativas} ${singularPlural}!`;
        exibirTexto('.jogo_numero_secreto p', mensagem);
        document.querySelector('.imagem_numero_secreto').src = imagemVitoria;
    } else {
        if (chute > numeroSecreto) {
            exibirTexto('.jogo_numero_secreto p', 'O número é menor!');
        } else {
            exibirTexto('.jogo_numero_secreto p', 'O número é maior!');
        }
        tentativas++;
        limparCampo();
    }
}

function gerarNumero() {
    return parseInt(Math.random() * 10 + 1);
}

function limparCampo() {
    usuarioInput = document.querySelector('.jogo_numero_secreto input');
    usuarioInput.value = ''
}

function reiniciarJogo() {
    numeroSecreto = gerarNumero();
    limparCampo();
    tentativas = 1;
    exibirTexto('.jogo_numero_secreto h1', 'Bem-vindo ao Jogo do Número Secreto!');
    exibirTexto('.jogo_numero_secreto p', 'Escolha um número entre 1 e 10:');
    document.querySelector('.imagem_numero_secreto').src = imagemJogo;
}