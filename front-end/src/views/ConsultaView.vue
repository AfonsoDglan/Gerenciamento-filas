<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const atendente = ref(localStorage.getItem('nome'))
if (atendente.value) {
  atendente.value = atendente.value.replace(/['"]+/g, '')
}
const nomePaciente = ref('')
const diagnostico = ref('')

const mock = ref({ 	atendente:'112tf3y1t3',
				nomePaciente:'112tf3y1t3' ,
				estado:'112tf3y1t3',
				senha:'112tf3y1t3' ,
				sexo:'112tf3y1t3' ,
				queixaPrincipal:'112tf3y1t3' ,
				historicoBreve :'112tf3y1t3' ,
				observacaoObjetiva :'112tf3y1t3' ,
				dor:'112tf3y1t3' ,
				frequenciaCardiaca :'112tf3y1t3' ,
				frequenciaRespiratoria :'112tf3y1t3' ,
				pressaoArterial :'112tf3y1t3' ,
				temperatura :'112tf3y1t3' ,
				fraturasExpostas :'112tf3y1t3' ,
				quimadurasGraves :'112tf3y1t3' ,
				classificação :'112tf3y1t3' ,
				})



const data = [
				nomePaciente,   
				diagnostico]

// const url = ('http://127.0.0.1:8000/proximopaciente')
// axios.get(url).
// then( (response) => {
//   console.log('ProximoPaciente',response.data)
      
// })
// .catch( (erro) => {
//   console.log('Erro', erro)
// })

const confirmar = () => {

  if (FormularioPreenchido()){
	const url = 'http://127.0.0.1:8000/triagem/'
	console.log()
   	axios.post(url,{
                   nomePaciente: nomePaciente.value,
                   diagnostico: diagnostico.value,
                   })
  } else {
	invalido.value = true
	console.log('invalido')
  }
}

function FormularioPreenchido() {
	let valid = true
	Object.values(data).forEach( (item) => {
		if (item.value === '') {
			valid = false
	}
	})
	return valid
}
const invalido = ref(false)
function sumir(){
  invalido.value = false
}
</script>

<template>
    <body>
        <div class="invalido" @click="sumir" v-if="invalido"> Preencha todos os campos.
		<p class="closetag">clique para fechar</p></div>

        <div class="box">

          <div class="content">

            <h1>Consulta</h1>

            <div class="perfilPaciente">
				<h2>Resultados da Triagem</h2>
				<div :class="['item',i % 2 == 0 ? 'alternando' : '']" v-for="(value,key,i) in mock">
					<div class="titleitem"  >{{ key.charAt(0).toUpperCase() + key.slice(1) }}:</div>  {{  value }}
				</div>



            </div>

            <div class='form'>



                <div class="inputBox"> 
                    <label for="diagnostico">Diagnostico</label> 
                    <textarea v-model="diagnostico" id="diagnostico" type="text" required></textarea>
                </div>  
                

                <div class="inputBox"> 
                    <input @click="confirmar()" type="submit" value="Confirmar"> 
                </div> 

            </div>

          </div>

        </div>

    </body>
    
</template>

<style scoped>
body 
{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: var(--background);
  font-family: 'Quicksand', sans-serif;
}

.box  
{
  position: relative;
  margin: 10px 0;
  width: 70vw;
  background: var(--secondarycolor);  

  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0,0,0,9);
}
.content 
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 10px;
}
h1
{
  font-size: 2em;
  color: var(--primarycolor);
  font-weight: bold;
  text-transform: uppercase;
}
.form 
{
  
  display: flex;
  flex-wrap: wrap;
  width: 100%;
}
.box  .form .inputBox
{
  position: relative;
  width: 100%;
  color: black;
  font-weight: bold;
}
.box .form .inputBox label
{
  color: var(--fontcolortext);
  font-weight:bold;
}
.box .form .freqs
{
  display: flex;
  position: relative;
  justify-content: space-between;
  width: 100%;
  flex-direction: row;
 
  
}

.box .form .freq
{
  position: relative;
  width: 30%;
}


.box  .form .inputBox input 
{
  position: relative;
  width: 100%;
  background:var(--background);
  border: 2px solid transparent;
  outline: none;
  padding:  12px;
  border-radius: 4px;
  color: black;
  font-weight: 500;
  font-size: 1em;
}
.box  .form .inputBox select 
{
  position: relative;
  min-width: 100%;
  background: var(--background);
  border: 2px solid transparent;
  outline: none;
  padding: 12px;
  border-radius: 4px;
  color: var(--fontcolortext);
  font-weight: 500;
  font-size: 1em;
}

.box  .form .inputBox textarea 
{
  position: relative;
  width: 100%;
  background:var(--background);
  border: 2px solid transparent;
  outline: none;
  padding:  12px;
  border-radius: 4px;
  color: black;
  font-weight: 500;
  font-size: 1em;
}

.box .content .form .inputBox input:focus,select:focus{
    border: 2px solid var(--primarycolor) ;
}
.box .content .form .inputBox select:focus{
    border: 2px solid var(--primarycolor) ;
}
.box .content .form .inputBox textarea:focus{
    border: 2px solid var(--primarycolor) ;
    height: 100px;
}



.box .form .inputBox input[type="submit"]
{
  padding: 10px;
  background: var(--primarycolor);
  color: #000;
  font-weight: 600;
  font-size: 1.35em;
  letter-spacing: 0.05em;
  cursor: pointer;
}

.box .form .inputBox input[type="range"]
{
  padding: 0;
}



datalist {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  font-weight: bold;
  padding:0 2px;
 
}

.invalido{ 
  position:fixed;
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 35%;
  height: 30%;
  top: 40%;
  padding-top: 22px;
  gap: 5px;


  background-color: var(--secondarycolor);

  border: 10px solid rgb(231, 105, 105);;
  border-radius: 8px;


  font-weight: bold;
  font-size: 20px;
  color: black;
}
.invalido .closetag{
	font-size: 15px;
	color: gray;
}

.perfilPaciente{
	width: 100%;
	display: flex;

	flex-wrap: wrap;

	border-bottom: 2px solid black;


	color: var(--fontcolortext);

}

.perfilPaciente h2{
	width: 100%;
	border-bottom: 2px solid black;
}

.item{
	width: 100%;
	display: flex;
	flex-wrap: nowrap;
	align-items: center;
	justify-content: space-between;
	height: 1.8em;
	background-color: white;
	
}
.alternando{
	background-color: #a1d4c0;
}

.titleitem{
	font-weight: bold;
}



</style>