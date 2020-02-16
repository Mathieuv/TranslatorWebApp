import Vue from 'vue'
import Router from 'vue-router'

const routeroptions = [
  {path: '/', component: 'Translator', name: 'Translator'}
]

const routes = routeroptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
