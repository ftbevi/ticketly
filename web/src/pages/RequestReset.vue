<template>
  <div class="row justify-content-center">
    <div class="col-md-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h5 class="card-title mb-3">Recuperar senha</h5>
          <form novalidate class="needs-validation" :class="{ 'was-validated': tried }">
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input type="email" v-model="email" class="form-control" required />
              <div class="invalid-feedback">Informe um e-mail válido.</div>
            </div>
            <button class="btn btn-primary w-100" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
              Enviar link de redefinição
            </button>
            <div v-if="success" class="alert alert-success mt-3">
              Se o e-mail existir, enviaremos instruções para redefinir sua senha.
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

// const email = ref('')
// const loading = ref(false)
// const tried = ref(false)
// const success = ref(false)
// const error = ref(null)

// const auth = useAuthStore()

// async function onSubmit() {
//   tried.value = true
//   success.value = false
//   error.value = null
//   loading.value = true
//   try {
//     await auth.requestReset(email.value)
//     success.value = true
//   } catch (e) {
//     error.value = 'Erro ao solicitar redefinição.'
//   } finally {
//     loading.value = false
//   }
// }
</script>
