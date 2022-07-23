const readline = require('readline-sync');
const Forca = require('./forca');

const palavras =['abacaxi', 'computador', 'dbserver', 'inclusao', 'divercidade']
let index = Math.floor(Math.random() * palavras.length)

const jogo = new Forca(index);

while (!["perdeu", "ganhou"].includes(jogo.buscarEstado())) {
    const chute = readline.question("Aguardando chute: \n");
    jogo.chutar(chute);
    console.log(jogo.buscarDadosDoJogo());
}

console.log("você " + jogo.buscarEstado());
