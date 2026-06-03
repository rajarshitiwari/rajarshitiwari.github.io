<template>
  <div class="cv-header-grid">
    <div class="cv-info">
      <slot></slot>
    </div>
    <div class="cv-photo" v-if="image">
      <img :src="image" alt="Profile Photo" />
    </div>
  </div>
</template>

<script setup>
defineProps({
  image: String
})
</script>

<style scoped>
.cv-header-grid {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 0.5rem; /* Tight gap to pull image and table closer together */
  align-items: center;
  margin-bottom: 2rem;
}

.cv-info :deep(table) {
  margin: 0;
  width: 100%;
}

.cv-photo img {
  width: 210px;
  height: auto;
  border-radius: 6px;
  margin-left: auto;
  display: block;
}

@media (max-width: 640px) {
  .cv-header-grid {
    grid-template-columns: 1fr;
  }
  .cv-photo img {
    margin: 0 auto;
  }
}
</style>