<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import router from './router';


const Logado = ref(false)

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

</script>

<template>

  <header>
    <nav>
        <HelloWorld msg="Hospital" />
        <RouterLink class="navbtn" to="/">Home</RouterLink>
        <RouterLink class="navbtn" to="/fila">Fila</RouterLink>
        <RouterLink class="navbtn" to="/perfil">Perfil</RouterLink>
        <RouterLink class="navbtn" to="/triagem">Triagem</RouterLink>
        <RouterLink class="navbtn" to="/senha">Senha</RouterLink>
       
        
        <RouterLink v-if="!Logado" class="navbtn login" to="/login">Login</RouterLink>

        <a v-if="Logado" class="navbtn login" @click="Sair()">Sair</a>
        
        
    </nav>
 
  </header>

  <RouterView />

  <RouterLink class="navbtn todapag" v-if="Logado && tipo === '1'" to="/addfila">+</RouterLink>
  <RouterLink class="navbtn todapag" v-if="Logado && tipo === '2'" to="/triagem">+</RouterLink>

  <div class="footer">
	<div class="footcol">Atendimento</div>
	<div class="footcol">Fila</div>
	<div class="footcol">Traigem</div>
	<div class="footcol">Social</div>
	<div class="footcol">Noticias</div>

  </div>
  

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



</style>
