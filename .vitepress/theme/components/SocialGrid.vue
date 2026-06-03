<template>
  <div class="social-cards-grid">
    <slot></slot>
  </div>
</template>

<style scoped>
.social-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
</style>