<script setup lang="ts">
import {ref} from 'vue'

const senha = ref(localStorage.getItem('senha'))

</script>

<template>
    <body>
        <div class="page">
            <div class="box">
                <div class="senha">
                    <h2>Sua Senha é</h2>
                    <h1>{{ senha }}</h1>
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

.senha{
  display: flex;
 
  justify-content: space-evenly;
  flex-direction: column;
  align-items: center;

  background-color: var(--primarycolor);
  color: var(--secondarycolor);
  border-radius: 4px;
  border: 5px solid var(--fontcolortext);

  width: 100%;
  height:10em;

  font-size: 20px;
}
</style>