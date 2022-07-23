class Forca {

  letrasChutadas = []
  vidas = 6
  palavra = []
  palavra_certa = []

  constructor(palavra){
    this.palavra_certa = Array.from(palavra)
    this.palavra = Array(this.palavra_certa.length).fill("_")
  }

  chutar(letra) { 
    if(letra.length === 1){
      if(!this.letrasChutadas.some(lt => lt === letra)){
        this.letrasChutadas.push(letra)
        if(this.palavra_certa.some(lt => lt === letra)){
          this.palavra_certa.map((value, index) => {
            if(value === letra){
              this.palavra[index] = letra
            }
          })
        }else
          this.vidas--
      }
    }

  }

  buscarEstado() { 

    if(this.vidas === 0){
      return "perdeu"
    }else if(this.palavra.toString() === this.palavra_certa.toString()){
      return "ganhou"
    }else
      return "Aguardando chute: \n"
  } // Possiveis valores: "perdeu", "aguardando chute" ou "ganhou"

  buscarDadosDoJogo() {
      return {
          letrasChutadas: this.letrasChutadas, // Deve conter todas as letras chutadas
          vidas: this.vidas, // Quantidade de vidas restantes
          palavra: this.palavra.toString() // Deve ser um array com as letras que já foram acertadas ou o valor "_" para as letras não identificadas
      }
  }
}

module.exports = Forca;
