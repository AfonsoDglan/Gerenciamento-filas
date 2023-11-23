<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';

const username = ref('teste')
const password = ref('teste')
const incorreto = ref(false)

const  autenticar = () => {
  
  // Autentificação
  const API_URL = 'URL da API'
  const url = API_URL + 'user=' + username.value + '&senha=' +password.value
  //const  autenticar = async () => {
  //   const response =  (await fetch(url)).json()
  //}
  //criptografar senha - checar qual

  

  if (username.value === 'teste' && password.value === 'teste') {
    console.log('Autenticado!')
    localStorage.setItem('token','1234')
    localStorage.setItem('nome','João de Maria da Silva')
    router.push({name:'perfil'}) 
    
   
  } 
  else{
    incorreto.value = true
  }
}




</script>

<template>

<body> <!-- partial:index.partial.html --> 

<section> 

 <div class="signin"> 

  <div class="content"> 

   <h2>Sign In</h2> 

   <div class="error"> 

    <div v-if="incorreto">Usuario ou Senha incorreto</div>

  </div> 

   <div class="form"> 

    <div class="inputBox"> 

     <input v-model="username" type="text" required> <i>Username</i> 

    </div> 

    <div class="inputBox"> 

     <input v-model="password" type="password" required> <i>Password</i> 

    </div> 

    <div class="links"> <a href="#">Forgot Password</a> <a @click="router.push({name:'signup'})">Signup</a> 

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
  background: var(--secondarycolor);
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

@keyframes animate 
{
  0%
  {
    transform: translateY(-100%);
  }
  100%
  {
    transform: translateY(100%);
  }
}
section span 
{
  position: relative;
  display: block;
  width: calc(6.25vw - 2px);
  height: calc(6.25vw - 2px);
  background: var(--secondarycolor);
  z-index: 2;
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
  background: #222;  
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
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
  gap: 30px;
}
section .signin .content h2 
{
  font-size: 2em;
  color: var(--primarycolor);
  text-transform: uppercase;
} 

section .signin .content .error
{
  background-color: #333;
  text-transform: uppercase;
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
section .signin .content .form .inputBox input 
{
  position: relative;
  width: 100%;
  background: #333;
  border: none;
  outline: none;
  padding: 25px 10px 7.5px;
  border-radius: 4px;
  color: #fff;
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
</style>
