<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  
  <div class="greetings">
    <img alt="Vue logo" class="logo" src="src\assets\health_sign-removebg-preview.png" width="40 " height="40" />
    <h1 class="green">{{ msg }}</h1>
  </div>
</template>

<style scoped>
.greetings{
  display: flex;
  align-content: center;
}

.green {
  text-decoration: none;
  color: var(--primarycolor);
  transition: 0.4s;
}

.logo {
  background-color: var(--secondarycolor  );
}
</style>
