<script setup lang="ts">
import router from '@/router';
import axios, { type AxiosResponse } from 'axios';
import { ref } from 'vue'

const cpf = ref('')
const username = ref('')
const password = ref('')
const email = ref('')
const sexo = ref('')
const area = ref('')

const invalido = ref(false)
const alma =ref(false)

const confirmar = () => {

    const data = {  cpf: cpf.value,
                    username: username.value,
                    password: password.value,
                    email: email.value,
                    sexo: sexo.value,
                    area: area.value}
    const url = 'http://127.0.0.1:8000/alugma coisa aqui/'
    axios.post(url,data)
    .then( (response:  AxiosResponse) => {
        if (response.status === 201){
            router.push({name:'perfil'})
        }
    })
    .catch( (erro) => {
        console.log(erro)
        invalido.value = true
    })
    
};


function sumir(){
	invalido.value = false
}



</script>

<template>
<body> 

    <div v-if="invalido" class="invalido" @click="sumir()">Preencha Todos os Campos
        <p class="closetag">clique para fechar</p></div>

<section> 

 <div class="signin"> 

  <div class="content"> 

   <h2>Cadastro</h2> 

   <div class="form"> 

    <div class="inputBox"> 

      <label for="cpf">CPF</label> 
      <input v-model="cpf" id='cpf' type="text" required> 

    </div> 

    <div class="inputBox"> 
      <label for="nome">Nome Completo</label> 
      <input v-model="username" id="nome" type="text" required> 

    </div> 

    <div class="inputBox"> 
      <label for="senha">Senha</label> 
     <input v-model="password" id="senha" type="password" required>

    </div> 

    <div class="inputBox"> 
      <label for="email">Email</label> 
     <input v-model="email" id="email" type="email" required>

    </div> 

    <div class="inputBox freqs"> 

        <div class="inputBox"> 

            <label for="atuacao">Area de Atuação</label><br>
            <select  v-model="area" id="atuacao">
            <option  disabled value="">Selecione</option>
            <option>Atendendimento</option>
            <option>Triagem</option>
            <option>Consulta</option>
            </select>

        </div> 

        <div class="inputBox"> 

            <label for="sexo">Sexo</label><br>
            <select  v-model="sexo" id="sexo">
            <option  disabled value="">Selecione</option>
            <option>Masculino</option>
            <option>Feminino</option>
            <option>Outro</option>
            </select>

        </div> 

    </div>
    <div class="termos" >
        <input type="checkbox" id="termos" v-model="alma">
        <label for="termos">Sim, eu aceito com os termos e condições</label>
    </div>



   

  


    <div class="inputBox cadastrar"> 

     <input @click="confirmar" type="submit" value="Cadastrar" :disabled="!alma"> 

    </div> 

   </div> 

  </div> 

 </div> 

</section> <!-- partial --> 

</body>

</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');


*
{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Quicksand', sans-serif;
}
body 
{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: var(--background);
}

.signin
{
  position: relative;
  top: 10px;  
  width: 80vw;
  background: var(--secondarycolor);  

  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0,0,0,9);
}
.signin .content 
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 30px;
}

.freqs
{
  display: flex;
  position: relative;
  justify-content: space-between;
  width: 100%;
  flex-direction: row;
 
  
}

.freq
{
  position: relative;
  width: 40%;
}


.signin .content h2 
{
  font-size: 2em;
  color: var(--primarycolor);
  text-transform: uppercase;
  font-weight: bold;
}
.signin .content .form 
{
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.signin .content .form .inputBox
{
  position: relative;
  width: 100%;

}
section .signin .content .form .inputBox label
{
  color: var(--fontcolortext);
  font-weight:bold;
}
.signin .content .form .inputBox input 
{
  position: relative;
  width: 100%;
  background: var(--background);
  border: 0;
  outline: none;
  padding:  12px;
  border-radius: 4px;
  color: var(--fontcolortext);
  font-weight: 500;
  font-size: 1em;
}
.signin .content .form .inputBox select 
{
  position: relative;
    width: 50%;
  background: var(--background) ;
  border: none;
  outline: none;
  padding: 12px;
  border-radius: 4px;
  color: black;
  font-weight: 500;
  font-size: 1em;
}
.signin .content .form .inputBox i 
{
  position: absolute;
  left: 0;
  padding: 15px 10px;
  font-style: normal;
  color: #aaa;
  transition: 0.5s;
  pointer-events: none;
}
.signin .content .form .inputBox input:focus ~ i,
.signin .content .form .inputBox input:valid ~ i
{
  transform: translateY(-7.5px);
  font-size: 0.8em;
  color: #fff;
}
.signin .content .form .inputBox select:focus ~ i,
.signin .content .form .inputBox select:valid ~ i
{
  transform: translateY(-7.5px);
  font-size: 0.8em;
  color: #fff;
}
.signin .content .form .inputBox input[type="email"]:invalid ~ i
{
  transform: translateY(-7.5px);
  font-size: 0.8em;
  color: #fff;
}
.signin .content .form .inputBox input[type="email"]:focus ~ .inputBox
{
  border: 2px solid red;
}

.signin .content .form .links 
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.signin .content .form .links a 
{
  color: #fff;
  text-decoration: none;
}
.signin .content .form .links a:nth-child(2)
{
  color: var(--primarycolor);
  font-weight: 600;
}
.signin .content .form .inputBox input[type="submit"]
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

.signin .content .form .inputBox input[type="submit"]:hover{
  background-color: var(--hoverprimarycolor)
}

.signin .content .form .inputBox input[type="submit"]:disabled{
  background-color:gray
}

.termos{
    color: var(--fontcolortext);
}

.termos label{
    padding-left: 5px\   ;
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
  padding-top: 20px;
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
