<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';
import axios from 'axios';

const tipo = ref('n')

function senha(tipo:string){
    const url = 'http://127.0.0.1:8000/senha/?tipo=' + tipo
    console.log(url)
    axios.get(url)
    .then( ( response ) => {
        if (response.status === 201) {
            localStorage.setItem('senha',response.data['senha'])
            //localStorage.setItem('senha','c1')
            router.push({name: 'senha'})
        }
    })
    .catch( (erro) => {
        console.log(erro) 
        //localStorage.setItem('senha','c1')
        }
    )
}
</script>

<template>
<body> 
  <div class="page">
      	<div class="box">
        	<div class="welcome">
        	 	<h2>Bem-vindo ao App </h2>
         		<h2>Onde Sua Saúde é a Nossa Prioridade! </h2>
            </div>
            
            <div class="instruções">
                <h2>Para ser atendido, pressione uma das opções abaixo </h2>
                <div class="butoes"> 
                    <button class="btn normal" @click="senha('n')">Senha Convêncional</button>
                    <button class="btn prefe" @click="senha('p')">Senha Preferêncial</button>
                </div>
                <div class="info">
                    <h2>Atenção!</h2>
                    <img alt="Vue logo" class="logo" src="@\assets\preferencial.webp"/>

                </div>
            </div>

            
        
      </div>
  </div>

</body>

</template>

<style scoped>
body{
  display: flex;
  justify-content: center;

    background-color: var(--background);


    height: auto !important;
    font-weight: normal;
    font-size: 16px;
    line-height: 25px;
    letter-spacing: 0;
    color: #333333;
}

.page{
  position: relative;

  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  height: 100%;
  width: 80vw;
  margin-top: 10px;



  background-color: var(--secondarycolor);
  border-radius: 4px;
}

.box{
  position: relative;
  width: 100%;
  height: 60%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap:2px;

  margin: 1% 1%;
  border-radius: 4px;

}

.welcome{
	display: flex;
  	justify-content: center;
  	align-items: center;
  	flex-direction: column;
	width: 100%;
	height: 100px;
	

	border-radius: 4px;
	background-color: var(--primarycolor);

	color: var(--secondarycolor);
}

.instruções{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    border: 5px solid var(--primarycolor);
    border-radius: 4px;

    width: 100%;
    
}



.butoes{
    display: flex;
    justify-content: space-around;
    width: 100%;
    margin: 10px 0;

}

.btn{
    width: 30%;
    height: 3em;
    border-radius: 4px;
    font-size: 20px;
    min-width: 150px;
}


.normal{
    background-color: #0853bd;
    color: var(--secondarycolor);
    
}

.normal:hover{
    background-color: #0d71ff;
}

.prefe{
    background-color: #6b1114 ;
    color: var(--secondarycolor);
}
.prefe:hover{
    background-color: #fc262d;
}

.info{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    width: 600px;
    border: 4px solid var(--fontcolortext);
    border-radius: 4px;
    
}

.info h2{
    display: flex;
    justify-content: center;

    background-color: var(--background);
    width: 600px;
}
</style>
