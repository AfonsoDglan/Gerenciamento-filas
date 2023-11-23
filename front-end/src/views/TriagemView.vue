<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'



const api = 'url da api'

const atendente = ref(localStorage.getItem('nome'))
const nomePaciente = ref('')
const estado = ref('')
const senha = ref('')
const sexo = ref('')
const queixa = ref('')
const historico = ref('')
const observacoes = ref('')
const dor = ref(5)
const freqcard = ref('')
const freqresp = ref('')
const freqarte = ref('') 
const temperatura = ref('')
const fratura = ref('')
const queimadura = ref('')
const classe = ref('')




const confirmar = () => {
    console.log()
    axios.post(api,{atendente: atendente,
                    nomePaciente: nomePaciente,
                    estado: estado,
                    senha: senha,
                    sexo: sexo,
                    queixaPrincipal: queixa,
                    historicoBreve : historico,
                    observacaoObjetiva : observacoes,
                    dor: dor,
                    frequenciaCardiaca : freqcard ,
                    frequenciaRespiratoria : freqresp,
                    pressaoArterial : freqarte,
                    temperatura : temperatura,
                    fraturasExpostas : fratura,
                    quimadurasGraves : queimadura, 
                    classificacao : classe,
                    })
}
</script>

<template>
    <body>
   
        <div class="box">
            <h1>Triagem</h1>
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

                    <label for="sexo">Sexo</label>
                    <select  v-model="sexo" id="sexo">
                    <option  disabled value="">Selecione</option>
                    <option>Masculino</option>
                    <option>Feminino</option>
                    <option>Outro</option>
                    </select>

                </div> 

                <div class="inputBox"> 
                    <label for="queixa">Queixa</label> 
                    <input v-model="queixa" id="queixa" type="text" required> 
                </div>  

                <div class="inputBox"> 
                    <label for="historico">Historico</label> 
                    <input v-model="historico" id="historico" type="text" required> 
                </div> 

                <div class="inputBox"> 
                    <label for="observacoes">Observações</label> 
                    <input v-model="observacoes" id="observacoes" type="text" required> 
                </div> 

                <div class="inputBox"> 
                    <label for="dor">Nivel de dor : {{  dor }}</label> 
                    <input v-model="dor" id="dor" type="range" min="0" max="10" class="slider">
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
                      <label for="freqarte">Pressão Arterial</label> 
                      <input v-model="freqarte" id="freqarte" type="text" required> 
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

                    <label for="classe">Classificação</label><br>
                    <select  v-model="classe" id="classe">
                    <option  disabled value="">Selecione</option>
                    <option>Emergência</option>
                    <option>Muito Urgente</option>
                    <option>Urgente</option>
                    <option>Pouco Urgente</option>
                    <option>Não Urgente</option>
                    </select>

                </div> 
                

                <div class="inputBox"> 
                    <input @click="confirmar()" type="submit" value="Confirmar"> 
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
  background: var(--secondarycolor);
}

h1{
  color: var(--primarycolor)
}

.box
{
  position: relative;
  flex-direction: column;
  gap: 10px;
  width: 50vw;
  background: #222;  
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0,0,0,9);
}

.box  
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 40px;
}
.box  h2 
{
  font-size: 2em;
  color: var(--primarycolor);
  text-transform: uppercase;
}
.box  .form 
{
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 25px;
}
.box  .form .inputBox
{
  position: relative;
  width: 100%;
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
  background: #333;
  border: 0;
  outline: none;
  padding:  12px;
  border-radius: 4px;
  color: #fff;
  font-weight: 500;
  font-size: 1em;
}
.box  .form .inputBox select 
{
  position: relative;
  min-width: 100%;
  background: #333;
  border: none;
  outline: none;
  padding: 12px;
  border-radius: 4px;
  color: #fff;
  font-weight: 500;
  font-size: 1em;
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
input[type="submit"]:active
{
  opacity: 0.6;
}
@media (max-width: 900px)
{
  section span 
  {
    width: calc(10vw - 2px);
    height: calc(10vw - 2px);
  }
}
@media (max-width: 600px)
{
  section span 
  {
    width: calc(20vw - 2px);
    height: calc(20vw - 2px);
  }
}

.box .form .inputBox input[type="submit"]:hover{
  background-color: var(--hoverprimarycolor);
  color: var(--secondarycolor)
}



</style>