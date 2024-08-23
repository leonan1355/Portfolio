const painelJogo = document.querySelector(".painelJogo");
const contexto = painelJogo.getContext("2d");
const pontuacaoTexto = document.querySelector(".pontuacaoTexto");
const botaoJogarDenovo = document.querySelector(".botaoJogarDenovo");
const larguraJogo = painelJogo.width;
const alturaJogo = painelJogo.height;
const corPlano = "black";
const corCobra = "navy";
const corCabeca = "blue";
const bordaCobra = "yellow";
const corComida = "red";
const tamanhoUnidade = 25;
let funcionando = false;
let mudouDirecao = false;
let velocidadeX = tamanhoUnidade;
let velocidadeY = 0;
let comidaX;
let comidaY;
let pontuacao = 0;
let cobra = [
    {x:tamanhoUnidade * 4,y:0},
    {x:tamanhoUnidade * 3,y:0},
    {x:tamanhoUnidade * 2,y:0},
    {x:tamanhoUnidade,y:0},
    {x:0,y:0}
];

window.addEventListener("keydown", mudarDirecao);
botaoJogarDenovo.addEventListener("click", jogarDenovo);

comecarJogo();

function criarComida() {
    function comidaAleatoria(min, max) {
        const randNum = Math.round((Math.random() * (max-min)+min) / tamanhoUnidade) * tamanhoUnidade;
        return randNum;
    }
    comidaX = comidaAleatoria(0, larguraJogo - tamanhoUnidade);
    comidaY = comidaAleatoria(0, alturaJogo - tamanhoUnidade);

    cobra.forEach(parteCobra => {
        if (parteCobra.x == comidaX && parteCobra.y == comidaY) {
            criarComida();
        }
    });
};

function desenharComida() {
    contexto.fillStyle = corComida;
    contexto.fillRect(comidaX, comidaY, tamanhoUnidade, tamanhoUnidade);
};

function limparTela() {
    contexto.fillStyle = corPlano;
    contexto.fillRect(0, 0, larguraJogo, alturaJogo);
};

function desenharCobra() {
    
    cobra.forEach((corpoCobra, index) => {
        if (index == 0) {
            contexto.fillStyle = corCabeca;
        } else {
            contexto.fillStyle = corCobra;
        }
        contexto.strokeStyle = bordaCobra;
        contexto.fillRect(corpoCobra.x, corpoCobra.y, tamanhoUnidade, tamanhoUnidade);
        contexto.strokeRect(corpoCobra.x, corpoCobra.y, tamanhoUnidade, tamanhoUnidade);
    });
};

function andarCobra() {
    const ponta = {x: cobra[0].x + velocidadeX, y: cobra[0].y + velocidadeY};
    cobra.unshift(ponta);
    if(cobra[0].x == comidaX && cobra[0].y == comidaY) {
        pontuacao += 1;
        pontuacaoTexto.textContent = pontuacao;
        criarComida();
    } else {
        cobra.pop();
    }
};

function mudarDirecao(event) {
    if (mudouDirecao) return;

    const botaoPressionado = event.keyCode;
    const esquerda = 37;
    const cima = 38;
    const direita = 39;
    const baixo = 40;

    const paraEsquerda = (velocidadeX == -tamanhoUnidade);
    const paraCima = (velocidadeY == -tamanhoUnidade);
    const paraDireita = (velocidadeX == tamanhoUnidade);
    const paraBaixo = (velocidadeY == tamanhoUnidade);

    switch(true){
        case(botaoPressionado == esquerda && !paraDireita):
            velocidadeX = -tamanhoUnidade;
            velocidadeY = 0;
            mudouDirecao = true;
            break;
        case(botaoPressionado == cima && !paraBaixo):
            velocidadeX = 0;
            velocidadeY = -tamanhoUnidade;
            mudouDirecao = true;
            break;
        case(botaoPressionado == direita && !paraEsquerda):
            velocidadeX = tamanhoUnidade;
            velocidadeY = 0;
            mudouDirecao = true;
            break;
        case(botaoPressionado == baixo && !paraCima):
            velocidadeX = 0;
            velocidadeY = tamanhoUnidade;
            mudouDirecao = true;
            break;
    }
};

function verificarFim(){
    switch(true){
        case (cobra[0].x < 0):
            funcionando = false;
            break;
        case (cobra[0].x >= larguraJogo):
            funcionando = false;
            break;
        case (cobra[0].y < 0):
            funcionando = false;
            break;
        case (cobra[0].y >= alturaJogo):
            funcionando = false;
            break;
    }
    for(let i = 1; i < cobra.length; i+=1){
        if(cobra[i].x == cobra[0].x && cobra[i].y == cobra[0].y){
            funcionando = false;
        }
    }
};

function mostrarFim() {
    contexto.font = "50px Arial";
    contexto.fillStyle = "white";
    contexto.textAlign = "center";
    contexto.fillText("FIM DE JOGO", larguraJogo/2, alturaJogo/2);
    funcionando = false;
};

function proximoQuadrado() {
    if(funcionando){
        setTimeout(()=>{
            limparTela();
            desenharComida();
            andarCobra();
            desenharCobra();
            mudouDirecao = false;
            verificarFim();
            proximoQuadrado();
        }, 100);
    } else {
        mostrarFim();
    }
};

function comecarJogo() {
    funcionando = true;
    pontuacaoTexto.textContent = pontuacao;
    criarComida();
    desenharComida();
    proximoQuadrado();
};

function jogarDenovo(){
    pontuacao = 0;
    velocidadeX = tamanhoUnidade;
    velocidadeY = 0;
    cobra = [
        {x:tamanhoUnidade * 4,y:0},
        {x:tamanhoUnidade * 3,y:0},
        {x:tamanhoUnidade * 2,y:0},
        {x:tamanhoUnidade,y:0},
        {x:0,y:0}
    ];
    comecarJogo();
};