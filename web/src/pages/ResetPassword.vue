<template>
  <div class="row justify-content-center">
    <div class="col-md-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h5 class="card-title mb-3">Definir nova senha</h5>
          <form novalidate class="needs-validation" :class="{ 'was-validated': tried }">
            <div class="mb-3">
              <label class="form-label">Nova senha</label>
              <input type="password" v-model="password" class="form-control" minlength="6" required />
              <div class="invalid-feedback">Mínimo de 6 caracteres.</div>
            </div>
            <div class="mb-3">
              <label class="form-label">Confirmar senha</label>
              <input type="password" v-model="confirm" class="form-control" :class="{ 'is-invalid': mismatch }" required />
              <div class="invalid-feedback">As senhas não conferem.</div>
            </div>
            <button class="btn btn-primary w-100" :disabled="loading || mismatch">
              <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
              Redefinir
            </button>

            <div v-if="success" class="alert alert-success mt-3">Senha alterada! Faça login.</div>
            <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// import { computed, ref } from 'vue'
// import { useRoute, useRouter } from 'vue-router'
// import { useAuthStore } from '../stores/auth'

// const route = useRoute()
// const router = useRouter()
// const token = route.params.token

// const password = ref('')
// const confirm = ref('')
// const tried = ref(false)
// const loading = ref(false)
// const success = ref(false)
// const error = ref(null)

// const mismatch = computed(() => confirm.value && password.value !== confirm.value)
// const auth = useAuthStore()

// async function onSubmit() {
//   tried.value = true
//   loading.value = true
//   success.value = false
//   error.value = null
//   try {
//     await auth.resetPassword(token, password.value)
//     success.value = true
//     setTimeout(() => router.push({ name: 'login' }), 1200)
//   } catch (e) {
//     error.value = 'Link inválido ou expirado.'
//   } finally {
//     loading.value = false
//   }
// }
</script>
