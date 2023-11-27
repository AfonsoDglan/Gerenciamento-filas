<script setup lang="ts">
import { onUpdated, ref } from 'vue'
import router from '@/router';
import axios from 'axios';

const addfilabtn = () => {
  router.push({name: 'addfila'})
}

const triagembtn = () => {
  router.push({name: 'triagem'})
}

const nome = ref(localStorage.getItem('nome'))
if (nome.value) {
  nome.value = nome.value.replace(/['"]+/g, '')
}
const tipo = ref(localStorage.getItem('tipo'))
if (tipo.value) {
  if (tipo.value === '1')
    tipo.value = 'Atendente'
  if (tipo.value === '2')
    tipo.value = 'Triagem'

}


const cpf = ref('12312312312')
const sexo = ref('masculino')
const email = ref('email@.com')


const data = ref([{label:'CPF',value:cpf, refe: cpf},
              {label:'Nome Completo', value:nome, refe: nome},
              {label:'Sexo', value: sexo, refe: sexo},
              {label:'Email', value:email, refe: email},
              {label:'Area de Atuação', value: tipo, refe: tipo},
])

const edit = ref(false)

const editar = () => {
    edit.value = !edit.value
}

const confirmar = () => {
  //axios.post(url editar,{new data})
  edit.value = !edit.value
}



</script>

<template>
<body>
  <div class="page">
    <div class="box">
      <div class="profilecard">

        <img src="@/assets/defaultprofilepic.png" alt="Vue logo" class="profilepic" />
        <div>{{ nome }}</div>
        <div>{{ tipo }}</div>

      </div>

      <div class="datacard">

        <div v-for="item in data" class="dataitem" v-if="!edit">
          <div class="dtl">{{ item.label }}</div>  <div class="dtv">{{ item.value }}</div>
        </div>

        <div v-for="item in data" class="dataitem" v-if="edit"> 
          <label class="dtl" for="{{ item.label }}"> {{ item.label }} </label>
          <input class="dtv" type="text" id=" {{  item.label }}" v-model="item.refe">
        </div>

        <div class="navbtn" @click="editar( )" v-if="!edit"> Atualizar </div>
        <div class="navbtn" @click="confirmar( )" v-if="edit"> Confirmar </div>
        
      </div>

    </div>

    <div class="box">
      <div class="atividades">
        <div class="titulo">Atividades Recentes</div>
      </div>

    </div>

  </div>
</body>

</template>

<style scoped>

body 
{
  font-family: 'Quicksand', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  box-sizing: border-box;
  background: var(--background);
  margin: 0;
  padding: 0;
  border: 0;
  box-sizing: border-box;
}


.page{
  position: relative;
  top: 10px;
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  height: 100%;
  width: 80vw;
  background-color: var(--background);
  border-radius: 4px;
}

.box{
  position: relative;
  display: flex;
 
  width: 100%;
  height: 60%;
  margin: 0 10px 10px 10px;

 
  border-radius: 4px;
}

.profilecard{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width:30%;
  margin-right: 5px;
   
  gap: 5px;

  background-color: var(--secondarycolor);
  border-radius: 4px;
  color: var(--fontcolortext);
}

.profilepic{
  border-radius: 100%;
  min-width: 90px;
  max-width: 50%;
}

.datacard{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width:70%;
  margin-left: 5px;
  border-radius: 4px;

  background-color: var(--secondarycolor);
  color: var(--fontcolortext);
}
.dataitem{
  display: flex;
  border-bottom: 1px solid  gray;
  margin: 0 5px;
  padding: 5px 0 12px;
}
.dtl{
  font-weight: bold;
  width: 9rem;
}
.dtv{
  width: 70%  ;
}

.atividades{
  background-color: var(--secondarycolor);
  color: var(--fontcolortext);
  width: 100%;
  height: 1400px;
  
}

.atividades .titulo{
  font-weight: bold;
}

.navbtn{
  background-color: var(--primarycolor);

  padding: 0.45em;
  text-align: center;
  
  border: 0.5em;
  border-radius: 3px;
  width: 100px;
  max-height: 40px;
  margin: 5px 5px 5px auto;

}
.navbtn:hover{
  background-color: var(--hoverprimarycolor);
}
</style>
