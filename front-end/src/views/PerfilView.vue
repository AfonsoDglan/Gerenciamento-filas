<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';

const addfilabtn = () => {
  router.push({name: 'addfila'})
}

const triagembtn = () => {
  router.push({name: 'triagem'})
}

</script>

<template>
<body> 
  <h2>Perfil</h2>
  <a class="navbtn" @click="addfilabtn()">Adicionar a fila</a>

  <h2>Triagem</h2>
  <a class="navbtn" @click="triagembtn()">Triagem</a>
</body>

</template>

<style scoped>
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
</style>
