<script setup lang="ts">
import { ref } from 'vue'

const username = ref('')
const tipo =  ref('')

const c = () => {
    console.log('clicou no botao')
}
</script>

<template>
    <body>
    <h1>Adicionar Fila</h1>
        <div class='form'>
            <div class="inputBox"> 
                <label for="nome">Nome Completo</label>
                <input v-model="username" id="nome" type="text" required> 
            </div> 

            <div class="inputBox"> 
                <label for="nome">Nome Completo</label> 
                <input v-model="username" id="nome" type="text" required> 
            </div> 

            <div class="inputBox"> 
                <label for="nome">Nome Completo</label> 
                <input v-model="username" id="nome" type="text" required> 
            </div> 

            <div class="inputBox"> 

                <label for="tipo">Tipo</label> 
                <select  v-model="tipo" id="tipo">
                <option  disabled value="">Selecione</option>
                <option>Convencional</option>
                <option>Preferencial</option>
                </select>

            </div>  

            <div class="inputBox"> 
                <input @click="c()" type="submit" value="Login"> 
            </div> 

        </div>
    </body>
</template>