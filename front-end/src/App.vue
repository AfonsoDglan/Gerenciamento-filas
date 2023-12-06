<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import router from './router';
import axios from 'axios';


const Logado = ref(false)
const confirma = ref(false)

const tipo = ref('')

const Sair = () => {
  if (window.confirm("Click Ok para sair, ou cancelar para fechar essa mensagem")) {
    localStorage.clear()
    Logado.value = false
    router.push({name:'home'})
}
}

router.beforeEach((to,from) => {
  if (from.name === 'login'&& localStorage.getItem('token')) {
      Logado.value = true 
      const tipoexist = localStorage.getItem('tipo')
      if (tipoexist){
        tipo.value = tipoexist
      }
    }
  }
)

function Chamar(){
	if (tipo.value === '1'){ 
		confirma.value = false
		router.push({name:'triagem'})}
	if (tipo.value === '2'){ 
		confirma.value = false
		router.push({name:'consulta'})}
}

</script>

<template>

  <header>
    <nav>
        <HelloWorld msg="Hospital" />
        <RouterLink class="navbtn" to="/"  v-if="!Logado">Home</RouterLink>
        <a class="navbtn" @click="confirma = true" v-if="Logado && tipo === '1'" >Triagem</a>
        <a class="navbtn" @click="confirma = true" v-if="Logado && tipo === '2'" >Consulta</a>
		<RouterLink class="navbtn" to="/fila">Fila</RouterLink>
       
        
        <RouterLink v-if="!Logado" class="navbtn login" to="/login">Login</RouterLink>

        <a v-if="Logado" class="navbtn login" @click="Sair()">Sair</a>
        
        
    </nav>
 
  </header>

  <RouterView />

  	<div class="confirmação" v-if="confirma"> 
		<div class="confbox">
			<div class="greentop"></div>
			<div class="content">
				<h2>Deseja Chamar o Proximo Paciente</h2>
				<div class="options"><a class="navbtn" @click="Chamar">Confirmar</a> <div class="navbtn cancelar" @click="confirma=false">Cancelar</div></div>
			</div>
		</div>

	</div>

  <a class="navbtn todapag" v-if="Logado && tipo === '1'" @click="confirma = true">+</a>
  <a class="navbtn todapag" v-if="Logado && tipo === '2'" @click="confirma = true">+</a>

  <!--<div class="footer">
	<div class="footcol">Atendimento</div>
	<div class="footcol">Fila</div>
	<div class="footcol">Traigem</div>
	<div class="footcol">Social</div>
	<div class="footcol">Noticias</div>

  </div> -->
  

</template>

<style scoped>

header {
  margin: 0px;
  padding: 0px;
  position: sticky;
  top: 0px;
  left: 0px;
  z-index: 10;

  line-height: 1.5;
  max-height: 100vh;
  background-color:  var(--secondarycolor);

  display: flex;
  box-shadow: 0 1px 4px rgba(0,0,0,9);
}

.navbtn{
  background-color: var(--primarycolor);
  

  padding: 0.45em;
  text-align: center;
  
  border: 0.5em;
  border-radius: 3px;
  width: 110px
}

.navbtn:hover{
  background-color: var(--hoverprimarycolor);
}


nav {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.5em;
  width: 100%;
  font-size: 16px;

  margin: 1rem 1rem;

}

nav a.router-link-exact-active {
  color: /*var(--color-text)*/black;
  background-color: gray;
}

nav a.router-link-exact-active:hover {
  background-color: gray;
}

nav a {
  display: inline;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.login {
  margin-left: auto; 
}

.login a.router-link-exact-active {
  background-color: var(--primarycolor);
  color: /*var(--color-text)*/black;
  border-radius: 5px;
}

.todapag{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0 0 4px;
  margin: 0;

  position: fixed;
  bottom: 5%;
  left:2%;
  z-index: 10;
  

  font-weight: bold;
  font-size: 25px;

  
  width:50px;
  height: 50px;
  border-radius: 100%;
  
}


.footer{
  position: relative;
   left: 0;
   bottom: 0;
   width: 100%;
   height: 5%;
   background-color: var(--secondarycolor);
   color: var(--fontcolortext);
   text-align: center;

   display: flex;
   justify-content: space-evenly;
   
}

.footcol{
	height: 100%;
	background-color: var(--secondarycolor);
	width: auto;
}

.confirmação{
	position: fixed;
	top: 0;
	left:0;
	height: 100%;
	width: 100vw;

	display: flex;
	justify-content: center;
	align-items: center;
	backdrop-filter: blur(10px);
}

.confirmação h2{
	color: black;
	font-size: 1.2vw;
}

.confbox {
	height: 20%;
	width: 25%;

	display: flex;
	flex-direction: column;
	
	border: 2px solid black;

	border-radius: 4px;
	background-color: white;
}

.greentop{

	height: 10%;
	min-height: 15px;
	background-color: var(--primarycolor);
}

.content{ 
	height: auto-fill;
	display: flex;
	flex-direction: column;

	margin: 15px;

	align-items: center;
	gap: 15px;
}

.options{
	display: flex;
	gap: 20px;
}
.cancelar{
	background-color: #a10303;
}
.cancelar:hover{
	background-color: #ed0000;
}





</style>
