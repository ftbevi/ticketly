<template>
  <div class="row justify-content-center">
    <div class="col-md-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h5 class="card-title mb-3">Acesso</h5>
          <form novalidate class="needs-validation" :class="{ 'was-validated': tried }">
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input type="email" v-model="email" class="form-control" required />
              <div class="invalid-feedback">Informe um e-mail válido.</div>
            </div>
            <div class="mb-3">
              <label class="form-label">Senha</label>
              <input type="password" v-model="password" class="form-control" minlength="6" required />
              <div class="invalid-feedback">A senha deve ter ao menos 6 caracteres.</div>
            </div>

            <button class="btn btn-primary w-100" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
              Entrar
            </button>

            <div class="text-center mt-3">
              <router-link :to="{ name: 'request-reset' }" class="small">Esqueci minha senha</router-link>
            </div>

            <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
// import { useAuthStore } from '../stores/auth'
// import { useRoute, useRouter } from 'vue-router'

// const email = ref('')
// const password = ref('')
// const loading = ref(false)
// const error = ref(null)
// const tried = ref(false)

// const auth = useAuthStore()
// const route = useRoute()
// const router = useRouter()

// async function onSubmit() {
//   tried.value = true
//   error.value = null
//   loading.value = true
//   try {
//     await auth.login(email.value, password.value)
//     const to = route.query.redirect || { name: 'dashboard' }
//     router.push(to)
//   } catch (e) {
//     error.value = 'Credenciais inválidas.'
//   } finally {
//     loading.value = false
//   }
// }
</script>
