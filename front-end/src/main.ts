import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Button from 'primevue/button';
import Divider from 'primevue/divider';
import InputText from 'primevue/inputtext';

import '../node_modules/primevue/resources/themes/saga-green/theme.css';
import '../node_modules/primevue/resources/primevue.min.css';  

const app = createApp(App)

app.use(router)


app.use(PrimeVue)

app.component('Button', Button)
app.component('Divider', Divider)
app.component('InputText', InputText)



app.mount('#app')
