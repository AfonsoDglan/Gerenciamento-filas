<script setup lang="ts">
import { ref } from 'vue'

const cpf = ref('')
const username = ref('')
const nasc = ref('')
const sexo = ref('')
const tipo = ref('')

const confirmar = () => {
  console.log('Logging in with:',nasc.value);
};





</script>

<template>
<body> 

<section> 

 <div class="box"> 

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

    <div class="inputBox freqs">

        <div class="inputBox freq"> 
        <label for="idade">Data de Nascimento</label> 
        <input v-model="nasc" id="idade" type="date" required>

    </div> 

        <div class="inputBox freq"> 

        <label for="sexo">Sexo</label>
        <select  v-model="sexo" id="sexo">
            <option disabled value="" selected>Selecione</option>
            <option value="1">Masculino</option>
            <option>Feminino</option>
            <option>Outro</option>
        </select>
        
        </div> 

        <div class="inputBox freq"> 

            <label for="sexo">Atendimento</label>
            <select  v-model="tipo" id="sexo" ref="s1">
            <option  disabled value="">Selecione</option>
            <option>Convencional</option>
            <option>Preferencial</option>
            <option>Emergêncial</option>
            </select>

        </div> 

    </div>

    <div class="inputBox cadastrar"> 

     <input @click="confirmar" type="submit" value="Adicionar"> 

    </div> 

   </div> 

  </div> 

 </div> 

</section> <!-- partial --> 

</body>

</template>

<style scoped>
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

.box
{
  position: relative;
  top: 10px;  
  width: 70vw;
  background: var(--secondarycolor);  
  z-index: 1;
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
h2 
{
  font-size: 2em;
  color: var(--primarycolor);
  text-transform: uppercase;
  font-weight: bold;
}
.form 
{
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.freqs
{
  display: flex;
  position: relative;
  justify-content: space-between;
  width: 100%;
  flex-direction: row;
  gap:5% 
}
.box .content .form .inputBox .freq
{
  position: relative;
  width:30%;
  
}

.box .content .form .inputBox
{
  position: relative;
  width: 100%;
}
section .box .content .form .inputBox label
{
  color: var(--fontcolortext);
  font-weight:bold;
}
.box .content .form .inputBox input 
{
  position: relative;
  width: 100%;
  background: var(--background);
  border: 0;
  outline: none;
  padding:  12px;
  border-radius: 4px;
  color:  var(--fontcolortext);
  font-weight: 500;
  font-size: 1em;
}
.box .content .form .inputBox select 
{
  position: relative;
  width: 100%;
  background: var(--background) ;
  border: none;
  outline: none;
  padding: 12px;
  border-radius: 4px;
  color: black;
  font-weight: 500;
  font-size: 1em;

}

.box .content .form .inputBox input:focus{
    border: 2px solid var(--primarycolor) ;
}

.box .content .form .inputBox select:focus{
    border: 2px solid var(--primarycolor) ;
}

.box .content .form .inputBox input[type="submit"]
{
  padding: 10px;
  background: var(--primarycolor);
  color: #000;
  font-weight: 600;
  font-size: 1.35em;
  letter-spacing: 0.05em;
  cursor: pointer;
}

.box .content .form .inputBox input[type="submit"]:hover{
  background-color: var(--hoverprimarycolor)
}

</style>
