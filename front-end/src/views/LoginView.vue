<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';
import axios from 'axios'

const username = ref('')
const password = ref('')
const incorreto = ref(false)

const  autenticar = () => {

  const API_URL = 'http://127.0.0.1:8000/login'
    axios.post(API_URL,{'usename':username.value,'password':password.value})
    .then( (response) => {
      console.log('response',response.data)
      if(response.status == 200){
        localStorage.setItem('token',response.data['token'])
        localStorage.setItem('tipo',response.data['tipo'])
        router.push({name:'fila'})
      }
    }).catch( (erro) => {
      if (erro.status === 401 ) {
      incorreto.value = true
      } else {
        console.log(erro)
      }
    })
}

</script>

<template>

<body> <!-- partial:index.partial.html --> 

<section> 

 <div class="signin"> 

  <div class="content"> 

   <h2>Login</h2> 

   <div class="error"> 

    <div v-if="incorreto">Usuario ou Senha incorreto</div>

  </div> 

   <div class="form"> signup

    <div class="inputBox"> 

      <label for="username">Usuario</label>
     <input v-model="username" id="username" type="text" required>  

    </div> 

    <div class="inputBox"> 

      <label for="senha">Senha</label> 
     <input v-model="password" id="senha" type="password" required> 

    </div> 

    <div class="links"> <a @click="router.push({name:'signup'})">Signup</a> 

    </div>

    <div class="inputBox"> 

     <input @click="autenticar" type="submit" value="Login"> 

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
section 
{
  position: absolute;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2px;
  flex-wrap: wrap;
  overflow: hidden;
}

section span 
{
  position: relative;
  display: block;
  width: calc(6.25vw - 2px);
  height: calc(6.25vw - 2px);
  background: var(--secondarycolor);

  transition: 1.5s;
}
section span:hover 
{
  background: var(--primarycolor);
  transition: 0s;
}

section .signin
{
  position: absolute;
  width: 400px;
  background: var(--secondarycolor);  

  display: flex;
  justify-content: center;

  padding: 40px;
  border-radius: 4px;
  box-shadow: 0 15px 35px rgba(0,0,0,9);
}
section .signin .content 
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 10px;
}
section .signin .content h2 
{
  font-size: 2em;
  color: var(--primarycolor);
  text-transform: uppercase;
} 

section .signin .content .error
{
  background-color: rgb(231, 105, 105);
  text-transform: uppercase;
  color: black  ;
  font-weight: bold;
  padding: 0 8px;
  border-radius: 3px;
}


section .signin .content .form 
{
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 25px;
}
section .signin .content .form .inputBox
{
  position: relative;
  width: 100%;
}

section .signin .content .form .inputBox label
{
  color: var(--fontcolortext);
  font-weight:bold;
}
section .signin .content .form .inputBox input 
{
  position: relative;
  width: 100%;
  background: var(--background);
  border: none;
  outline: none;
  padding: 10px 7.5px;
  border-radius: 4px;
  color: var(--fontcolortext);
  font-weight: 500;
  font-size: 1em;
}
section .signin .content .form .inputBox i 
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
.signin .content .form .links 
{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.signin .content .form .links a 
{
  color: var(--primarycolor);
  text-decoration: none;
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
</style>
