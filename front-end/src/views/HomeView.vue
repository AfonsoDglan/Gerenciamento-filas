<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';
</script>

<template>
<body> 
  <div class="page">
      	<div class="box">
        	<div class="welcome">
        	 	 <h2>Bem-vindo ao App </h2>
         		 <h2>Onde Sua Saúde é a Nossa Prioridade! </h2>
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

  margin: 1% 1%;
  border-radius: 4px;
  font-size: 16px;
}

.welcome{
	display: flex;
  	justify-content: center;
  	align-items: center;
  	flex-direction: column;
	width: 100%;
	height: 200px;
	

	border-radius: 4px;
	background-color: var(--primarycolor);

	color: var(--secondarycolor);
}
</style>
