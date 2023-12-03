<script setup lang="ts">
import axios from 'axios';
import { ref } from  'vue'
import type { Ref } from  'vue'



const fila = ref([	{senha: '...', sala: '...'},
					{senha: '...', sala: '...'},	
					{senha: '...', sala: '...'},	
					{senha: '...', sala: '...'},	
					{senha: '...', sala: '...'},	
])
console.log('fila original',fila.value)

const ws = new WebSocket("ws://127.0.0.1:8000/senhasPainel");
ws.onopen = function (e) {
  console.log('Websocket Aberta')
	ws.send(
		JSON.stringify({
			action: "list",
			request_id: new Date().getTime(),
		})
	);
};

ws.onmessage = function (e) {

	let allData = JSON.parse(e.data);

	if (allData.action === "list") {

    let chamadas: Array<{senha:string , sala:string}> = allData.data
    
    if (chamadas.length){

        chamadas.forEach((element,i) => {
        fila.value[i] = element
        i++
      });
      var i = chamadas.length 
      while (i < 5) {
        fila.value[i] = {senha: '...', sala: '...'}
        i++
      }
    }

	} else if (allData.action === "create") {
		fila.value.push(allData.data);
	}
};

const hora: Ref<Date | string> = ref(new Date())
displayCurrentDate()

function displayCurrentDate() {
    const locale = 'pt-BR';
    
    const currentDate = new Date();
    hora.value = currentDate.toLocaleString(locale,{year: 'numeric', month: 'long',day: 'numeric', hour: 'numeric', minute: 'numeric'});
    
    // Call the function every second
    setTimeout(displayCurrentDate, 30000);
    
}

</script>

<template>
<body>
    <div class="page">
        <div class="painel">
            <div class="boxatual"> 
                <div class="titulo">Atual</div>
                <div class="atual">
                    <div>Senha:{{  fila[0].senha }}</div>
                    <div>Sala:{{  fila[0].sala }}</div>
                </div>
                <div class="hora">{{ hora }}</div>
            </div>

            <div class="boxanterior"> 
                <div class="titulo">Ultimas Chamadas</div>
                <div class="anterior">
                    <div class="item" v-for="item in fila.slice(1,)">
                        <div class="itemrow"><div>Senha</div> <div>{{  item.senha }}</div> </div>
                        <div class="itemrow"><div>Sala</div> <div>{{  item.sala }}</div> </div>
                    </div>

                    
                </div>

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
  height: 100%;
  box-sizing: border-box;
  background: var(--background);
  margin: 0;
  padding: 0;
  border: 0;
}


.page{
  position: relative;
  margin-top: 10px;

  display: flex;
  justify-content: space-evenly;

  height: 100%;
  width: 80vw;

  background-color: var(--secondarycolor);
  border-radius: 4px;
}

.painel{
    width: auto-fill;
    display: flex;
    justify-content: space-between;

    width: 100%;

    margin: 5px;
    border-radius: 4px;

    gap: 5px;

}

.boxatual{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    

    height: 100%;
    width: 70%;
}

.boxanterior{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    

    height: 100%;
    width: 30%;
}

.titulo{
    position: relative;
    top:0;
    display: flex;
    justify-content: center;
    width: 100%;
    height: 10%;
    background-color: var(--background);
    color: var(--fontcolortext);
    font-size:2vw;


}
.atual{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    

    height: 100%;
    width: 100%;


    background-color: var(--primarycolor);

    color: var(--secondarycolor);

    font-size: 5vw;
}

.anterior{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;

    height: 100%;
    width: 100%;

    background-color: var(--secondarycolor);
    border-radius: 4px;
}

.anterior .item{
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 25%;
    width: 100%;


    background-color: #287d3c;
    font-size: 2dvw;

    border-width: 1px 2px 1px 2px;
    border-style: solid ;
    border-color: black;
}

.anterior .item .itemrow{
    padding: 0 5px;
    width: 100%;
    display: flex;
    justify-content: space-between;
}


.hora{
    width: 100%;
    background-color: black;
    color: white;
    display: flex;
    justify-content: center;
}



.callbox{
  display: flex;
  justify-content: center;
  align-items: center;

  background-color: var(--secondarycolor);
  width: 50%;
  height: 50%;
  border-radius: 8px;
}

h2{
    color: var(--fontcolortext);
}

.tablecard{
  background-color: var(--secondarycolor);
  color: var(--fontcolortext);
  width: 100%;
  border-radius: 8px;

}

table {
  width: 100%;
  padding: 5px;

}
th {
    font-weight: bold;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color:#dddddd;
}
tr:hover{
   background-color: #99ffd6;
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

</style>
