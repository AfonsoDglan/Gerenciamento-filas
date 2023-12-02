<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const atendente = ref(localStorage.getItem('nome'))
if (atendente.value) {
  atendente.value = atendente.value.replace(/['"]+/g, '')
}
const nomePaciente = ref('')
const diagnostico = ref('')



const data = [  atendente,
				nomePaciente,   
				diagnostico]

const confirmar = () => {

  if (FormularioPreenchido()){
	const url = 'http://127.0.0.1:8000/triagem/'
	console.log()
   	axios.post(url,{atendente: atendente.value,
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

            <div class='form'>

                <div class="inputBox"> 
                    <label for="atendente">Atendente</label>
                    <input v-model="atendente" id="atendente" type="text" required> 
                </div> 

                <div class="inputBox"> 
                    <label for="paciente">Nome do Paciente</label> 
                    <input v-model="nomePaciente" id="paciente" type="text" required> 
                </div> 

                <div class="inputBox"> 
                    <label for="diagnostico">diagnostico</label> 
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
  gap: 20px;
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
  gap: 20px;
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






</style>