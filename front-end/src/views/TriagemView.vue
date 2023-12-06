<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const nomePaciente = ref('')
const estado = ref('')
const senha = ref('')
const sexo = ref('')
const queixa = ref('')
const historico = ref('')
const observacoes = ref('')
const dor = ref(0)
const freqcard = ref('')
const freqresp = ref('')
const freqarte = ref('') 
const temperatura = ref('')
const fratura = ref('')
const queimadura = ref('')
const classe = ref('')

const data = [	nomePaciente,
				senha,
				senha,
				sexo,
				queixa,
				historico,
				observacoes,
				dor,
				freqcard,
				freqresp,
				freqarte, 
				temperatura,
				fratura,
				queimadura,
				classe ]

axios.get('http://127.0.0.1:8000/proxima')
.then( (response) => {
	console.log('proxima',response.data)
})
.catch( (erro) => {
	console.log('erro de proxima',erro)
})

const confirmar = () => {

  if (FormularioPreenchido()){
	const url = 'http://127.0.0.1:8000/triagem'
	console.log()
   	axios.post(url,{nomePaciente: nomePaciente.value,
                   senha: senha.value,
                   sexo: sexo.value,
                   queixaPrincipal: queixa.value,
                   historicoBreve : historico.value,
                   observacaoObjetiva : observacoes.value,
                   dor: dor.value,
                   frequenciaCardiaca : freqcard .value,
                   frequenciaRespiratoria : freqresp.value,
                   pressaoArterial : freqarte.value,
                   temperatura : temperatura.value,
                   fraturasExpostas : fratura.value,
                   quimadurasGraves : queimadura.value,
                   classificacao : classe.value,
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
// Utilidades
// todos os campos preenchidos
const invalido = ref(false)
function sumir(){
  invalido.value = false
}

// spinner
const esperar = ref(true)

</script>

<template>
    <body>
        <div class="invalido" @click="sumir" v-if="invalido"> Preencha todos os campos.
		<p class="closetag">clique para fechar</p></div>

        <div class="box">

          <div class="content">

            <h1>Triagem</h1>

            <div class='form'>

                <div class="inputBox"> 
                    <label for="paciente">Nome do Paciente</label> 
                    <input v-model="nomePaciente" id="paciente" type="text" required> 
                </div> 

                <div class="inputBox"> 

                    <label for="sexo">Sexo</label>
                    <select  v-model="sexo" id="sexo">
                    <option  disabled value="">Selecione</option>
                    <option>Masculino</option>
                    <option>Feminino</option>
                    </select>

                </div> 

                <div class="inputBox"> 
                    <label for="queixa">Queixa</label> 
                    <textarea v-model="queixa" id="queixa" type="text" required></textarea>
                </div>  

                <div class="inputBox"> 
                    <label for="historico">Historico</label> 
                    <textarea v-model="historico" id="historico" type="text" required placeholder="Nada a declarar"> </textarea>
                </div> 

                <div class="inputBox"> 
                    <label for="observacoes">Observações</label> 
                    <textarea v-model="observacoes" id="observacoes" type="text" required placeholder="Nada a declarar"> </textarea>
                </div> 

                <div class="inputBox"> 
                    <label for="dor">Nivel de dor : {{  dor }}</label> 
                    <input v-model="dor" id="dor" type="range" min="0" max="10" class="slider" list="markers">

                      <datalist id="markers">
                      <option value="0">0</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                      <option value="6">6</option>
                      <option value="7">7</option>
                      <option value="8">8</option>
                      <option value="9">9</option>
                      <option value="10">10</option>
                      </datalist>
                    
                </div> 

                <div class="inputBox freqs"> 

                  <div class="inputBox freq"> 
                      <label for="freqcard">Frequencia Cardiaca</label> 
                      <input v-model="freqcard" id="freqcard" type="text" required> 
                  </div> 

                  <div class="inputBox freq"> 
                      <label for="freqresp">Frequencia Respiratoria</label> 
                      <input v-model="freqresp" id="freqresp" type="text" required> 
                  </div> 

                  <div class="inputBox freq"> 
                      <label for="queimadura">Pressão Arterial</label> 
                      <select  v-model="queimadura" id="queimadura">
                      <option  disabled value="">Selecione</option>
                          <option>Normal</option>
                          <option>Elevada</option>
                          <option>Hipertensão Estágio 1</option>
                          <option>Hipertensão Estágio 2</option>
                          <option>Crise Hipertensiva</option>
                    </select>
                  </div> 

                </div>

                <div class="inputBox freqs"> 

                  <div class="inputBox freq"> 
                      <label for="temperatura">Temperatura</label> 
                      <input v-model="temperatura" id="temperatura" type="text" required> 
                  </div> 

                  <div class="inputBox freq"> 

                      <label for="fratura">Fratura Exposta: </label>
                      <select  v-model="fratura" id="fratura">
                      <option  disabled value="">Selecione</option>
                      <option>Sim</option>
                      <option>Não</option>
                      </select>

                  </div> 

                  <div class="inputBox freq"> 

                    <label for="queimadura">Queimaduras Graves: </label>
                    <select  v-model="queimadura" id="queimadura">
                    <option  disabled value="">Selecione</option>
                    <option>Sim</option>
                    <option>Não</option>
                    </select>

                  </div> 

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

.box .form .inputBox input[type="submit"]:hover{
	background-color: var(--hoverprimarycolor);
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