<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <div class="container">
      <a class="navbar-brand fw-semibold" href="#">My Vue JWT</a>

      <div class="d-flex ms-auto">
        <!-- <template v-if="auth.isAuthenticated">
          <span class="me-3 small text-muted">Olá, {{ auth.email }}</span>
          <button class="btn btn-outline-secondary btn-sm" @click="logout">Sair</button>
        </template> -->
        <template>
          <router-link class="btn btn-primary btn-sm" :to="{ name: 'login' }">Entrar</router-link>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup>
// import { useAuthStore } from '../stores/auth'
// const auth = useAuthStore()

// function logout() {
//   auth.logout()
// }
</script>
