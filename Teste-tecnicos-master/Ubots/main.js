import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-app.js";
import {setDoc,addDoc,updateDoc, getFirestore, collection, query, deleteDoc, doc,getDoc, onSnapshot} from "https://www.gstatic.com/firebasejs/9.6.3/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCjKCBS-Unpcs3_K1mzjUX3a8Ws3W16nQg",
  authDomain: "avaliador-de-filmes-a3501.firebaseapp.com",
  projectId: "avaliador-de-filmes-a3501",
  storageBucket: "avaliador-de-filmes-a3501.appspot.com",
  messagingSenderId: "859110304403",
  appId: "1:859110304403:web:e5d8d5be4e7ccd3707fb66",
  measurementId: "G-7WNBRP0BQ6"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const movieslist = document.querySelector('[data-js="movies-list"]')
const fromAddMovie = document.querySelector('[data-js="form-add-movie"]');

// cadastra novo item

fromAddMovie.addEventListener('submit', e =>{
  e.preventDefault()
  addDoc(collection(db,'moves'),{
    titulo: e.target.titulo.value,
    sinopse: e.target.sinopse.value,
    lancamento: e.target.lancamento.value, 
    avalia: 0,
  });
});

// Lê os dados do banco de dados

const movesDb = query(collection (db, 'moves'));

onSnapshot(movesDb, snapshot => { 
 const movieslis =  snapshot.docs.reduce((acc, movie)=>{
    const {titulo, sinopse, lancamento}= movie.data();
  acc += ` 
    <li data-id="${movie.id}">
      <h2 class="title" > ${titulo}</h2>  
      
      <ul>
        <li class="movie-description" >Sinopse: ${sinopse}</li>
        <li class="movie-description" >Ano de estreia: ${lancamento}</li>
      </ul>
      <ul class="stars">
        <li class="star-icon ativo star-hidden ${movie.id} " data-test="${movie.id} data-star="0"></li>
        <li class="star-icon ${movie.id}" data-test="${movie.id}" data-star="1"></li>
        <li class="star-icon ${movie.id}" data-test="${movie.id}" data-star="2"></li>
        <li class="star-icon ${movie.id}" data-test="${movie.id}" data-star="3"></li>
        <li class="star-icon ${movie.id}" data-test="${movie.id}" data-star="4"></li>
        <li class="star-icon ${movie.id}" data-test="${movie.id}" data-star="5"></li>
     </ul>
      <div class="continer-btn" >    
        <button data-remove="${movie.id}" class="btn remove">Remover</button>
        <button data-update="${movie.id}" class="btn update">Alterar</button>
      </div>
    </li>`;
  
  return acc
},'')
movieslist.innerHTML = movieslis
})

//avalia o filme
movieslist.addEventListener('click', function(e){
  const avalia = e.target.dataset.test
  const starId = e.target.classList
  const avaliacaoId= doc(db, 'moves', avalia)
    
  const star = document.querySelectorAll('.star-icon')
  

  if(!starId.contains ('ativo')){
    star.forEach(function(e){
      if(starId.contains(avalia)){
        console.log(avalia)
        e.classList.remove('ativo') 
      }  
    })
    starId.add('ativo')
  }
  
  
    setDoc(avaliacaoId),{
      avaliacao : e.target.dataset.star
    }
  console.log(e.target.dataset.star)

});


//exclui um filme
movieslist.addEventListener('click', e =>{
  const removeButton = e.target.dataset.remove
  
  if (removeButton){  
    deleteDoc(doc(db,'moves',removeButton))
  
  }
})

//atualiza um filme

movieslist.addEventListener('click', async e=>{
  const updateButtonId = e.target.dataset.update
  const docAtt =doc(db, 'moves', updateButtonId)
  const docId = await getDoc(docAtt)
  const {titulo, sinopse, lancamento }= docId.data()
  
  const creatInput = async () => { 
    if(updateButtonId){

      movieslist.innerHTML = `
      <form class="cadastro" data-js="update" >
      
      <label class="label" >Titulo</label>
      <input class="input-style att-input" type="text" name="titulo" value="${titulo}">
      
      <label class="label" >Descrição</label>
      <textarea class="input-style att-input" name="sinopse" >${sinopse}</textarea>
      
      <label class="label" > Data de lancamento</label>
      <input class="input-style att-input" type="number" name="lancamento" value="${lancamento}" >
     
      <div class="conteinerAtualiza">
          <input   class="submit atualizar" type="submit" value="Atualizar">
          <button data-js="cancela" class="submit cancelar " >cancelar</button>
          </div>    
          </form>
          `
        }
  }

  await creatInput()
  
  //cancela a atulização

  const update = document.querySelector('[data-js="update"]')
  update.addEventListener(
    'submit', e =>{
      e.preventDefault()
      updateDoc(docAtt,{
        titulo: e.target.titulo.value,
        sinopse: e.target.sinopse.value,
        lancamento: e.target.lancamento.value,
      })
    }
  )
    const cancela = document.querySelector('[data-js="cancela"]')
    cancela.addEventListener("click", () =>{

      location.reload()
    })

})