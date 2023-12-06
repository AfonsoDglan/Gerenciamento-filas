<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';
import axios from 'axios'

const username = ref('teste')
const password = ref('teste')
const incorreto = ref(false)

const  autenticar = () => {
  
  // Autentificação
  const API_URL = 'URL da API'
  const url = API_URL + 'user=' + username.value + '&senha=' +password.value
  //axios.post(url)
  //  .then(( ))
  //}
  //criptografar senha - checar qual

  const resp: any = {"token": "1234",
                "nome" : username.value + ' sobrenome',
                'tipo' : 1}

  const resp2: any = {"token": "1234",
                "nome" : username.value + ' sobrenome',
                'tipo' : 2}            
  

  if (username.value === 'teste' && password.value === 'teste') {
    console.log('Autenticado!')
    for (const key in resp) {
      if (resp.hasOwnProperty(key)) {
        localStorage.setItem(key, JSON.stringify(resp[key]));
      }
    }
    router.push({name:'fila'}) 

    
   
  }
  else if (username.value === 'teste1' && password.value === 'teste'){
    console.log('Autenticado!')
    for (const key in resp2) {
      if (resp.hasOwnProperty(key)) {
        localStorage.setItem(key, JSON.stringify(resp2[key]));
      }
    }
    router.push({name:'fila'}) 
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

   <h2>Login</h2> 

   <div class="error"> 

    <div v-if="incorreto">Usuario ou Senha incorreto</div>

  </div> 

   <div class="form"> 

    <div class="inputBox"> 

      <label for="username">Usuario</label>
     <input v-model="username" id="username" type="text" required>  

    </div> 

    <div class="inputBox"> 

      <label for="senha">Senha</label> 
     <input v-model="password" id="senha" type="password" required> 

    </div> 

    <div class="links"> <a style="color: black;" href="#">Esqueceu a senha?</a> <a @click="router.push({name:'signup'})">Signup</a> 

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
