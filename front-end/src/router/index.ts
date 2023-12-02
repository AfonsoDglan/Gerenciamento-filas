import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import FilaView from '@/views/FilaView.vue'
import PerfilView from '@/views/PerfilView.vue'
import AdicionarFilaView from '@/views/AdicionarFilaView.vue'
import TriagemView from '@/views/TriagemView.vue'
import SenhaView from '@/views/SenhaView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/senha',
      name: 'senha',
      component: SenhaView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/fila',
      name: 'fila',
      component: FilaView
    },
    {
      path: '/perfil',
      name: 'perfil',
      component: PerfilView,
      meta: {
        requiresAuth: true // Add meta field to indicate protected route
      }
    },
    {
      path: '/addfila',
      name: 'addfila',
      component: AdicionarFilaView,
      meta: {
        requiresAuth: true // Add meta field to indicate protected route
      }
    },
    {
      path: '/triagem',
      name: 'triagem',
      component: TriagemView,
      meta: {
        requiresAuth: true // Add meta field to indicate protected route
      }
    }
  ]
})

router.beforeEach((to, from) => {
  if (to.meta.requiresAuth)  {
    if (localStorage.getItem('token')) {
    }
    else{
      return {name:'login'}
    }  
  }
})

export default router
