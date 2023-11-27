<script setup lang="ts">
import { ref } from  'vue'

const fila = ref([  {nome:'ana',tipo:'convencional'},
                    {nome:'bia',tipo:'prefenrencial'},
                    {nome:'carlo',tipo:'convencional'},
                    {nome:'diego',tipo:'convencional'},
                    {nome:'eric',tipo:'convencional'},
                    {nome:'fabio',tipo:'prefenrencial'},
                    {nome:'gabriel',tipo:'convencional'},
                ])

const edit = ref(false)

</script>

<template>
<body>
    <div class="page">
        <div class="box">
          <div class="callbox">
              {{ fila[0].nome }}
          </div>
          <div class="callbox">
              Primeiro lugar
          </div>
            
        </div>

        <div class="box">
            <div class="tablecard">
                <h2>Fila</h2>
                <table>
                        <tr>
                            <th>Nome</th>
                            <th>Tipo</th>
                        </tr>
                        <tr v-for="item in fila">
                            <td>{{ item.nome }}</td>
                            <td>{{ item.tipo }}</td>
                        </tr>
                </table>
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
  margin: 0 1% 1%;
  gap: 1%;
 
  border-radius: 4px;
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
